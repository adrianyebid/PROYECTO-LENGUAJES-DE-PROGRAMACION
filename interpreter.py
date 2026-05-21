"""
interpreter.py — Visitor ANTLR4 que evalúa el AST de MiniQL.

Flujo de procesamiento:
  1. ANTLR4 invoca el método visit* correspondiente a cada nodo del árbol.
  2. El estado del intérprete se mantiene en self._data (lista de dicts) y
     self._view (la proyección/filtro activa lista para SHOW).
  3. Las expresiones WHERE se evalúan de forma funcional con filter() + lambda.
"""

import csv
import os
from functools import reduce
from antlr4 import CommonTokenStream, InputStream

from MiniQLLexer  import MiniQLLexer
from MiniQLParser import MiniQLParser
from MiniQLVisitor import MiniQLVisitor


# ─────────────────────────────────────────────────────────────────────────────
# Manejador de errores personalizado
# Reemplaza el comportamiento por defecto de ANTLR4 (imprime y continúa)
# por mensajes más informativos que detienen la ejecución.
# ─────────────────────────────────────────────────────────────────────────────
from antlr4.error.ErrorListener import ErrorListener

class MiniQLErrorListener(ErrorListener):
    """Captura errores léxicos y sintácticos con mensajes de posición claros."""

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        token_text = getattr(offendingSymbol, "text", "?")
        raise SyntaxError(
            f"[Error sintáctico] Línea {line}:{column}  "
            f"token='{token_text}'  →  {msg}"
        )


# ─────────────────────────────────────────────────────────────────────────────
# Función auxiliar: coerción de tipos para comparaciones
# ─────────────────────────────────────────────────────────────────────────────
def _coerce(raw: str):
    """
    Convierte una cadena leída del CSV al tipo Python más adecuado.
    Intenta int → float → str, en ese orden.
    """
    try:
        return int(raw)
    except ValueError:
        pass
    try:
        return float(raw)
    except ValueError:
        pass
    return raw.strip()


def _coerce_literal(text: str):
    """
    Convierte un literal MiniQL (ya tokenizado) al tipo Python.
    Las cadenas pierden las comillas dobles; los números se convierten.
    """
    if text.startswith('"') and text.endswith('"'):
        return text[1:-1]          # quita comillas → str
    try:
        return int(text)
    except ValueError:
        pass
    try:
        return float(text)
    except ValueError:
        pass
    return text


# ─────────────────────────────────────────────────────────────────────────────
# Tabla de operadores de comparación (expresiones WHERE)
# ─────────────────────────────────────────────────────────────────────────────
_OPS = {
    "=":  lambda a, b: a == b,
    "!=": lambda a, b: a != b,
    "<":  lambda a, b: a <  b,
    ">":  lambda a, b: a >  b,
    "<=": lambda a, b: a <= b,
    ">=": lambda a, b: a >= b,
}


