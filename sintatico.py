import ply.yacc as yacc
import os
from lexicoPython import tokens

def p_cuerpo(p):
    '''cuerpo : expression
              | comentario
              | asignacion
              | valoresComa
              | lista
              | if
              | while   
              | for 
              | print  
              | inputF
              | openF 
              | funcion 
              | comparacion   
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

def p_term_cuadrado(p):
    'term : term EXPONENTE factor'
    p[0] = p[1] ** p[3]

def p_term_divEntera(p):
    'term : term DIVISIONENTERA factor'
    p[0] = p[1] // p[3]

def p_term_Mod(p):
    'term : term MOD factor'
    p[0] = p[1] % p[3]

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
                  | asignacionComa
                  | ID ASSIGN BOOLEAN
                  | ID ASSIGN lista
                  | ID ASSIGN tupla'''
    p[0] = "ASIGNACION"

def p_multipleAsignacion(p):
    '''multipleAsignacion : ID ASSIGN 
                          | ID ASSIGN multipleAsignacion 
                          '''
def p_asignacionComa(p):
    'asignacionComa : valoresComaID ASSIGN valoresComa'

def p_valoresComaID(p):
    '''valoresComaID : ID
                   | valoresComaID COMA ID'''

def p_valoresComa(p):
    '''valoresComa : factor
                   | valoresComa COMA factor
                   | valoresComa COMA'''
    p[0] = "COMAS"

def p_lista(p):
    '''lista : CORCHETEIZQ valoresComa CORCHETEDER'''
    p[0] = "LISTA"

def p_tupla(p):
    '''tupla : LPAREN valoresComa RPAREN'''
    p[0] = "TUPLA"

def p_comparacion(p):
    '''comparacion : BOOLEAN
                   | NOTS BOOLEAN
                   | expression operadorLogico expression
                   | ID operadorLogico ID'''
    p[0] = "COMPARACION"

def p_operadorLogico(p):
    '''operadorLogico : EQUALS
                      | MAYORIGUAL
                      | MENORIGUAL
                      | LESSTHAN
                      | MORETHAN
                      | DIFERENTE
    '''
def p_conectoresLogicos(p):
    '''conectoresLogicos : AND
                         | OR'''

def p_operacionConectoresLogicos(p):
    '''operacionConectoresLogicos : 
    '''

def p_if(p):
    '''if : IF LPAREN comparacion RPAREN DOSPUNTOS'''
    p[0] = "IF"

def p_while(p):
    '''while : WHILE LPAREN comparacion RPAREN DOSPUNTOS'''
    p[0] = "while"

def p_for(p):
    '''for : FOR ID IN RANGE LPAREN NUMBER RPAREN DOSPUNTOS'''
    p[0] = "FOR"

def p_print(p):
    '''print : PRINT LPAREN factor RPAREN
             | PRINT LPAREN ID RPAREN'''
    p[0] = "PRINT"

def p_input(p):
    '''inputF : ID ASSIGN INPUT LPAREN RPAREN
              | INPUT LPAREN RPAREN'''
    p[0] = "INPUT"

def p_open(p):
    '''openF : OPEN LPAREN CADENA RPAREN
             | OPEN LPAREN CADENA COMA CADENA RPAREN
             | ID ASSIGN OPEN LPAREN CADENA COMA CADENA RPAREN'''
    p[0] = "OPEN"

def p_funcion(p):
    '''funcion : DEF ID LPAREN valoresComa RPAREN DOSPUNTOS'''
    p[0] = "FUNCION"



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
""" while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result) """
     