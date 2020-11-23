import ply.yacc as yacc
import os
from lexicoPython import tokens

def p_cuerpo(p):
    '''cuerpo : expression
              | comentario
              | asignacion
              | list
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
            | STRING'''
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_comentario(p):
    '''comentario : COMMENT
                 | COMMENTS'''
    p[0] = "COMENTARIO"

def p_boolean(p):
    '''boolean : TRUE
    | FALSE'''
    p[0] = p[1]





def p_asignacion(p):
    '''asignacion : ID ASSIGN expression
                  | multipleAsignacion expression
                  | ID ASSIGN boolean'''
    p[0] = "ASIGNACION"

def p_multipleAsignacion(p):
    '''multipleAsignacion : ID ASSIGN 
                          | ID ASSIGN multipleAsignacion 
                          | ID ASSIGN "(" COMA ID ASSIGN ")" "*" expression'''

def p_list1(p):
    'list :  factor '
    p[0] = [p[1]]
def p_list2(p):
    '''list : list COMA factor'''
    p[0] = p[1] + [p[3]]


    
    


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
     