# ─────────────────────────────────────────────────────────────────────────────
# Visitor principal
# ─────────────────────────────────────────────────────────────────────────────
class MiniQLInterpreter(MiniQLVisitor):
    """
    Recorre el AST producido por MiniQLParser y ejecuta cada nodo.

    Estado interno:
        _data      — tabla completa cargada con LOAD (lista de dicts)
        _view      — resultado de la última operación SELECT/SORT (para SHOW)
        _gui_mode  — cuando True, SHOW acumula resultados en lugar de imprimir
        results    — [(descripción, headers, rows), ...] acumulados por SHOW
        log        — mensajes de texto (ej. LOAD) para mostrar en la GUI
    """

    def __init__(self, gui_mode: bool = False):
        self._data: list[dict] = []
        self._view: list[dict] = []
        self._gui_mode  = gui_mode
        self._last_desc = ""          # descripción del último SELECT (para tab GUI)
        self.results:  list = []      # (descripción, headers, rows) por SHOW
        self.log:      list[str] = [] # mensajes informativos (LOAD, etc.)

    # ── programa ──────────────────────────────────────────────────────────────

    def visitProgram(self, ctx: MiniQLParser.ProgramContext):
        """Punto de entrada: visita cada sentencia en orden."""
        for stmt in ctx.statement():
            self.visit(stmt)

    # ── LOAD ─────────────────────────────────────────────────────────────────

    def visitLoadStatement(self, ctx: MiniQLParser.LoadStatementContext):
        return self.visit(ctx.loadStmt())

    def visitLoadStmt(self, ctx: MiniQLParser.LoadStmtContext):
        """
        Fase 1 — Carga de datos.
        Lee el CSV y almacena cada fila como dict {columna: valor_raw}.
        """
        # El token STRING incluye las comillas; se eliminan con [1:-1]
        path = ctx.STRING().getText()[1:-1]

        if not os.path.exists(path):
            raise FileNotFoundError(f"[LOAD] Archivo no encontrado: '{path}'")

        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            self._data = [dict(row) for row in reader]

        self._view = list(self._data)   # la vista inicial es la tabla completa
        msg = (f"[LOAD] '{path}' — {len(self._data)} filas, "
               f"columnas: {list(self._data[0].keys()) if self._data else []}")
        if self._gui_mode:
            self.log.append(msg)
        else:
            print(msg + "\n")

    # ── SELECT ────────────────────────────────────────────────────────────────

    def visitSelectStatement(self, ctx: MiniQLParser.SelectStatementContext):
        return self.visit(ctx.selectStmt())

    def visitSelectStmt(self, ctx: MiniQLParser.SelectStmtContext):
        """
        Fase 2 — Proyección y filtrado (functional style).

        Pasos:
          a) Obtener la lista de columnas a proyectar.
          b) Construir un predicado Python desde el subárbol WHERE (si existe).
          c) Aplicar filter() sobre self._data para obtener filas válidas.
          d) Aplicar map() para proyectar solo las columnas solicitadas.
        """
        # a) Columnas
        cols = self.visit(ctx.columns())   # None → todas

        # b) Predicado WHERE (función fila → bool)
        if ctx.WHERE():
            predicate = self.visit(ctx.condition())
        else:
            predicate = lambda row: True   # sin filtro: todas las filas pasan

        # c) filter: selecciona filas que cumplen la condición
        filtered = filter(predicate, self._data)

        # d) map: proyecta las columnas deseadas
        if cols is None:
            self._view = list(filtered)
        else:
            self._view = list(
                map(lambda row: {c: row[c] for c in cols if c in row}, filtered)
            )

        # Guarda una descripción legible para el título de pestaña en la GUI
        cols_text = "*" if cols is None else ", ".join(cols)
        where_text = f" WHERE ..." if ctx.WHERE() else ""
        self._last_desc = f"SELECT {cols_text}{where_text}"

    # ── SORT ──────────────────────────────────────────────────────────────────

    def visitSortStatement(self, ctx: MiniQLParser.SortStatementContext):
        return self.visit(ctx.sortStmt())

    def visitSortStmt(self, ctx: MiniQLParser.SortStmtContext):
        """
        Fase 3 — Ordenamiento.
        Ordena self._view por la columna indicada usando _coerce para
        comparar correctamente enteros/flotantes, no lexicográficamente.
        """
        col       = ctx.ID().getText()
        direction = ctx.direction           # token ASC/DESC (puede ser None)
        descend   = (direction is not None and direction.text == "DESC")

        if self._view and col not in self._view[0]:
            raise KeyError(f"[SORT] Columna desconocida: '{col}'")

        self._view = sorted(
            self._view,
            key=lambda row: _coerce(row.get(col, "")),
            reverse=descend,
        )

    # ── SHOW ──────────────────────────────────────────────────────────────────

    def visitShowStatement(self, ctx: MiniQLParser.ShowStatementContext):
        return self.visit(ctx.showStmt())

    def visitShowStmt(self, ctx: MiniQLParser.ShowStmtContext):
        """
        Fase 4 — Presentación.
        Modo consola: imprime self._view como tabla formateada.
        Modo GUI:     acumula (descripción, headers, rows) en self.results.
        """
        if self._gui_mode:
            headers = list(self._view[0].keys()) if self._view else []
            self.results.append((self._last_desc, headers, list(self._view)))
        else:
            _print_table(self._view)

    # ── Columnas ──────────────────────────────────────────────────────────────

    def visitAllColumns(self, ctx: MiniQLParser.AllColumnsContext):
        """'*' → None indica "todas las columnas"."""
        return None

    def visitNamedColumns(self, ctx: MiniQLParser.NamedColumnsContext):
        """Lista de IDs separados por comas → lista de strings."""
        return [tok.getText() for tok in ctx.ID()]

    # ── Condiciones booleanas ─────────────────────────────────────────────────
    # Cada visitXxx devuelve una función  (dict → bool)  que el SELECT aplicará
    # con filter().  Esto es programación funcional pura: las condiciones son
    # valores de primera clase que se componen con and/or/not.

    def visitOrCond(self, ctx: MiniQLParser.OrCondContext):
        left  = self.visit(ctx.condition(0))
        right = self.visit(ctx.condition(1))
        # OR: la fila pasa si alguna sub-condición es verdadera
        return lambda row: left(row) or right(row)

    def visitAndCond(self, ctx: MiniQLParser.AndCondContext):
        left  = self.visit(ctx.condition(0))
        right = self.visit(ctx.condition(1))
        # AND: ambas sub-condiciones deben ser verdaderas
        return lambda row: left(row) and right(row)

    def visitNotCond(self, ctx: MiniQLParser.NotCondContext):
        inner = self.visit(ctx.condition())
        # NOT: invierte el resultado de la sub-condición
        return lambda row: not inner(row)

    def visitParenCond(self, ctx: MiniQLParser.ParenCondContext):
        # Los paréntesis no cambian la semántica; solo la precedencia en el AST
        return self.visit(ctx.condition())

    def visitCompCond(self, ctx: MiniQLParser.CompCondContext):
        return self.visit(ctx.comparison())

    # ── Comparación atómica ───────────────────────────────────────────────────

    def visitComparison(self, ctx: MiniQLParser.ComparisonContext):
        """
        col op valor  →  lambda row: _coerce(row[col]) op literal

        La clave de la evaluación funcional: devuelve una función, no un bool.
        El filter() del SELECT la llamará por cada fila.
        """
        col     = ctx.ID().getText()
        op_text = ctx.op.text
        literal = self.visit(ctx.value())    # valor Python ya tipado

        op_fn = _OPS.get(op_text)
        if op_fn is None:
            raise ValueError(f"Operador desconocido: '{op_text}'")

        # La comparación coerce el valor del CSV al tipo más adecuado antes
        # de comparar, para que "3500000 > 3000000" funcione como enteros.
        return lambda row: op_fn(_coerce(row.get(col, "")), literal)

    # ── Valores literales ─────────────────────────────────────────────────────

    def visitStringVal(self, ctx: MiniQLParser.StringValContext):
        return _coerce_literal(ctx.STRING().getText())

    def visitNumberVal(self, ctx: MiniQLParser.NumberValContext):
        return _coerce_literal(ctx.NUMBER().getText())

    def visitIdVal(self, ctx: MiniQLParser.IdValContext):
        # Un ID como valor literal se trata como string sin comillas
        return ctx.ID().getText()


