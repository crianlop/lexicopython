
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND APPEND ASSIGN BOOLEAN CADENA COMA COMILLAS COMILLASSIMPLES COMMENT COMMENTS CORCHETEDER CORCHETEIZQ DEF DIFERENTE DIVIDE DIVISIONENTERA DOSPUNTOS ELSE EQUALS EXPONENTE FLOAT FOR ID IF IN INPUT IS LESSTHAN LLAVEDER LLAVEIZQ LPAREN MAYORIGUAL MENORIGUAL MINUS MOD MORETHAN NONE NOT NOTS NUMBER OPEN OR PLUS PRINT PUNTO PUNTOCOMA RANGE REMOVE RETURN RPAREN STRING SUBGUION TIMES WHILEcuerpo : expression\n              | comentario\n              | asignacion\n              | if\n              | else\n              | while   \n              | for \n              | print  \n              | inputF\n              | openF \n              | funcion \n              | comparacion \n              | operacionConectoresLogicos  \n              | tupla\n              | lista\n              | diccionario\n              | conjunto\n              | return\n              | append\n              | remove\n              expression : expression PLUS termexpression : expression MINUS termexpression : termterm : term TIMES factorterm : term DIVIDE factorterm : term EXPONENTE factorterm : term DIVISIONENTERA factorterm : term MOD factorterm : factorfactor : NUMBER\n              | STRING\n              | FLOAT\n              | CADENA\n              | ID   \n              factor : LPAREN expression RPARENcomentario : COMMENT\n                 | COMMENTSasignacion : ID ASSIGN expression\n                  | multipleAsignacion expression\n                  | valoresID ASSIGN valoresComa\n                  | ID ASSIGN BOOLEANmultipleAsignacion : ID ASSIGN \n                          | ID ASSIGN multipleAsignacionvaloresID : ID\n                | valoresID COMA IDvaloresComa : expression\n                   | valoresComa COMA expression\n                   | valoresComa COMAvaloresDic  : factor DOSPUNTOS factor\n                   | valoresDic COMA factor DOSPUNTOS factor\n                   | valoresDic COMAdiccionario : LLAVEIZQ valoresDic LLAVEDER\n                | ID ASSIGN diccionariolista : CORCHETEIZQ valoresComa CORCHETEDER\n             | ID ASSIGN lista\n             | ID ASSIGN CORCHETEIZQ CORCHETEDERtupla : LPAREN valoresComa RPAREN\n             | ID ASSIGN tuplaconjunto : LLAVEIZQ valoresComa LLAVEDER\n                | ID ASSIGN conjuntocomparacion : ID operadorLogico expression\n                   | BOOLEAN\n                   | NOTS BOOLEAN\n                   | expression operadorLogico expression\n                   | comparacion operadorLogico ID\n                   | ID operadorLogico BOOLEANoperadorLogico : EQUALS\n                      | MAYORIGUAL\n                      | MENORIGUAL\n                      | LESSTHAN\n                      | MORETHAN\n                      | DIFERENTE\n    conectoresLogicos : AND\n                         | ORoperacionConectoresLogicos : NOT ID\n                                  | ID conectoresLogicos ID\n                                  | operacionConectoresLogicos conectoresLogicos IDif : IF LPAREN comparacion RPAREN DOSPUNTOS\n          | IF comparacion DOSPUNTOS\n          | IF ID DOSPUNTOSelse : ELSE DOSPUNTOSwhile : WHILE LPAREN comparacion RPAREN DOSPUNTOS\n             | WHILE comparacion DOSPUNTOS\n             | WHILE ID DOSPUNTOSfor : FOR ID IN RANGE LPAREN NUMBER RPAREN DOSPUNTOS\n           | FOR ID IN ID DOSPUNTOS\n           | FOR ID IN lista\n           | FOR ID IN tupla\n           | FOR ID IN conjuntoprint : PRINT LPAREN factor RPAREN\n             | PRINT LPAREN ID RPARENinputF : ID ASSIGN INPUT LPAREN RPAREN\n              | INPUT LPAREN RPARENopenF : OPEN LPAREN CADENA RPAREN\n             | OPEN LPAREN CADENA COMA CADENA RPAREN\n             | ID ASSIGN OPEN LPAREN CADENA COMA CADENA RPAREN\n             | ID ASSIGN OPEN LPAREN ID COMA CADENA RPARENfuncion : DEF ID LPAREN valoresID RPAREN DOSPUNTOSdatos : lista\n             | tupla\n             | conjunto\n             | diccionario\n    return : RETURN expression\n              | RETURN NONEappend : ID PUNTO APPEND LPAREN ID RPAREN\n              | ID PUNTO APPEND LPAREN expression RPAREN\n              | ID PUNTO APPEND LPAREN datos RPARENremove : ID PUNTO REMOVE LPAREN ID RPAREN\n              | ID PUNTO REMOVE LPAREN RPAREN\n              | ID PUNTO REMOVE LPAREN expression RPAREN'
    
