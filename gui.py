"""
gui.py — Interfaz de escritorio para MiniQL usando CustomTkinter.

Layout:
  ┌──────────────────────────────────────────────────────────┐
  │  Toolbar: título · Abrir CSV · Ejecutar · Limpiar · tema │
  ├────────────────────┬─────────────────────────────────────┤
  │  Editor MiniQL     │  Resultados (pestañas por SHOW)     │
  │  (CTkTextbox)      │  (ttk.Treeview con scrollbars)      │
  ├────────────────────┴─────────────────────────────────────┤
  │  Consola: mensajes de LOAD, errores, estado              │
  └──────────────────────────────────────────────────────────┘
"""

import sys
import os
import re
import tkinter as tk
from tkinter import ttk, filedialog

import customtkinter as ctk

# Fuerza UTF-8 en salida estándar (Windows)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# ── Paletas de color para el Treeview según el modo ──────────────────────────
_PALETTE = {
    "dark": {
        "tree_bg":    "#1e1e2e",
        "tree_fg":    "#cdd6f4",
        "field_bg":   "#1e1e2e",
        "head_bg":    "#181825",
        "head_fg":    "#89b4fa",
        "sel_bg":     "#313244",
        "row_odd":    "#1e1e2e",
        "row_even":   "#252535",
        "console_fg": "#a6e3a1",
        "console_bg": "#11111b",
        "border":     "#313244",
    },
    "light": {
        "tree_bg":    "#eff1f5",
        "tree_fg":    "#4c4f69",
        "field_bg":   "#ffffff",
        "head_bg":    "#dce0e8",
        "head_fg":    "#1e66f5",
        "sel_bg":     "#bcc0cc",
        "row_odd":    "#eff1f5",
        "row_even":   "#e6e9ef",
        "console_fg": "#40a02b",
        "console_bg": "#dce0e8",
        "border":     "#bcc0cc",
    },
}

# Script que aparece en el editor al iniciar la aplicación
_DEFAULT_SCRIPT = """\
// Script MiniQL de ejemplo
LOAD "examples/datos.csv"

// Todos los registros
SELECT *
SHOW

// Ingenieros con salario > 3,000,000
SELECT nombre, ciudad, salario WHERE departamento = "Ingeniería" AND salario > 3000000
SHOW

// Ordenar por salario descendente
SORT BY salario DESC
SHOW

// Empleados jóvenes en Bogotá
SELECT nombre, edad, departamento WHERE edad < 30 AND ciudad = "Bogotá"
SHOW
"""