# ─────────────────────────────────────────────────────────────────────────────
# Utilidad: impresión de tabla formateada
# ─────────────────────────────────────────────────────────────────────────────
def _print_table(rows: list[dict]) -> None:
    """Dibuja rows como tabla ASCII con bordes, alineada por ancho de columna."""
    if not rows:
        print("(sin resultados)\n")
        return

    headers = list(rows[0].keys())

    # Calcular ancho máximo por columna (header vs. datos)
    widths = {
        h: max(len(h), max(len(str(row.get(h, ""))) for row in rows))
        for h in headers
    }

    sep  = "+" + "+".join("-" * (widths[h] + 2) for h in headers) + "+"
    head = "|" + "|".join(f" {h:<{widths[h]}} " for h in headers) + "|"

    print(sep)
    print(head)
    print(sep)
    for row in rows:
        line = "|" + "|".join(
            f" {str(row.get(h, '')):<{widths[h]}} " for h in headers
        ) + "|"
        print(line)
    print(sep)
    print(f"  {len(rows)} fila(s)\n")


# ─────────────────────────────────────────────────────────────────────────────
# API pública: ejecutar un script MiniQL desde una cadena de texto
# ─────────────────────────────────────────────────────────────────────────────
def run_script_gui(source: str) -> tuple[list, list]:
    """
    Versión para la GUI: ejecuta el script y devuelve los resultados
    en lugar de imprimirlos.

    Returns:
        results  — lista de (descripción, headers, rows) por cada SHOW
        log      — mensajes informativos (LOAD, etc.)
    """
    input_stream = InputStream(source)
    lexer        = MiniQLLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(MiniQLErrorListener())

    token_stream = CommonTokenStream(lexer)
    parser       = MiniQLParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(MiniQLErrorListener())

    tree        = parser.program()
    interpreter = MiniQLInterpreter(gui_mode=True)
    interpreter.visit(tree)

    return interpreter.results, interpreter.log


def run_script(source: str) -> None:
    """
    Pipeline completo:
      texto fuente → InputStream → Lexer → TokenStream → Parser → AST → Visitor
    """
    # ── Fase léxica ───────────────────────────────────────────────────────────
    input_stream = InputStream(source)
    lexer        = MiniQLLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(MiniQLErrorListener())

    # ── Fase sintáctica ───────────────────────────────────────────────────────
    token_stream = CommonTokenStream(lexer)
    parser       = MiniQLParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(MiniQLErrorListener())

    # Construye el AST arrancando desde la regla inicial 'program'
    tree = parser.program()

    # ── Fase de evaluación ────────────────────────────────────────────────────
    interpreter = MiniQLInterpreter()
    interpreter.visit(tree)
