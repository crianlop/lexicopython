from ply.lex import lex
import ply.yacc as yacc
import os
from lexicoPython import tokens
from lexicoPython import *

ban = True

mensaje = ""

def p_cuerpo(p):
    '''cuerpo : cuerpoEstructura
              | cuerpo cuerpoEstructura
                        '''
    p[0] = p[1]

def p_cuerpoEstructura(p):
    ''' cuerpoEstructura : import  
            | expression 
            | comentario 
            | asignacion
            | if 
            | while 
            | for  
            | print 
            | inputF 
            | openF 
            | funcion 
            | comparacion 
            | operacionConectoresLogicos  
            | tupla 
            | lista 
            | diccionario 
            | conjunto 
            | append 
            | remove'''
    p[0] = p[1]


def p_expression_plus(p):
    'expression : expression PLUS term'
    if type(p[1]) == int and type(p[3]) == int:
        p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    if type(p[1]) == int and type(p[3]) == int:
        p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    if type(p[1]) == int and type(p[3]) == int:
        p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    if type(p[1]) == int and type(p[3]) == int:
        p[0] = p[1] / p[3]

def p_term_cuadrado(p):
    'term : term EXPONENTE factor'
    if type(p[1]) == int and type(p[3]) == int:
        p[0] = p[1] ** p[3]

def p_term_divEntera(p):
    'term : term DIVISIONENTERA factor'
    if type(p[1]) == int and type(p[3]) == int:
        p[0] = p[1] // p[3]

def p_term_Mod(p):
    'term : term MOD factor'
    if type(p[1]) == int and type(p[3]) == int:
        p[0] = p[1] % p[3]

def p_term_factor(p):
    '''term : factor'''
    p[0] = p[1]

def p_factor_num(p):
    '''factor : NUMBER
              | STRING
              | FLOAT
              | CADENA
              | ID   
              '''
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
                  | valoresID ASSIGN valoresComa
                  | ID ASSIGN BOOLEAN
                  | ID ASSIGN funcion'''
    p[0] = "ASIGNACION"

def p_multipleAsignacion(p):
    '''multipleAsignacion : ID ASSIGN 
                          | ID ASSIGN multipleAsignacion'''

def p_valoresID(p):
    '''valoresID : ID
                | valoresID COMA ID'''

def p_valoresComa(p):
    '''valoresComa : expression
                   | valoresComa COMA expression
                   | valoresComa COMA'''
    p[0] = "COMAS"

def p_valoresDic(p):
    '''valoresDic  : factor DOSPUNTOS factor
                   | valoresDic COMA factor DOSPUNTOS factor
                   | valoresDic COMA'''
    p[0] = "valoresDic"
    
def p_diccionario(p):
    '''diccionario : LLAVEIZQ valoresDic LLAVEDER
                | LLAVEIZQ LLAVEDER
                | ID ASSIGN diccionario'''
    p[0] = "DICCIONARIO"

def p_lista(p):
    '''lista : CORCHETEIZQ valoresComa CORCHETEDER
             | ID ASSIGN CORCHETEIZQ valoresComa CORCHETEDER
             | ID ASSIGN CORCHETEIZQ CORCHETEDER'''
    p[0] = "LISTA"

def p_tupla(p):
    '''tupla : LPAREN valoresComa RPAREN
             | ID ASSIGN tupla'''
    p[0] = "TUPLA"

def p_conjunto(p):
    '''conjunto : LLAVEIZQ valoresComa LLAVEDER
                | ID ASSIGN conjunto'''
    p[0] = "CONJUNTO"

def p_comparacion(p):
    '''comparacion : ID operadorLogico expression
    | ID operadorLogico CADENA
                   | BOOLEAN
                   | comparacion conectoresLogicos ID
                   | NOTS BOOLEAN
                   | expression operadorLogico expression
                   | comparacion operadorLogico ID
                   | ID operadorLogico BOOLEAN
                   | comparacion conectoresLogicos comparacion
                   | BOOLEAN EQUALS BOOLEAN
                   | BOOLEAN DIFERENTE BOOLEAN
                   
                   '''
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
    '''operacionConectoresLogicos : NOT ID
                                  | ID conectoresLogicos ID
                                  | operacionConectoresLogicos conectoresLogicos ID'''
    p[0] = "OPERACION CON CONECTORES LOGICOS"

def p_if(p):
    '''if : IF LPAREN comparacion RPAREN DOSPUNTOS cuerpo
          | IF comparacion DOSPUNTOS cuerpo
          | IF ID DOSPUNTOS cuerpo
          | IF LPAREN ID RPAREN DOSPUNTOS cuerpo
          | if else
        '''
    p[0] = "IF"

def p_else(p):
    '''else : ELSE DOSPUNTOS cuerpo'''
    p[0] = "ELSE"

def p_while(p):
    '''while : WHILE LPAREN comparacion RPAREN DOSPUNTOS 
             | WHILE comparacion DOSPUNTOS 
             | WHILE ID DOSPUNTOS '''
    p[0] = "while"

def p_for(p):
    '''for : FOR ID IN RANGE LPAREN NUMBER RPAREN DOSPUNTOS cuerpo
           | FOR ID IN ID DOSPUNTOS cuerpo
           | FOR ID IN lista DOSPUNTOS 
           | FOR ID IN tupla DOSPUNTOS 
           | FOR ID IN conjunto DOSPUNTOS  '''
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
             | ID ASSIGN OPEN LPAREN CADENA COMA CADENA RPAREN
             | ID ASSIGN OPEN LPAREN ID COMA CADENA RPAREN'''
    p[0] = "OPEN"

