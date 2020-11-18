# GRUPO PYTHON
import ply
import ply.lex as lex
import ply.yacc as yacc
import os

conectoresLogicos = {"and" : "AND","not" : "NOT","is" : "IS","or":"OR","in":"IN",}

estructuras_control = {"if": "IF", "else": "ELSE", "while": "WHILE", "for" : "FOR",}

booleanos = {"True" : "TRUE","False" : "FALSE",}

IO_reserved = {"print":"PRINT","input":"INPUT","open":"OPEN",}

funcion = {"def":"DEF","return":"RETURN",}

metodos = {"append":"APPEND","remove":"REMOVE",}
    
otros = {"number":"NUMBER","id":"ID","range":"RANGE", "comments":"COMMENTS"}   
    
reserved = conectoresLogicos and estructuras_control and booleanos and IO_reserved and funcion and metodos and otros

tokens_puntuacion = ('DOSPUNTOS','COMILLAS','COMILLASSIMPLES','COMA','PUNTOCOMA','PUNTO','SUBGUION')
#puntuacion
t_DOSPUNTOS = r'\:'
t_COMILLAS = r'\"'
t_COMILLASSIMPLES = r'\''
t_COMA = r'\,'
t_PUNTOCOMA = r'\;'
t_PUNTO = r'\.'
t_SUBGUION = r'\_'

tokens_operadores = ("PLUS",'MINUS','TIMES','EXPONENTE','MOD','DIVISIONENTERA','DIVIDE',)
#operadores matematicos
t_PLUS = r'\+'
t_MINUS = r'\-'
t_EXPONENTE = r'\*\*'
t_TIMES = r'\*'
t_MOD = r'\%'
t_DIVISIONENTERA = r'\/\/'
t_DIVIDE = r'\/'

tokens_logicos = ('ASSIGN','NOTS','LESSTHAN','MORETHAN','EQUALS','DIFERENTE','MAYORIGUAL','MENORIGUAL')
#operadores logicos
t_ASSIGN = r'\='
t_NOTS = r'\!'
t_MAYORIGUAL = r'\>\='
t_MENORIGUAL = r'\<\='
t_LESSTHAN = r'\<'
t_MORETHAN = r'\>'
t_EQUALS = r'\=\='
t_DIFERENTE = r'\!\='

tokens_llaves = ('LPAREN','RPAREN','LLAVEIZQ','LLAVEDER','CORCHETEDER','CORCHETEIZQ',)
#llaves,corechetes,parentesis
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LLAVEDER = r'\}'
t_LLAVEIZQ = r'\{'
t_CORCHETEDER = r'\]'
t_CORCHETEIZQ = r'\['

#UNION de todos los tokens
tokens = tokens_operadores + tokens_logicos + tokens_llaves + tokens_puntuacion + tuple(reserved.values())
#Funciones dicionales
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = otros.get(t.value,'ID')    # Check for reserved words
    return t

t_ignore  = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_COMMENT(t):
     r'\#.*'
     pass

def t_COMMENTS(t):
     r'\/\*[a-zA-Z0-9\w\s]*\*\/'
     t.type = otros.get(t.value,"COMMENTS")
     return t

lexer = lex.lex()

def analizar(data):
    lexer = lex.lex()
    lexer.input(linea)
    while True:
        tok = lexer.token()
        if not tok: 
            break      
        print(tok)

""" THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'archivo.txt') """
archivo = open('archivo.txt','r',encoding="utf-8")
for linea in archivo:
    print(">> "+linea)
    analizar(linea)
archivo.close()