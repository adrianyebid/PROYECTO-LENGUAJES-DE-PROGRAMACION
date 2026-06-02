MiniQL — Interprete de consultas sobre archivos CSV
====================================================
Proyecto Final — Lenguajes de Programacion
Universidad Nacional de Colombia

Autores:
  Adrian Rincon   (adrincon@unal.edu.co)
  Pablo Sandoval  (psandoval@unal.edu.co)
  John Paez       (jopaeza@unal.edu.co)

Descripcion
-----------
MiniQL es un interprete de un mini-lenguaje de consultas inspirado en SQL,
disenado para operar sobre archivos CSV. Se define mediante una gramatica
formal en ANTLR4 que genera automaticamente el analizador lexico (lexer) y
sintatico (parser). Un Visitor recorre el arbol de sintaxis abstracta (AST)
y evalua cada instruccion de forma funcional usando filter() y map().

Estructura del proyecto
-----------------------
miniQL/
├── MiniQL.g4           Gramatica formal ANTLR4 (archivo principal)
├── MiniQLLexer.py      Lexer generado por ANTLR4
├── MiniQLParser.py     Parser generado por ANTLR4
├── MiniQLVisitor.py    Visitor base generado por ANTLR4
├── interpreter.py      Visitor concreto — evalua el AST
├── gui.py              Aplicacion de escritorio (CustomTkinter)
├── main.py             Punto de entrada para consola
├── antlr-4.13.2-complete.jar  Herramienta ANTLR4
├── README.txt          Este archivo
└── examples/
    ├── datos.csv           Dataset de ejemplo (12 registros)
    ├── empleados.csv       Dataset ampliado (200 registros)
    ├── consulta.mql        Script de ejemplo con todos los comandos
    └── salida_consulta.txt Salida esperada al ejecutar consulta.mql

Sintaxis del lenguaje MiniQL
-----------------------------
  LOAD "archivo.csv"
  SELECT col1, col2 WHERE condicion
  SORT BY columna ASC|DESC
  SHOW

  Operadores de comparacion: =  !=  <  >  <=  >=
  Operadores logicos:        AND  OR  NOT  (...)
  Tipos soportados:          "cadena"  42  3.14

Requisitos
----------
  - Python 3.10 o superior
  - Java (para regenerar la gramatica, opcional)

Instalacion de dependencias
----------------------------
  pip install antlr4-python3-runtime==4.13.2 customtkinter

(!) Los archivos MiniQLLexer.py, MiniQLParser.py y MiniQLVisitor.py ya estan
    generados. Solo es necesario regenerarlos si se modifica MiniQL.g4:

  java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -no-listener MiniQL.g4

Uso — Interfaz de escritorio (recomendado)
------------------------------------------
  py -3.10 gui.py

  Panel izquierdo : Editor de codigo MiniQL
  Panel derecho   : Resultados — una pestana por cada SHOW
  Panel inferior  : Consola con mensajes de carga y errores
  Boton "Abrir CSV": Selecciona un CSV e inserta LOAD automaticamente
  Boton "Ejecutar" : Corre el pipeline completo

Uso — Linea de comandos
------------------------
  py -3.10 main.py examples/consulta.mql
  py -3.10 main.py mi_consulta.mql

Ejemplo rapido
--------------
  Contenido de mi_consulta.mql:

    LOAD "examples/datos.csv"
    SELECT nombre, salario WHERE departamento = "Ingenieria" AND salario > 3000000
    SORT BY salario DESC
    SHOW

  Ejecucion:
    py -3.10 main.py mi_consulta.mql

  Ver salida completa en: examples/salida_consulta.txt

Codigos de salida (modo consola)
---------------------------------
  0  Exito
  1  Argumento incorrecto (falta ruta del script)
  2  Error lexico o sintatico en el script MiniQL
  3  Archivo CSV no encontrado (LOAD)
  4  Columna inexistente (SELECT o SORT)
  5  Error inesperado
