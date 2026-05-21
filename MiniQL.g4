// MiniQL.g4 — Gramática formal del lenguaje de consultas MiniQL
// Define las reglas léxicas y sintácticas que ANTLR4 convierte en lexer/parser Python.

grammar MiniQL;

// ─────────────────────────────────────────────
// REGLA INICIAL
// program es el axioma: una secuencia de sentencias seguida de EOF.
// ─────────────────────────────────────────────
program
    : statement+ EOF
    ;

// ─────────────────────────────────────────────
// SENTENCIAS DEL LENGUAJE
// Cada alternativa corresponde a uno de los cuatro comandos MiniQL.
// ─────────────────────────────────────────────
statement
    : loadStmt   # LoadStatement
    | selectStmt # SelectStatement
    | sortStmt   # SortStatement
    | showStmt   # ShowStatement
    ;

// LOAD "archivo.csv"
// Carga un archivo CSV en el contexto de ejecución.
loadStmt
    : LOAD STRING
    ;

// SELECT col1, col2  [WHERE condición]
// Proyecta columnas y filtra filas según la condición opcional.
selectStmt
    : SELECT columns (WHERE condition)?
    ;

// SORT BY col [ASC|DESC]
// Ordena el conjunto de datos actual por una columna.
sortStmt
    : SORT BY ID direction=(ASC | DESC)?
    ;

// SHOW
// Imprime en consola la tabla actualmente activa.
showStmt
    : SHOW
    ;

// ─────────────────────────────────────────────
// CLÁUSULA DE COLUMNAS
// '*' selecciona todas; de lo contrario, lista separada por comas.
// ─────────────────────────────────────────────
columns
    : STAR                  # AllColumns
    | ID (COMMA ID)*        # NamedColumns
    ;

// ─────────────────────────────────────────────
// CONDICIÓN WHERE — árbol de expresiones booleanas
// Precedencia (menor → mayor): OR → AND → NOT → átomo
// ─────────────────────────────────────────────
condition
    : condition OR  condition   # OrCond
    | condition AND condition   # AndCond
    | NOT condition             # NotCond
    | LPAREN condition RPAREN   # ParenCond
    | comparison                # CompCond
    ;

// Comparación atómica: identificador  operador  valor
comparison
    : ID op=(EQ | NEQ | LT | GT | LTE | GTE) value
    ;

// Valor literal que puede aparecer en el lado derecho de una comparación.
value
    : STRING    # StringVal
    | NUMBER    # NumberVal
    | ID        # IdVal
    ;

// ─────────────────────────────────────────────
// PALABRAS CLAVE (case-sensitive)
// ─────────────────────────────────────────────
LOAD   : 'LOAD'   ;
SELECT : 'SELECT' ;
WHERE  : 'WHERE'  ;
SORT   : 'SORT'   ;
BY     : 'BY'     ;
ASC    : 'ASC'    ;
DESC   : 'DESC'   ;
SHOW   : 'SHOW'   ;
AND    : 'AND'    ;
OR     : 'OR'     ;
NOT    : 'NOT'    ;

// ─────────────────────────────────────────────
// OPERADORES DE COMPARACIÓN
// ─────────────────────────────────────────────
EQ  : '='  ;
NEQ : '!=' ;
LTE : '<=' ;
GTE : '>=' ;
LT  : '<'  ;
GT  : '>'  ;

// ─────────────────────────────────────────────
// PUNTUACIÓN
// ─────────────────────────────────────────────
COMMA  : ','  ;
STAR   : '*'  ;
LPAREN : '('  ;
RPAREN : ')'  ;

// ─────────────────────────────────────────────
// LITERALES
// ─────────────────────────────────────────────
// Cadena entre comillas dobles (sin soporte de escape por simplicidad).
STRING : '"' (~["\r\n])* '"' ;

// Número entero o decimal, opcionalmente negativo.
NUMBER : '-'? [0-9]+ ('.' [0-9]+)? ;

// Identificador: letra/guión bajo seguido de alfanuméricos/guión bajo.
ID : [a-zA-Z_][a-zA-Z_0-9]* ;

// ─────────────────────────────────────────────
// TOKENS IGNORADOS
// ─────────────────────────────────────────────
WS      : [ \t\r\n]+  -> skip ;           // Espacios y saltos de línea
COMMENT : '//' ~[\r\n]* -> skip ;         // Comentarios de línea estilo //