_lr_action_items = {'COMMENT':([0,],[23,]),'COMMENTS':([0,],[24,]),'ID':([0,26,29,30,32,33,40,42,43,44,45,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,72,73,74,75,82,86,116,119,134,139,144,147,149,150,152,154,155,161,165,185,192,196,200,],[25,71,77,71,84,85,89,91,71,71,71,71,71,71,-67,-68,-69,-70,-71,-72,102,103,-73,-74,71,71,71,71,71,109,71,122,71,71,127,130,130,141,71,-43,71,159,170,71,71,174,176,178,186,71,71,71,205,71,212,]),'IF':([0,],[29,]),'ELSE':([0,],[31,]),'WHILE':([0,],[32,]),'FOR':([0,],[33,]),'PRINT':([0,],[35,]),'INPUT':([0,66,],[37,112,]),'OPEN':([0,66,],[38,113,]),'DEF':([0,],[40,]),'BOOLEAN':([0,29,32,41,51,52,53,54,55,56,66,67,75,82,],[28,28,28,90,-67,-68,-69,-70,-71,-72,111,121,28,28,]),'NOTS':([0,29,32,75,82,],[41,41,41,41,41,]),'NOT':([0,],[42,]),'LPAREN':([0,26,29,30,32,35,37,38,43,44,45,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,72,73,75,82,86,89,112,113,116,119,123,124,134,139,147,149,150,154,155,160,161,165,185,192,196,200,],[30,72,75,72,82,86,87,88,72,72,72,72,72,72,-67,-68,-69,-70,-71,-72,72,72,72,72,72,30,72,72,72,72,72,72,144,151,152,72,-43,154,155,72,161,72,72,161,30,72,193,72,72,72,161,72,161,]),'CORCHETEIZQ':([0,66,139,150,154,192,200,],[43,116,43,116,43,116,116,]),'LLAVEIZQ':([0,66,139,150,154,192,200,],[44,44,165,44,185,165,185,]),'RETURN':([0,],[45,]),'NUMBER':([0,26,29,30,32,43,44,45,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,72,73,75,82,86,116,119,134,147,149,150,154,155,161,165,185,193,196,],[34,34,34,34,34,34,34,34,34,34,34,-67,-68,-69,-70,-71,-72,34,34,34,34,34,34,34,34,34,34,34,34,34,-43,34,34,34,-42,34,34,34,34,34,206,34,]),'STRING':([0,26,29,30,32,43,44,45,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,72,73,75,82,86,116,119,134,147,149,150,154,155,161,165,185,196,],[46,46,46,46,46,46,46,46,46,46,46,-67,-68,-69,-70,-71,-72,46,46,46,46,46,46,46,46,46,46,46,46,46,-43,46,46,46,-42,46,46,46,46,46,46,]),'FLOAT':([0,26,29,30,32,43,44,45,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,72,73,75,82,86,116,119,134,147,149,150,154,155,161,165,185,196,],[47,47,47,47,47,47,47,47,47,47,47,-67,-68,-69,-70,-71,-72,47,47,47,47,47,47,47,47,47,47,47,47,47,-43,47,47,47,-42,47,47,47,47,47,47,]),'CADENA':([0,26,29,30,32,43,44,45,48,49,50,51,52,53,54,55,56,61,62,63,64,65,66,67,72,73,75,82,86,88,116,119,134,147,149,150,152,154,155,161,165,169,185,196,197,198,],[39,39,39,39,39,39,39,39,39,39,39,-67,-68,-69,-70,-71,-72,39,39,39,39,39,39,39,39,39,39,39,39,143,39,-43,39,39,39,-42,177,39,39,39,39,194,39,39,210,211,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,28,34,36,39,46,47,70,71,81,90,91,93,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,114,115,117,118,120,121,122,126,131,132,133,134,135,137,138,142,145,146,148,153,157,162,163,164,166,167,168,175,187,189,190,191,199,201,202,203,204,207,208,214,215,216,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-23,-36,-37,-34,-62,-30,-29,-33,-31,-32,-39,-34,-81,-63,-75,-46,-103,-104,-21,-22,-64,-65,-77,-24,-25,-26,-27,-28,-34,-38,-41,-58,-55,-53,-60,-61,-66,-76,-40,-79,-80,-57,-48,-35,-83,-84,-93,-54,-52,-59,-56,-47,-87,-88,-89,-90,-91,-94,-92,-109,-78,-82,-86,-105,-106,-107,-108,-110,-95,-98,-97,-96,-85,]),'PLUS':([2,22,25,34,36,39,46,47,70,71,77,78,80,84,93,96,97,99,100,101,104,105,106,107,108,109,110,120,125,129,130,135,157,178,179,186,188,],[48,-23,-34,-30,-29,-33,-31,-32,48,-34,-34,48,48,-34,48,-29,48,-21,-22,48,-24,-25,-26,-27,-28,-34,48,48,48,48,-34,-35,48,-34,48,-34,48,]),'MINUS':([2,22,25,34,36,39,46,47,70,71,77,78,80,84,93,96,97,99,100,101,104,105,106,107,108,109,110,120,125,129,130,135,157,178,179,186,188,],[49,-23,-34,-30,-29,-33,-31,-32,49,-34,-34,49,49,-34,49,-29,49,-21,-22,49,-24,-25,-26,-27,-28,-34,49,49,49,49,-34,-35,49,-34,49,-34,49,]),'EQUALS':([2,13,22,25,28,34,36,39,46,47,71,76,77,78,83,84,90,99,100,101,102,104,105,106,107,108,120,121,128,129,130,135,136,],[51,51,-23,51,-62,-30,-29,-33,-31,-32,-34,51,51,51,51,51,-63,-21,-22,-64,-65,-24,-25,-26,-27,-28,-61,-66,51,51,51,-35,51,]),'MAYORIGUAL':([2,13,22,25,28,34,36,39,46,47,71,76,77,78,83,84,90,99,100,101,102,104,105,106,107,108,120,121,128,129,130,135,136,],[52,52,-23,52,-62,-30,-29,-33,-31,-32,-34,52,52,52,52,52,-63,-21,-22,-64,-65,-24,-25,-26,-27,-28,-61,-66,52,52,52,-35,52,]),'MENORIGUAL':([2,13,22,25,28,34,36,39,46,47,71,76,77,78,83,84,90,99,100,101,102,104,105,106,107,108,120,121,128,129,130,135,136,],[53,53,-23,53,-62,-30,-29,-33,-31,-32,-34,53,53,53,53,53,-63,-21,-22,-64,-65,-24,-25,-26,-27,-28,-61,-66,53,53,53,-35,53,]),'LESSTHAN':([2,13,22,25,28,34,36,39,46,47,71,76,77,78,83,84,90,99,100,101,102,104,105,106,107,108,120,121,128,129,130,135,136,],[54,54,-23,54,-62,-30,-29,-33,-31,-32,-34,54,54,54,54,54,-63,-21,-22,-64,-65,-24,-25,-26,-27,-28,-61,-66,54,54,54,-35,54,]),'MORETHAN':([2,13,22,25,28,34,36,39,46,47,71,76,77,78,83,84,90,99,100,101,102,104,105,106,107,108,120,121,128,129,130,135,136,],[55,55,-23,55,-62,-30,-29,-33,-31,-32,-34,55,55,55,55,55,-63,-21,-22,-64,-65,-24,-25,-26,-27,-28,-61,-66,55,55,55,-35,55,]),'DIFERENTE':([2,13,22,25,28,34,36,39,46,47,71,76,77,78,83,84,90,99,100,101,102,104,105,106,107,108,120,121,128,129,130,135,136,],[56,56,-23,56,-62,-30,-29,-33,-31,-32,-34,56,56,56,56,56,-63,-21,-22,-64,-65,-24,-25,-26,-27,-28,-61,-66,56,56,56,-35,56,]),'AND':([14,25,91,103,122,],[59,59,-75,-77,-76,]),'OR':([14,25,91,103,122,],[60,60,-75,-77,-76,]),'RPAREN':([22,28,34,36,39,46,47,71,79,80,87,90,93,99,100,101,102,104,105,106,107,108,114,115,117,118,120,121,125,127,128,129,130,133,134,135,136,140,141,143,145,146,148,151,153,155,157,170,171,178,179,180,181,182,183,184,186,188,194,206,210,211,],[-23,-62,-30,-29,-33,-31,-32,-34,133,135,142,-63,-46,-21,-22,-64,-65,-24,-25,-26,-27,-28,-58,-55,-53,-60,-61,-66,135,-45,156,135,-34,-57,-48,-35,158,166,167,168,-54,-52,-59,175,-56,187,-47,-44,195,199,201,202,-99,-100,-101,-102,203,204,207,213,214,215,]),'COMA':([22,25,27,34,36,39,46,47,71,79,80,92,93,94,95,96,99,100,104,105,106,107,108,126,127,134,135,143,147,157,170,171,173,176,177,209,],[-23,-44,74,-30,-29,-33,-31,-32,-34,134,-46,134,-46,147,134,-29,-21,-22,-24,-25,-26,-27,-28,134,-45,-48,-35,169,-51,-47,-44,74,-49,197,198,-50,]),'CORCHETEDER':([22,34,36,39,46,47,71,92,93,99,100,104,105,106,107,108,116,134,135,157,],[-23,-30,-29,-33,-31,-32,-34,145,-46,-21,-22,-24,-25,-26,-27,-28,153,-48,-35,-47,]),'LLAVEDER':([22,34,36,39,46,47,71,93,94,95,96,99,100,104,105,106,107,108,134,135,147,157,173,209,],[-23,-30,-29,-33,-31,-32,-34,-46,146,148,-29,-21,-22,-24,-25,-26,-27,-28,-48,-35,-51,-47,-49,-50,]),'DOSPUNTOS':([22,28,31,34,36,39,46,47,71,76,77,83,84,90,96,99,100,101,102,104,105,106,107,108,120,121,135,156,158,159,172,195,213,],[-23,-62,81,-30,-29,-33,-31,-32,-34,131,132,137,138,-63,149,-21,-22,-64,-65,-24,-25,-26,-27,-28,-61,-66,-35,189,190,191,196,208,216,]),'TIMES':([22,25,34,36,39,46,47,71,77,84,96,99,100,104,105,106,107,108,109,130,135,178,186,],[61,-34,-30,-29,-33,-31,-32,-34,-34,-34,-29,61,61,-24,-25,-26,-27,-28,-34,-34,-35,-34,-34,]),'DIVIDE':([22,25,34,36,39,46,47,71,77,84,96,99,100,104,105,106,107,108,109,130,135,178,186,],[62,-34,-30,-29,-33,-31,-32,-34,-34,-34,-29,62,62,-24,-25,-26,-27,-28,-34,-34,-35,-34,-34,]),'EXPONENTE':([22,25,34,36,39,46,47,71,77,84,96,99,100,104,105,106,107,108,109,130,135,178,186,],[63,-34,-30,-29,-33,-31,-32,-34,-34,-34,-29,63,63,-24,-25,-26,-27,-28,-34,-34,-35,-34,-34,]),'DIVISIONENTERA':([22,25,34,36,39,46,47,71,77,84,96,99,100,104,105,106,107,108,109,130,135,178,186,],[64,-34,-30,-29,-33,-31,-32,-34,-34,-34,-29,64,64,-24,-25,-26,-27,-28,-34,-34,-35,-34,-34,]),'MOD':([22,25,34,36,39,46,47,71,77,84,96,99,100,104,105,106,107,108,109,130,135,178,186,],[65,-34,-30,-29,-33,-31,-32,-34,-34,-34,-29,65,65,-24,-25,-26,-27,-28,-34,-34,-35,-34,-34,]),'ASSIGN':([25,27,109,127,159,174,178,205,212,],[66,73,150,-45,192,150,200,192,200,]),'PUNTO':([25,],[69,]),'NONE':([45,],[98,]),'APPEND':([69,],[123,]),'REMOVE':([69,],[124,]),'IN':([85,],[139,]),'RANGE':([139,],[160,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cuerpo':([0,],[1,]),'expression':([0,26,29,30,32,43,44,45,50,66,67,72,73,75,82,116,134,154,155,161,165,185,],[2,70,78,80,78,93,93,97,101,110,120,125,93,129,129,93,157,179,188,93,93,93,]),'comentario':([0,],[3,]),'asignacion':([0,],[4,]),'if':([0,],[5,]),'else':([0,],[6,]),'while':([0,],[7,]),'for':([0,],[8,]),'print':([0,],[9,]),'inputF':([0,],[10,]),'openF':([0,],[11,]),'funcion':([0,],[12,]),'comparacion':([0,29,32,75,82,],[13,76,83,128,136,]),'operacionConectoresLogicos':([0,],[14,]),'tupla':([0,66,139,150,154,192,200,],[15,114,163,114,182,114,114,]),'lista':([0,66,139,150,154,192,200,],[16,115,162,115,181,115,115,]),'diccionario':([0,66,150,154,200,],[17,117,117,184,117,]),'conjunto':([0,66,139,150,154,192,200,],[18,118,164,118,183,118,118,]),'return':([0,],[19,]),'append':([0,],[20,]),'remove':([0,],[21,]),'term':([0,26,29,30,32,43,44,45,48,49,50,66,67,72,73,75,82,116,134,154,155,161,165,185,],[22,22,22,22,22,22,22,22,99,100,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'multipleAsignacion':([0,66,150,],[26,119,119,]),'valoresID':([0,144,],[27,171,]),'factor':([0,26,29,30,32,43,44,45,48,49,50,61,62,63,64,65,66,67,72,73,75,82,86,116,134,147,149,154,155,161,165,185,196,],[36,36,36,36,36,36,96,36,36,36,36,104,105,106,107,108,36,36,36,36,36,36,140,36,36,172,173,36,36,36,36,96,209,]),'operadorLogico':([2,13,25,76,77,78,83,84,128,129,130,136,],[50,57,67,57,67,50,57,67,57,50,67,57,]),'conectoresLogicos':([14,25,],[58,68,]),'valoresComa':([30,43,44,73,116,161,165,185,],[79,92,95,126,92,79,95,95,]),'valoresDic':([44,185,],[94,94,]),'datos':([154,],[180,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> cuerpo","S'",1,None,None,None),
  ('cuerpo -> expression','cuerpo',1,'p_cuerpo','sintatico.py',6),
  ('cuerpo -> comentario','cuerpo',1,'p_cuerpo','sintatico.py',7),
  ('cuerpo -> asignacion','cuerpo',1,'p_cuerpo','sintatico.py',8),
  ('cuerpo -> if','cuerpo',1,'p_cuerpo','sintatico.py',9),
  ('cuerpo -> else','cuerpo',1,'p_cuerpo','sintatico.py',10),
  ('cuerpo -> while','cuerpo',1,'p_cuerpo','sintatico.py',11),
  ('cuerpo -> for','cuerpo',1,'p_cuerpo','sintatico.py',12),
  ('cuerpo -> print','cuerpo',1,'p_cuerpo','sintatico.py',13),
  ('cuerpo -> inputF','cuerpo',1,'p_cuerpo','sintatico.py',14),
  ('cuerpo -> openF','cuerpo',1,'p_cuerpo','sintatico.py',15),
  ('cuerpo -> funcion','cuerpo',1,'p_cuerpo','sintatico.py',16),
  ('cuerpo -> comparacion','cuerpo',1,'p_cuerpo','sintatico.py',17),
  ('cuerpo -> operacionConectoresLogicos','cuerpo',1,'p_cuerpo','sintatico.py',18),
  ('cuerpo -> tupla','cuerpo',1,'p_cuerpo','sintatico.py',19),
  ('cuerpo -> lista','cuerpo',1,'p_cuerpo','sintatico.py',20),
  ('cuerpo -> diccionario','cuerpo',1,'p_cuerpo','sintatico.py',21),
  ('cuerpo -> conjunto','cuerpo',1,'p_cuerpo','sintatico.py',22),
  ('cuerpo -> return','cuerpo',1,'p_cuerpo','sintatico.py',23),
  ('cuerpo -> append','cuerpo',1,'p_cuerpo','sintatico.py',24),
  ('cuerpo -> remove','cuerpo',1,'p_cuerpo','sintatico.py',25),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','sintatico.py',30),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','sintatico.py',35),
  ('expression -> term','expression',1,'p_expression_term','sintatico.py',40),
  ('term -> term TIMES factor','term',3,'p_term_times','sintatico.py',44),
  ('term -> term DIVIDE factor','term',3,'p_term_div','sintatico.py',49),
  ('term -> term EXPONENTE factor','term',3,'p_term_cuadrado','sintatico.py',54),
  ('term -> term DIVISIONENTERA factor','term',3,'p_term_divEntera','sintatico.py',59),
  ('term -> term MOD factor','term',3,'p_term_Mod','sintatico.py',64),
  ('term -> factor','term',1,'p_term_factor','sintatico.py',69),
  ('factor -> NUMBER','factor',1,'p_factor_num','sintatico.py',73),
  ('factor -> STRING','factor',1,'p_factor_num','sintatico.py',74),
  ('factor -> FLOAT','factor',1,'p_factor_num','sintatico.py',75),
  ('factor -> CADENA','factor',1,'p_factor_num','sintatico.py',76),
  ('factor -> ID','factor',1,'p_factor_num','sintatico.py',77),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','sintatico.py',82),
  ('comentario -> COMMENT','comentario',1,'p_comentario','sintatico.py',86),
  ('comentario -> COMMENTS','comentario',1,'p_comentario','sintatico.py',87),
  ('asignacion -> ID ASSIGN expression','asignacion',3,'p_asignacion','sintatico.py',91),
  ('asignacion -> multipleAsignacion expression','asignacion',2,'p_asignacion','sintatico.py',92),
  ('asignacion -> valoresID ASSIGN valoresComa','asignacion',3,'p_asignacion','sintatico.py',93),
  ('asignacion -> ID ASSIGN BOOLEAN','asignacion',3,'p_asignacion','sintatico.py',94),
  ('multipleAsignacion -> ID ASSIGN','multipleAsignacion',2,'p_multipleAsignacion','sintatico.py',98),
  ('multipleAsignacion -> ID ASSIGN multipleAsignacion','multipleAsignacion',3,'p_multipleAsignacion','sintatico.py',99),
  ('valoresID -> ID','valoresID',1,'p_valoresID','sintatico.py',102),
  ('valoresID -> valoresID COMA ID','valoresID',3,'p_valoresID','sintatico.py',103),
  ('valoresComa -> expression','valoresComa',1,'p_valoresComa','sintatico.py',106),
  ('valoresComa -> valoresComa COMA expression','valoresComa',3,'p_valoresComa','sintatico.py',107),
  ('valoresComa -> valoresComa COMA','valoresComa',2,'p_valoresComa','sintatico.py',108),
  ('valoresDic -> factor DOSPUNTOS factor','valoresDic',3,'p_valoresDic','sintatico.py',112),
  ('valoresDic -> valoresDic COMA factor DOSPUNTOS factor','valoresDic',5,'p_valoresDic','sintatico.py',113),
  ('valoresDic -> valoresDic COMA','valoresDic',2,'p_valoresDic','sintatico.py',114),
  ('diccionario -> LLAVEIZQ valoresDic LLAVEDER','diccionario',3,'p_diccionario','sintatico.py',118),
  ('diccionario -> ID ASSIGN diccionario','diccionario',3,'p_diccionario','sintatico.py',119),
  ('lista -> CORCHETEIZQ valoresComa CORCHETEDER','lista',3,'p_lista','sintatico.py',123),
  ('lista -> ID ASSIGN lista','lista',3,'p_lista','sintatico.py',124),
  ('lista -> ID ASSIGN CORCHETEIZQ CORCHETEDER','lista',4,'p_lista','sintatico.py',125),
  ('tupla -> LPAREN valoresComa RPAREN','tupla',3,'p_tupla','sintatico.py',129),
  ('tupla -> ID ASSIGN tupla','tupla',3,'p_tupla','sintatico.py',130),
  ('conjunto -> LLAVEIZQ valoresComa LLAVEDER','conjunto',3,'p_conjunto','sintatico.py',134),
  ('conjunto -> ID ASSIGN conjunto','conjunto',3,'p_conjunto','sintatico.py',135),
  ('comparacion -> ID operadorLogico expression','comparacion',3,'p_comparacion','sintatico.py',139),
  ('comparacion -> BOOLEAN','comparacion',1,'p_comparacion','sintatico.py',140),
  ('comparacion -> NOTS BOOLEAN','comparacion',2,'p_comparacion','sintatico.py',141),
  ('comparacion -> expression operadorLogico expression','comparacion',3,'p_comparacion','sintatico.py',142),
  ('comparacion -> comparacion operadorLogico ID','comparacion',3,'p_comparacion','sintatico.py',143),
  ('comparacion -> ID operadorLogico BOOLEAN','comparacion',3,'p_comparacion','sintatico.py',144),
  ('operadorLogico -> EQUALS','operadorLogico',1,'p_operadorLogico','sintatico.py',148),
  ('operadorLogico -> MAYORIGUAL','operadorLogico',1,'p_operadorLogico','sintatico.py',149),
  ('operadorLogico -> MENORIGUAL','operadorLogico',1,'p_operadorLogico','sintatico.py',150),
  ('operadorLogico -> LESSTHAN','operadorLogico',1,'p_operadorLogico','sintatico.py',151),
  ('operadorLogico -> MORETHAN','operadorLogico',1,'p_operadorLogico','sintatico.py',152),
  ('operadorLogico -> DIFERENTE','operadorLogico',1,'p_operadorLogico','sintatico.py',153),
  ('conectoresLogicos -> AND','conectoresLogicos',1,'p_conectoresLogicos','sintatico.py',157),
  ('conectoresLogicos -> OR','conectoresLogicos',1,'p_conectoresLogicos','sintatico.py',158),
  ('operacionConectoresLogicos -> NOT ID','operacionConectoresLogicos',2,'p_operacionConectoresLogicos','sintatico.py',161),
  ('operacionConectoresLogicos -> ID conectoresLogicos ID','operacionConectoresLogicos',3,'p_operacionConectoresLogicos','sintatico.py',162),
  ('operacionConectoresLogicos -> operacionConectoresLogicos conectoresLogicos ID','operacionConectoresLogicos',3,'p_operacionConectoresLogicos','sintatico.py',163),
  ('if -> IF LPAREN comparacion RPAREN DOSPUNTOS','if',5,'p_if','sintatico.py',167),
  ('if -> IF comparacion DOSPUNTOS','if',3,'p_if','sintatico.py',168),
  ('if -> IF ID DOSPUNTOS','if',3,'p_if','sintatico.py',169),
  ('else -> ELSE DOSPUNTOS','else',2,'p_else','sintatico.py',173),
  ('while -> WHILE LPAREN comparacion RPAREN DOSPUNTOS','while',5,'p_while','sintatico.py',177),
  ('while -> WHILE comparacion DOSPUNTOS','while',3,'p_while','sintatico.py',178),
  ('while -> WHILE ID DOSPUNTOS','while',3,'p_while','sintatico.py',179),
  ('for -> FOR ID IN RANGE LPAREN NUMBER RPAREN DOSPUNTOS','for',8,'p_for','sintatico.py',183),
  ('for -> FOR ID IN ID DOSPUNTOS','for',5,'p_for','sintatico.py',184),
  ('for -> FOR ID IN lista','for',4,'p_for','sintatico.py',185),
  ('for -> FOR ID IN tupla','for',4,'p_for','sintatico.py',186),
  ('for -> FOR ID IN conjunto','for',4,'p_for','sintatico.py',187),
  ('print -> PRINT LPAREN factor RPAREN','print',4,'p_print','sintatico.py',191),
  ('print -> PRINT LPAREN ID RPAREN','print',4,'p_print','sintatico.py',192),
  ('inputF -> ID ASSIGN INPUT LPAREN RPAREN','inputF',5,'p_input','sintatico.py',196),
  ('inputF -> INPUT LPAREN RPAREN','inputF',3,'p_input','sintatico.py',197),
  ('openF -> OPEN LPAREN CADENA RPAREN','openF',4,'p_open','sintatico.py',201),
  ('openF -> OPEN LPAREN CADENA COMA CADENA RPAREN','openF',6,'p_open','sintatico.py',202),
  ('openF -> ID ASSIGN OPEN LPAREN CADENA COMA CADENA RPAREN','openF',8,'p_open','sintatico.py',203),
  ('openF -> ID ASSIGN OPEN LPAREN ID COMA CADENA RPAREN','openF',8,'p_open','sintatico.py',204),
  ('funcion -> DEF ID LPAREN valoresID RPAREN DOSPUNTOS','funcion',6,'p_funcion','sintatico.py',208),
  ('datos -> lista','datos',1,'p_estructuraDatos','sintatico.py',212),
  ('datos -> tupla','datos',1,'p_estructuraDatos','sintatico.py',213),
  ('datos -> conjunto','datos',1,'p_estructuraDatos','sintatico.py',214),
  ('datos -> diccionario','datos',1,'p_estructuraDatos','sintatico.py',215),
  ('return -> RETURN expression','return',2,'p_return','sintatico.py',218),
  ('return -> RETURN NONE','return',2,'p_return','sintatico.py',219),
  ('append -> ID PUNTO APPEND LPAREN ID RPAREN','append',6,'p_append','sintatico.py',223),
  ('append -> ID PUNTO APPEND LPAREN expression RPAREN','append',6,'p_append','sintatico.py',224),
  ('append -> ID PUNTO APPEND LPAREN datos RPAREN','append',6,'p_append','sintatico.py',225),
  ('remove -> ID PUNTO REMOVE LPAREN ID RPAREN','remove',6,'p_remove','sintatico.py',229),
  ('remove -> ID PUNTO REMOVE LPAREN RPAREN','remove',5,'p_remove','sintatico.py',230),
  ('remove -> ID PUNTO REMOVE LPAREN expression RPAREN','remove',6,'p_remove','sintatico.py',231),
]
