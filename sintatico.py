import ply.yacc as yacc
import os
from lexicoPython import tokens

def p_cuerpo(p):
    '''cuerpo : expression
              | comentario
              | asignacion
              | valoresComa
              | lista
              | tupla
              | comparacion
              | if
              '''
    p[0] = p[1]

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    '''factor : NUMBER
              | STRING
              | FLOAT
              | CADENA'''
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_comentario(p):
    '''comentario : COMMENT
                 | COMMENTS'''
    p[0] = "COMENTARIO"

def p_asignacion(p):
    '''asignacion : ID ASSIGN expression
                  | multipleAsignacion expression
                  | ID ASSIGN BOOLEAN
                  | ID ASSIGN lista'''
    p[0] = "ASIGNACION"

def p_multipleAsignacion(p):
    '''multipleAsignacion : ID ASSIGN 
                          | ID ASSIGN multipleAsignacion 
                          '''

def p_valoresComa(p):
    '''valoresComa : factor
                   | valoresComa COMA factor'''
    p[0] = "COMAS"

def p_lista(p):
    '''lista : CORCHETEIZQ valoresComa CORCHETEDER'''
    p[0] = "LISTA"
def p_tupla(p):
    '''tupla : LPAREN valoresComa RPAREN'''
    p[0] = "TUPLA"
def p_comparacion(p):
    '''comparacion : BOOLEAN
                   |  NOTS BOOLEAN
                   | expression EQUALS expression
                   | expression MAYORIGUAL expression
                   | expression MENORIGUAL expression
                   | expression LESSTHAN expression
                   | expression MORETHAN expression
                   | expression DIFERENTE expression'''
    p[0] = "comparacion"

def p_if(p):
    '''if : MOD LPAREN comparacion RPAREN DOSPUNTOS'''
    p[0] = "IF"


    
    


""" def p_multipleAsignacionComa(p):
    '''multipleAsignacionComa : ID ASSIGN "(" COMA ID ASSIGN ")" "*" expression''' """


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()


THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'archivo.txt')
archivo = open(my_file,'r',encoding="utf-8")
for linea in archivo:
    print(">> "+linea)
    s = linea
    result = parser.parse(s)
    print(result)
archivo.close()
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result) 
     