class MiniQLApp(ctk.CTk):
    """Ventana principal de la aplicación MiniQL Desktop."""

    def __init__(self):
        super().__init__()

        self.title("MiniQL Desktop")
        self.geometry("1350x820")
        self.minsize(960, 640)

        # Estado interno
        self._dark_mode = True
        self._show_count = 0

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self._build_root_grid()
        self._build_toolbar()
        self._build_main_area()
        self._build_console()
        self._apply_tree_style()  # estilo inicial de ttk.Treeview

    # ── Grid raíz ─────────────────────────────────────────────────────────────

    def _build_root_grid(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)  # toolbar
        self.grid_rowconfigure(1, weight=1)  # editor + resultados
        self.grid_rowconfigure(2, weight=0)  # consola

    # ── Toolbar ───────────────────────────────────────────────────────────────

    def _build_toolbar(self):
        tb = ctk.CTkFrame(self, height=58, corner_radius=0,
                          fg_color=("gray90", "#12121f"))
        tb.grid(row=0, column=0, sticky="ew")
        tb.grid_propagate(False)

        # Título
        ctk.CTkLabel(
            tb, text="  ⚡ MiniQL",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="#89b4fa",
        ).pack(side="left", padx=(8, 24), pady=8)

        # Botón abrir CSV
        ctk.CTkButton(
            tb, text="📂  Abrir CSV", width=130,
            command=self._open_csv,
        ).pack(side="left", padx=4, pady=10)

        # Botón ejecutar (verde)
        ctk.CTkButton(
            tb, text="▶  Ejecutar", width=120,
            fg_color=("#2ecc71", "#2ecc71"),
            hover_color=("#27ae60", "#27ae60"),
            text_color="white",
            font=ctk.CTkFont(weight="bold"),
            command=self._execute,
        ).pack(side="left", padx=4, pady=10)

        # Botón limpiar
        ctk.CTkButton(
            tb, text="🗑  Limpiar", width=110,
            fg_color=("gray65", "gray30"),
            hover_color=("gray55", "gray25"),
            command=self._clear,
        ).pack(side="left", padx=4, pady=10)

        # Etiqueta CSV activo
        self._csv_lbl = ctk.CTkLabel(
            tb, text="Sin archivo cargado",
            text_color="gray55",
            font=ctk.CTkFont(size=12),
        )
        self._csv_lbl.pack(side="left", padx=20)

        # Toggle oscuro/claro (derecha)
        self._theme_var = ctk.BooleanVar(value=True)
        ctk.CTkSwitch(
            tb, text="Oscuro",
            variable=self._theme_var,
            onvalue=True, offvalue=False,
            command=self._toggle_theme,
        ).pack(side="right", padx=16, pady=10)

    # ── Área principal (editor + resultados) ──────────────────────────────────

    def _build_main_area(self):
        # PanedWindow horizontal permite redimensionar la división
        sash_bg = "#12121f" if self._dark_mode else "#dce0e8"
        self._paned = tk.PanedWindow(
            self, orient=tk.HORIZONTAL,
            sashwidth=7, sashrelief=tk.FLAT,
            bg=sash_bg,
        )
        self._paned.grid(row=1, column=0, sticky="nsew", padx=4, pady=4)

        self._build_editor_panel()
        self._build_results_panel()

    def _build_editor_panel(self):
        """Panel izquierdo: editor de código MiniQL."""
        left = ctk.CTkFrame(self._paned, corner_radius=8)
        self._paned.add(left, minsize=260, width=430)

        # Encabezado del editor
        hdr = ctk.CTkFrame(left, fg_color="transparent")
        hdr.pack(fill="x", padx=10, pady=(8, 2))
        ctk.CTkLabel(
            hdr, text="Editor MiniQL",
            font=ctk.CTkFont(size=13, weight="bold"),
        ).pack(side="left")
        ctk.CTkLabel(
            hdr, text="// soporta AND, OR, NOT, paréntesis",
            font=ctk.CTkFont(size=10),
            text_color="gray55",
        ).pack(side="left", padx=10)

        # Área de texto del editor
        self._editor = ctk.CTkTextbox(
            left,
            font=ctk.CTkFont(family="Consolas", size=13),
            wrap="none",
            undo=True,
            border_width=1,
            border_color=("gray75", "#313244"),
        )
        self._editor.pack(fill="both", expand=True, padx=8, pady=(0, 8))
        self._editor.insert("end", _DEFAULT_SCRIPT)

    def _build_results_panel(self):
        """Panel derecho: pestañas con las tablas de resultados."""
        right = ctk.CTkFrame(self._paned, corner_radius=8)
        self._paned.add(right, minsize=400)

        # Encabezado de resultados
        hdr = ctk.CTkFrame(right, fg_color="transparent")
        hdr.pack(fill="x", padx=10, pady=(8, 2))
        ctk.CTkLabel(
            hdr, text="Resultados",
            font=ctk.CTkFont(size=13, weight="bold"),
        ).pack(side="left")
        self._stats_lbl = ctk.CTkLabel(
            hdr, text="",
            font=ctk.CTkFont(size=11),
            text_color="gray55",
        )
        self._stats_lbl.pack(side="left", padx=12)

        # Notebook para múltiples SHOW
        self._notebook = ttk.Notebook(right, style="MiniQL.TNotebook")
        self._notebook.pack(fill="both", expand=True, padx=8, pady=(0, 8))

        self._add_placeholder_tab()

    def _add_placeholder_tab(self):
        """Pestaña vacía que se muestra antes de ejecutar una consulta."""
        ph = tk.Frame(self._notebook, bg="#1e1e2e" if self._dark_mode else "#eff1f5")
        self._notebook.add(ph, text="  Sin resultados  ")
        tk.Label(
            ph,
            text="Ejecuta una consulta con ▶ para ver resultados aquí.",
            fg="#585b70", bg="#1e1e2e" if self._dark_mode else "#eff1f5",
            font=("Segoe UI", 11),
        ).place(relx=0.5, rely=0.5, anchor="center")

    # ── Consola ───────────────────────────────────────────────────────────────

    def _build_console(self):
        cf = ctk.CTkFrame(self, height=148, corner_radius=0,
                          fg_color=("gray90", "#12121f"))
        cf.grid(row=2, column=0, sticky="ew")
        cf.grid_propagate(False)
        cf.grid_columnconfigure(0, weight=1)
        cf.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(
            cf, text="  Consola",
            font=ctk.CTkFont(size=12, weight="bold"),
        ).grid(row=0, column=0, sticky="w", pady=(4, 0))

        # tk.Text para soportar colores por etiqueta (CTkTextbox no lo permite)
        self._console = tk.Text(
            cf,
            font=("Consolas", 11),
            state="disabled",
            relief="flat",
            bd=0,
            wrap="word",
            bg="#11111b",
            fg="#a6e3a1",
            insertbackground="white",
            selectbackground="#313244",
        )
        self._console.grid(row=1, column=0, sticky="nsew", padx=8, pady=(2, 8))

        # Etiquetas de color para la consola
        self._console.tag_configure("info",    foreground="#a6e3a1")
        self._console.tag_configure("load",    foreground="#89b4fa")
        self._console.tag_configure("ok",      foreground="#a6e3a1")
        self._console.tag_configure("warning", foreground="#f9e2af")
        self._console.tag_configure("error",   foreground="#f38ba8")

    # ── Acciones de la UI ──────────────────────────────────────────────────────

    def _open_csv(self):
        """Abre un diálogo para seleccionar CSV e inyecta LOAD en el editor."""
        path = filedialog.askopenfilename(
            title="Seleccionar archivo CSV",
            filetypes=[("CSV", "*.csv"), ("Todos", "*.*")],
        )
        if not path:
            return

        # Ruta absoluta con barras normales (evita problemas de ruta relativa)
        abs_path = os.path.abspath(path).replace("\\", "/")
        self._csv_lbl.configure(text=f"📄 {os.path.basename(abs_path)}")

        # Reemplaza LOAD existente o antepone uno nuevo
        content = self._editor.get("1.0", "end-1c")
        new = re.sub(r'LOAD\s+"[^"]*"', f'LOAD "{abs_path}"', content)
        if new == content:          # no había LOAD → anteponer
            new = f'LOAD "{abs_path}"\n\n' + content
        self._editor.delete("1.0", "end")
        self._editor.insert("end", new)
        self._log(f"[CSV] Seleccionado: {abs_path}", "load")

    def _execute(self):
        """Parsea y evalúa el contenido del editor; muestra resultados en tabs."""
        source = self._editor.get("1.0", "end-1c").strip()
        if not source:
            self._log("⚠  El editor está vacío.", "warning")
            return

        # Limpiar resultados previos
        for tab in self._notebook.tabs():
            self._notebook.forget(tab)
        self._show_count = 0
        self._stats_lbl.configure(text="")

        self._log("▶  Ejecutando...", "load")

        try:
            from interpreter import run_script_gui

            # Pipeline: léxico → sintáctico → evaluación
            results, log_msgs = run_script_gui(source)

            # Mensajes del intérprete (LOAD, etc.)
            for msg in log_msgs:
                self._log(msg, "load")

            if not results:
                self._add_placeholder_tab()
                self._log("ℹ  Ejecución completada sin comandos SHOW.", "warning")
                return

            total_rows = 0
            for desc, headers, rows in results:
                self._show_count += 1
                tab_title = f"  SHOW {self._show_count}  ({len(rows)} filas)  "
                self._add_result_tab(tab_title, desc, headers, rows)
                total_rows += len(rows)

            self._stats_lbl.configure(
                text=f"{self._show_count} tabla(s)  ·  {total_rows} fila(s) total"
            )
            self._log(
                f"✓  Listo — {self._show_count} resultado(s), {total_rows} fila(s).",
                "ok",
            )

        except SyntaxError as e:
            self._add_placeholder_tab()
            self._log(f"[Error sintáctico]  {e}", "error")
        except FileNotFoundError as e:
            self._add_placeholder_tab()
            self._log(f"[Error LOAD]  {e}", "error")
        except KeyError as e:
            self._add_placeholder_tab()
            self._log(f"[Error semántico]  Columna desconocida: {e}", "error")
        except Exception as e:
            self._add_placeholder_tab()
            self._log(f"[Error]  {type(e).__name__}: {e}", "error")

    def _clear(self):
        """Limpia el editor, las pestañas y la consola."""
        self._editor.delete("1.0", "end")
        for tab in self._notebook.tabs():
            self._notebook.forget(tab)
        self._add_placeholder_tab()
        self._stats_lbl.configure(text="")
        self._show_count = 0

        self._console.configure(state="normal")
        self._console.delete("1.0", "end")
        self._console.configure(state="disabled")

    def _toggle_theme(self):
        """Alterna entre modo oscuro y claro y actualiza todos los estilos."""
        self._dark_mode = self._theme_var.get()
        mode = "dark" if self._dark_mode else "light"
        ctk.set_appearance_mode(mode)
        self._apply_tree_style()

        # Actualizar fondo de la consola
        p = _PALETTE[mode]
        self._console.configure(bg=p["console_bg"], fg=p["console_fg"])
        self._console.tag_configure("load",    foreground="#89b4fa")
        self._console.tag_configure("ok",      foreground=p["console_fg"])
        self._console.tag_configure("warning", foreground="#f9e2af")
        self._console.tag_configure("error",   foreground="#f38ba8")

    # ── Tabla de resultados ───────────────────────────────────────────────────

    def _add_result_tab(
        self,
        tab_title: str,
        desc: str,
        headers: list[str],
        rows: list[dict],
    ):
        """Crea una pestaña con un ttk.Treeview para mostrar los datos."""
        p = _PALETTE["dark" if self._dark_mode else "light"]

        outer = tk.Frame(self._notebook, bg=p["tree_bg"])
        self._notebook.add(outer, text=tab_title)

        # Etiqueta de descripción (la cláusula SELECT usada)
        tk.Label(
            outer,
            text=f"  {desc}",
            fg=p["head_fg"], bg=p["head_bg"],
            font=("Consolas", 10),
            anchor="w",
        ).pack(fill="x")

        # Frame interior para Treeview + scrollbars
        inner = tk.Frame(outer, bg=p["tree_bg"])
        inner.pack(fill="both", expand=True)

        vsb = ttk.Scrollbar(inner, orient="vertical")
        hsb = ttk.Scrollbar(inner, orient="horizontal")
        vsb.pack(side="right", fill="y")
        hsb.pack(side="bottom", fill="x")

        tree = ttk.Treeview(
            inner,
            columns=headers,
            show="headings",
            yscrollcommand=vsb.set,
            xscrollcommand=hsb.set,
            style="MiniQL.Treeview",
        )
        tree.pack(fill="both", expand=True)
        vsb.config(command=tree.yview)
        hsb.config(command=tree.xview)

        # Configurar columnas: ancho dinámico basado en contenido
        for col in headers:
            max_len = max(
                [len(col)] + [len(str(r.get(col, ""))) for r in rows]
            )
            width = min(max(max_len * 9, 70), 300)
            tree.heading(col, text=col, anchor="w")
            tree.column(col, anchor="w", width=width, minwidth=60, stretch=True)

        # Insertar filas con colores alternos
        tree.tag_configure("odd",  background=p["row_odd"])
        tree.tag_configure("even", background=p["row_even"])
        for i, row in enumerate(rows):
            tag = "odd" if i % 2 == 0 else "even"
            tree.insert("", "end",
                        values=[row.get(h, "") for h in headers],
                        tags=(tag,))

        # Dar el foco a la nueva pestaña
        self._notebook.select(outer)

    # ── Estilo del Treeview ───────────────────────────────────────────────────

    def _apply_tree_style(self):
        """Actualiza los estilos de ttk.Treeview y ttk.Notebook al tema actual."""
        p   = _PALETTE["dark" if self._dark_mode else "light"]
        s   = ttk.Style()

        # Usar tema 'clam' como base (permite personalización de colores)
        s.theme_use("clam")

        # Treeview
        s.configure("MiniQL.Treeview",
                    background=p["tree_bg"],
                    foreground=p["tree_fg"],
                    fieldbackground=p["field_bg"],
                    rowheight=27,
                    borderwidth=0,
                    font=("Segoe UI", 10))
        s.configure("MiniQL.Treeview.Heading",
                    background=p["head_bg"],
                    foreground=p["head_fg"],
                    relief="flat",
                    font=("Segoe UI", 10, "bold"),
                    padding=(8, 5))
        s.map("MiniQL.Treeview",
              background=[("selected", p["sel_bg"])],
              foreground=[("selected", p["tree_fg"])])

        # Notebook
        s.configure("MiniQL.TNotebook",
                    background=p["tree_bg"],
                    borderwidth=0)
        s.configure("MiniQL.TNotebook.Tab",
                    background=p["head_bg"],
                    foreground=p["head_fg"],
                    padding=(10, 5),
                    font=("Segoe UI", 10))
        s.map("MiniQL.TNotebook.Tab",
              background=[("selected", p["sel_bg"])],
              foreground=[("selected", p["head_fg"])])

    # ── Logger de consola ─────────────────────────────────────────────────────

    def _log(self, text: str, level: str = "info"):
        """Añade una línea de texto a la consola con color según el nivel."""
        self._console.configure(state="normal")
        self._console.insert("end", text + "\n", level)
        self._console.configure(state="disabled")
        self._console.see("end")


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app = MiniQLApp()
    app.mainloop()
