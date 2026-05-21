# MiniQL

Intérprete de un mini-lenguaje de consultas sobre archivos CSV, construido con ANTLR4 y Python. Permite cargar datos, filtrarlos, ordenarlos y visualizarlos desde un editor de escritorio o desde la terminal.

---

## ¿Qué es MiniQL?

MiniQL es un lenguaje de consultas minimalista inspirado en SQL. Se define mediante una gramática formal en ANTLR4 que genera automáticamente el analizador léxico y sintáctico. Un visitor recorre el árbol de sintaxis abstracta (AST) y evalúa cada instrucción de forma funcional, usando `filter` y `map` sin bucles imperativos.

## Sintaxis

```sql
LOAD "archivo.csv"
SELECT col1, col2 WHERE condición
SORT BY columna ASC|DESC
SHOW
```

### Operadores disponibles en WHERE

| Comparación | Lógica |
|---|---|
| `=`  `!=`  `<`  `>`  `<=`  `>=` | `AND`  `OR`  `NOT`  `(...)` |

### Tipos soportados

- **String** → `"entre comillas"`
- **Entero** → `42`
- **Flotante** → `3.14`

### Ejemplo completo

```sql
LOAD "examples/datos.csv"

SELECT nombre, ciudad, salario WHERE departamento = "Ingeniería" AND salario > 3000000
SHOW

SORT BY salario DESC
SHOW
```

---

## Arquitectura

```
archivo.mql
    │
    ▼  Análisis léxico
MiniQLLexer       (generado por ANTLR4 desde MiniQL.g4)
    │  tokens
    ▼  Análisis sintáctico
MiniQLParser      (generado por ANTLR4 desde MiniQL.g4)
    │  AST
    ▼  Evaluación
MiniQLInterpreter (interpreter.py — Visitor sobre el AST)
    │
    ▼
Interfaz de escritorio (gui.py) o consola (main.py)
```

---

## Instalación

**Requisitos:** Python 3.10+

```bash
pip install antlr4-python3-runtime==4.13.2 customtkinter
```

> Los archivos `MiniQLLexer.py`, `MiniQLParser.py` y `MiniQLVisitor.py` ya están generados. Si modificas `MiniQL.g4` necesitas regenerarlos con el jar de ANTLR4:
> ```bash
> java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -no-listener MiniQL.g4
> ```

---

## Uso

### Interfaz de escritorio

```bash
py -3.10 gui.py
```

![Layout de la interfaz](https://i.imgur.com/placeholder.png)

| Panel | Descripción |
|---|---|
| Editor MiniQL | Escribe o pega tu consulta `.mql` |
| Resultados | Una pestaña por cada `SHOW`, con tabla scrolleable |
| Consola | Mensajes de carga, confirmaciones y errores |
| 📂 Abrir CSV | Selecciona un archivo y actualiza `LOAD` automáticamente |
| ▶ Ejecutar | Corre el pipeline completo |
| Toggle Oscuro/Claro | Cambia el tema en tiempo real |

### Línea de comandos

```bash
py -3.10 main.py examples/consulta.mql
```

---

## Estructura del proyecto

```
miniQL/
├── MiniQL.g4               Gramática formal ANTLR4
├── MiniQLLexer.py          Lexer (generado)
├── MiniQLParser.py         Parser (generado)
├── MiniQLVisitor.py        Visitor base (generado)
├── interpreter.py          Visitor concreto — evalúa el AST
├── gui.py                  Aplicación de escritorio (CustomTkinter)
├── main.py                 Entry point para consola
└── examples/
    ├── datos.csv           Dataset de ejemplo (12 registros)
    └── consulta.mql        Script de ejemplo con todos los comandos
```

---

## Tecnologías

- **ANTLR4** — generación del lexer y parser desde la gramática `.g4`
- **antlr4-python3-runtime** — runtime de ANTLR4 para Python
- **CustomTkinter** — interfaz de escritorio moderna
- **Python 3.10+** — única dependencia de lenguaje
