# GRUPO PYTHON
import ply
import ply.lex as lex
import ply.yacc as yacc
import os

reserved = {
    "if": "IF",
    "then": "THEN",
    "else": "ELSE",
    "while": "WHILE",
    "and" : "AND",
    "not" : "NOT",
    "is" : "IS",
    "for" : "FOR",
    "True" : "TRUE",
    "False" : "FALSE",
    "print":"PRINT",
    "or":"OR",
    "in":"IN",
    "range":"RANGE",
    "input":"INPUT",
    "append":"APPEND",
    "remove":"REMOVE",
    "def":"DEF",
    "return":"RETURN",
    "open":"OPEN"
}
tokens = ("ID","EQUALS","ASSIGN","NUMBER",
        "PLUS","MINUS","TIMES","DIVIDE","LESSTHAN","MORETHAN","LPAREN",
        "RPAREN",'DIVISIONENTERA','DOSPUNTOS',"NOTS",
        'COMILLAS','COMILLASSIMPLES','EXPONENTE','MOD','DIFERENTE','LLAVEDER',
        'LLAVEIZQ','CORCHETEDER','CORCHETEIZQ','COMA','SUBGUION','PUNTO','PUNTOCOMA'
        ) + tuple(reserved.values())
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r'\='
t_NOTS = r'\!'
t_LESSTHAN = r'\<'
t_MORETHAN = r'\>'
t_DIVISIONENTERA = r'\/\/'
t_MOD = r'\%'
t_EXPONENTE = r'\*\*'
t_DOSPUNTOS = r'\:'
t_COMILLAS = r'\"'
t_COMILLASSIMPLES = r'\''
t_LLAVEDER = r'\}'
t_LLAVEIZQ = r'\{'
t_CORCHETEDER = r'\]'
t_CORCHETEIZQ = r'\['
t_COMA = r'\,'
t_SUBGUION = r'\_'
t_PUNTO = r'\.';
t_PUNTOCOMA = r'\;'



def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t
t_ignore  = ' \t'
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

data = '''
3 + 4 * 10
  + -20 *2
  _hola
  while
  for
  if
  else
'''

# Give the lexer some input

def analizar(data):
    lexer = lex.lex()
    lexer.input(linea)
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
# Give the lexer some input
#lexer.input(data)
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'archivo.txt')
archivo = open(my_file,'r')
for linea in archivo:
    print(">> "+linea)
    analizar(linea)