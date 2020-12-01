# GRUPO PYTHON
import ply
import ply.lex as lex
import ply.yacc as yacc
import os

conectoresLogicos = {"and" : "AND","not" : "NOT","is" : "IS","or":"OR","in":"IN",}

estructuras_control = {"if": "IF", "else": "ELSE", "while": "WHILE", "for" : "FOR","range":"RANGE"}

IO_reserved = {"print":"PRINT","input":"INPUT","open":"OPEN"}

funcion = {"def":"DEF","return":"RETURN","None":"NONE"}

metodos = {"append":"APPEND","remove":"REMOVE",}

tipo_datos = {"number":"NUMBER","float":"FLOAT", "boolean" : "BOOLEAN"}
    
otros = {"id":"ID","comments":"COMMENTS","comment":"COMMENT", "cadena":"CADENA","string":"STRING","import":"IMPORT","as":"AS"}   
    
reserved = { **conectoresLogicos, **tipo_datos,**estructuras_control, **IO_reserved, **funcion, **metodos, **otros}

t_CADENA = r'(\"[a-zA-Z0-9.*]*\")|(\'[a-zA-Z0-9.*]*\')'


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

tokens_logicos = ('MAYORIGUAL','MENORIGUAL','ASSIGN','NOTS','LESSTHAN','MORETHAN','EQUALS','DIFERENTE')
#operadores logicos
t_MAYORIGUAL = r'\>(\ )?\='
t_MENORIGUAL = r'\<(\ )?\='
t_EQUALS = r'\=(\ )?\='
t_DIFERENTE = r'\!(\ )?\='
t_ASSIGN = r'\='
t_NOTS = r'\!'
t_LESSTHAN = r'\<'
t_MORETHAN = r'\>'

tokens_llaves = ('LPAREN','RPAREN','LLAVEIZQ','LLAVEDER','CORCHETEDER','CORCHETEIZQ',)
#llaves,corechetes,parentesis
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LLAVEDER = r'\}'
t_LLAVEIZQ = r'\{'
t_CORCHETEDER = r'\]'
t_CORCHETEIZQ = r'\['

#UNION de todos los tokens
tokens = tuple(reserved.values()) + tokens_operadores + tokens_logicos + tokens_llaves + tokens_puntuacion 
#Funciones dicionales
def t_BOOLEAN(t):
    r'(True) | (False)'
    return t

def t_STRING(t):
    r'^"[a-zA-Z_0-9\s\ ]*"$'
    t.value = str(t.value)
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

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
    t.lexer.skip(1)
    return "Ilegal"

def t_COMMENT(t):
     r'\#. *'
     return t

def t_COMMENTS(t):
     r'\'\'\'[a-zA-Z0-9\w\s]*\'\'\''
     t.type = otros.get(t.value,"COMMENTS")
     return t

lexer = lex.lex()

def analizar(linea):
    lexer = lex.lex()
    lexer.input(linea)
    lista = []
    while True:
        tok = lexer.token()
        if not tok: 
            break      
        lista.append(tok)
    return lista
 
""" THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'algoritmoPrueba\henryAlgoritmo.py')

archivo = open(my_file,'r',encoding="utf-8")
for linea in archivo:
    print(">> "+linea)
    print(analizar(linea))
archivo.close()    """   