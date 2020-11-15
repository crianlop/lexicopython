# GRUPO PYTHON
import ply
import ply.lex as lex
import ply.yacc as yacc



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
    "False" : "FALSE"
}
tokens = ("ID","EQUALS","ASSIGN","NUMBER",
          "PLUS","MINUS","TIMES","DIVIDE",
          "NOT","LESSTHAN","MORETHAN","LPAREN","RPAREN","COLON","WHILE","IF","ELSE"
          ,"AND","IS","FOR","TRUE","FALSE")
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'\=='
t_ASSIGN = r'\='
t_NOT = r'\!'
t_LESSTHAN = r'\<'
t_MORETHAN = r'\>'
t_COLON = r':'


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
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)