"""
main.py — Punto de entrada de MiniQL.

Uso:
    py -3.10 main.py examples/consulta.mql
    py -3.10 main.py mi_consulta.mql
"""

import sys
import os

# Fuerza UTF-8 en la salida estándar (necesario en Windows con terminales CP1252)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from interpreter import run_script


def main() -> None:
    # ── Validar argumento ─────────────────────────────────────────────────────
    if len(sys.argv) != 2:
        print("Uso: python main.py <archivo.mql>")
        print("Ejemplo: python main.py examples/consulta.mql")
        sys.exit(1)

    script_path = sys.argv[1]

    if not os.path.exists(script_path):
        print(f"[Error] Archivo no encontrado: '{script_path}'")
        sys.exit(1)

    # ── Leer el script MiniQL ─────────────────────────────────────────────────
    with open(script_path, encoding="utf-8") as f:
        source = f.read()

    print(f"=== MiniQL — ejecutando '{script_path}' ===\n")

    # ── Ejecutar: léxico → sintáctico → evaluación ────────────────────────────
    try:
        run_script(source)
    except SyntaxError as e:
        # Error léxico o sintáctico detectado por el listener ANTLR4
        print(f"\n{e}", file=sys.stderr)
        sys.exit(2)
    except FileNotFoundError as e:
        # CSV no encontrado durante LOAD
        print(f"\n{e}", file=sys.stderr)
        sys.exit(3)
    except KeyError as e:
        # Columna inexistente referenciada en SELECT o SORT
        print(f"\n[Error semántico] {e}", file=sys.stderr)
        sys.exit(4)
    except Exception as e:
        print(f"\n[Error] {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(5)


if __name__ == "__main__":
    main()
