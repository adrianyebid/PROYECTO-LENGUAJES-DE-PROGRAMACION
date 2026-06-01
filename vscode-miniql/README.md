# Extensión MiniQL para VS Code

Resaltado de sintaxis (colores) y autocompletado para el lenguaje de consultas **MiniQL** (archivos `.mql`).

## Características

- **Colores** para comandos (`LOAD`, `SELECT`, `WHERE`, `SORT`, `BY`, `ASC`, `DESC`, `SHOW`),
  operadores lógicos (`AND`, `OR`, `NOT`), operadores de comparación, strings, números y comentarios `//`.
- **Autocompletado / snippets**: escribe `LOAD`, `SELECT`, `SORT`, `consulta`, etc. y presiona `Tab`.
- **Autocierre** de comillas `"` y paréntesis `(`.

## Instalación (modo desarrollo)

1. Abre la carpeta `vscode-miniql/` en VS Code.
2. Presiona `F5` → se abre una ventana nueva ("Extension Development Host").
3. Abre cualquier archivo `.mql` (por ejemplo `examples/consulta.mql`) y verás los colores.

## Instalación permanente (empaquetar)

```bash
npm install -g @vscode/vsce
cd vscode-miniql
vsce package
```

Esto genera un archivo `miniql-0.1.0.vsix`. Instálalo con:

```bash
code --install-extension miniql-0.1.0.vsix
```

O desde VS Code: `Extensiones` → `...` → `Install from VSIX...`