def p_funcion(p):
    '''funcion : DEF ID LPAREN valoresID RPAREN DOSPUNTOS cuerpo
                | DEF ID LPAREN RPAREN DOSPUNTOS cuerpo
                | DEF ID LPAREN valoresID RPAREN DOSPUNTOS cuerpo return
                | DEF ID LPAREN RPAREN DOSPUNTOS cuerpo return
                | ID LPAREN RPAREN
                | ID LPAREN valoresID RPAREN'''
    p[0] = "FUNCION"

def p_estructuraDatos(p):
    '''datos : lista
             | tupla
             | conjunto
             | diccionario
    '''
def p_return(p):
    '''return : RETURN expression
              | RETURN NONE'''
    p[0] = "RETURN"

def p_append(p):
    '''append : ID PUNTO APPEND LPAREN ID RPAREN
              | ID PUNTO APPEND LPAREN expression RPAREN
              | ID PUNTO APPEND LPAREN datos RPAREN'''
    p[0] = "APPEND"

def p_remove(p):
    '''remove : ID PUNTO REMOVE LPAREN ID RPAREN
              | ID PUNTO REMOVE LPAREN RPAREN
              | ID PUNTO REMOVE LPAREN expression RPAREN'''
    p[0] = "REMOVE"
def p_import(p):
    '''import : IMPORT ID
              | IMPORT ID AS ID'''
    p[0] = "IMPORT"


# Error rule for syntax errors
def p_error(p):
    global ban
    global mensaje
    # global mensaje2
    if p:
        print("Error de sintaxis en esta línea: ", "token tipo: ",p.type," Valor: "+str(p.value))
        mensaje += "-Error de sintaxis\n -En esta línea: "+ str(p.lineno)+"\n -token tipo: " + str(p.type) + " -Valor :"+str(p.value)+ "\n"
        ban = False
    else:
        mensaje = "Error en la última línea"
        ban = False


# Construir parser

def sintacticoS(entrada):
    lexer.lineno = 1
    lexer.lexpos = 0
    global ban
    global mensaje
    parser = yacc.yacc()
    result = parser.parse(entrada)
    if (not ban):
        listaErrores = []
        listaErrores.append(mensaje)
        ban = True
        print(listaErrores)
        mensaje = ""
        return listaErrores
    else:
        listaErrores = []
        ban = True
        mensaje = ""
        return listaErrores

sintaxis = yacc.yacc()

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'codigoPrueba.py')
archivo = open(my_file,'r',encoding="utf-8")

cadena = '''
x = 7
aveces = xo = 4
'''

#print(sintacticoS(archivo.read()))


