
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND APPEND AS ASSIGN BOOLEAN CADENA COMA COMILLAS COMILLASSIMPLES COMMENT COMMENTS CORCHETEDER CORCHETEIZQ DEF DIFERENTE DIVIDE DIVISIONENTERA DOSPUNTOS ELSE EQUALS EXPONENTE FLOAT FOR ID IF IMPORT IN INPUT IS LESSTHAN LLAVEDER LLAVEIZQ LPAREN MAYORIGUAL MENORIGUAL MINUS MOD MORETHAN NONE NOT NOTS NUMBER OPEN OR PLUS PRINT PUNTO PUNTOCOMA RANGE REMOVE RETURN RPAREN SALTOLINEA STRING SUBGUION TIMES WHILEcuerpo : import\n              | funcionDeclaracion\n              | cuerpoEstructuracuerpoEstructura :  expression\n                        | comentario\n                        | asignacion\n                        | if\n                        | while   \n                        | for \n                        | print  \n                        | funcion\n                        | inputF\n                        | openF \n                        | comparacion \n                        | operacionConectoresLogicos  \n                        | tupla\n                        | lista\n                        | diccionario\n                        | conjunto\n                        | append\n                        | removeexpression : expression PLUS termexpression : expression MINUS termexpression : termterm : term TIMES factorterm : term DIVIDE factorterm : term EXPONENTE factorterm : term DIVISIONENTERA factorterm : term MOD factorterm : factorfactor : NUMBER\n              | STRING\n              | FLOAT\n              | CADENA\n              | ID   \n              factor : LPAREN expression RPARENcomentario : COMMENT\n                 | COMMENTSasignacion : ID ASSIGN expression\n                  | multipleAsignacion expression\n                  | valoresID ASSIGN valoresComa\n                  | ID ASSIGN BOOLEAN\n                  | ID ASSIGN funcionmultipleAsignacion : ID ASSIGN \n                          | ID ASSIGN multipleAsignacionvaloresID : ID\n                | valoresID COMA IDvaloresComa : expression\n                   | valoresComa COMA expression\n                   | valoresComa COMAvaloresDic  : factor DOSPUNTOS factor\n                   | valoresDic COMA factor DOSPUNTOS factor\n                   | valoresDic COMAdiccionario : LLAVEIZQ valoresDic LLAVEDER\n                | LLAVEIZQ LLAVEDER\n                | ID ASSIGN diccionariolista : CORCHETEIZQ valoresComa CORCHETEDER\n             | ID ASSIGN lista\n             | ID ASSIGN CORCHETEIZQ CORCHETEDERtupla : LPAREN valoresComa RPAREN\n             | ID ASSIGN tuplaconjunto : LLAVEIZQ valoresComa LLAVEDER\n                | ID ASSIGN conjuntocomparacion : ID operadorLogico expression\n                   | BOOLEAN\n                   | comparacion conectoresLogicos ID\n                   | NOTS BOOLEAN\n                   | expression operadorLogico expression\n                   | comparacion operadorLogico ID\n                   | ID operadorLogico BOOLEAN\n                   | comparacion conectoresLogicos comparacion\n                   | BOOLEAN EQUALS BOOLEAN\n                   | BOOLEAN DIFERENTE BOOLEAN\n                   | factor operadorLogico factor\n                   \n                   operadorLogico : EQUALS\n                      | MAYORIGUAL\n                      | MENORIGUAL\n                      | LESSTHAN\n                      | MORETHAN\n                      | DIFERENTE\n    conectoresLogicos : AND\n                         | ORoperacionConectoresLogicos : NOT ID\n                                  | ID conectoresLogicos ID\n                                  | operacionConectoresLogicos conectoresLogicos IDif : IF LPAREN comparacion RPAREN DOSPUNTOS cuerpoEstructura ELSE DOSPUNTOS cuerpoEstructura\n          | IF LPAREN comparacion RPAREN DOSPUNTOS cuerpoEstructura\n          | IF LPAREN ID RPAREN DOSPUNTOS cuerpoEstructura ELSE DOSPUNTOS cuerpoEstructura\n          | IF LPAREN ID RPAREN DOSPUNTOS cuerpoEstructura\n          | IF ID DOSPUNTOS cuerpoEstructura ELSE DOSPUNTOS cuerpoEstructura\n          | IF ID DOSPUNTOS cuerpoEstructurawhile : WHILE LPAREN comparacion RPAREN DOSPUNTOS cuerpoEstructura\n             | WHILE LPAREN ID RPAREN DOSPUNTOS cuerpoEstructura\n             | WHILE ID DOSPUNTOS cuerpoEstructuradentroFor : NUMBER\n                 | NUMBER COMA NUMBER\n                 | NUMBER COMA NUMBER COMA NUMBERfor : FOR ID IN RANGE LPAREN dentroFor RPAREN DOSPUNTOS cuerpoEstructura\n           | FOR ID IN ID DOSPUNTOS cuerpoEstructura\n           | FOR ID IN lista DOSPUNTOS cuerpoEstructura\n           | FOR ID IN tupla DOSPUNTOS cuerpoEstructura\n           | FOR ID IN conjunto DOSPUNTOS cuerpoEstructuraprint : PRINT LPAREN factor RPAREN\n             | PRINT LPAREN ID RPARENinputF : ID ASSIGN INPUT LPAREN RPAREN\n              | INPUT LPAREN RPARENopenF : OPEN LPAREN CADENA RPAREN\n             | OPEN LPAREN CADENA COMA CADENA RPAREN\n             | ID ASSIGN OPEN LPAREN CADENA COMA CADENA RPAREN\n             | ID ASSIGN OPEN LPAREN ID COMA CADENA RPARENparametros : ID\n                  | expression\n                  | parametros COMA ID\n                  | parametros COMA expressionfuncionDeclaracion :  DEF ID LPAREN parametros RPAREN DOSPUNTOS cuerpoEstructura RETURN parametros\n                           | DEF ID LPAREN RPAREN DOSPUNTOS cuerpoEstructura RETURN parametros\n                           | DEF ID LPAREN RPAREN DOSPUNTOS cuerpoEstructura\n                           | DEF ID LPAREN parametros RPAREN DOSPUNTOS cuerpoEstructurafuncion :  ID LPAREN RPAREN\n               | ID LPAREN parametros RPARENdatos : lista\n             | tupla\n             | conjunto\n             | diccionario\n    return : RETURN expression\n              | RETURN NONEappend : ID PUNTO APPEND LPAREN ID RPAREN\n              | ID PUNTO APPEND LPAREN expression RPAREN\n              | ID PUNTO APPEND LPAREN datos RPARENremove : ID PUNTO REMOVE LPAREN ID RPAREN\n              | ID PUNTO REMOVE LPAREN RPAREN\n              | ID PUNTO REMOVE LPAREN expression RPARENimport : IMPORT ID\n              | IMPORT ID AS ID'
    
_lr_action_items = {'IMPORT':([0,],[5,]),'DEF':([0,],[7,]),'COMMENT':([0,147,150,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'COMMENTS':([0,147,150,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'ID':([0,5,7,8,30,33,34,35,42,43,44,49,50,51,52,54,55,56,57,58,59,60,61,63,68,69,70,71,72,73,74,75,76,77,78,80,81,84,86,89,90,101,110,113,123,126,147,150,151,159,161,163,165,168,169,170,182,186,206,211,212,213,215,216,217,218,220,221,222,224,228,233,237,253,261,263,264,265,],[6,48,62,67,67,85,87,88,94,67,67,102,114,67,120,-75,-76,-77,-78,-79,-80,-81,-82,67,67,67,67,132,134,135,67,67,67,67,67,67,142,146,149,153,67,162,67,-45,114,67,6,6,180,67,67,193,195,197,199,207,67,67,67,6,6,6,6,6,6,241,6,6,6,67,251,6,6,114,114,6,6,6,]),'IF':([0,147,150,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'WHILE':([0,147,150,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'FOR':([0,147,150,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'PRINT':([0,147,150,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'INPUT':([0,49,147,150,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[38,106,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'OPEN':([0,49,147,150,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[39,107,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'BOOLEAN':([0,41,49,51,54,55,56,57,58,59,60,61,71,82,83,84,86,147,150,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[32,93,104,119,-75,-76,-77,-78,-79,-80,-81,-82,32,143,144,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'NOTS':([0,60,61,71,84,86,147,150,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[41,-81,-82,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'NOT':([0,147,150,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'LPAREN':([0,6,8,30,33,34,36,38,39,43,44,49,50,51,54,55,56,57,58,59,60,61,62,63,68,69,70,71,74,75,76,77,78,80,84,86,89,90,102,106,107,110,113,121,122,123,126,147,150,151,159,161,163,168,169,170,181,182,186,206,211,212,213,215,216,217,218,220,221,222,224,228,233,237,253,261,263,264,265,],[8,50,63,63,84,86,89,91,92,63,63,8,63,63,-75,-76,-77,-78,-79,-80,-81,-82,123,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,50,164,165,63,-45,169,170,63,63,8,8,182,63,63,182,63,8,63,219,63,63,63,8,8,8,8,8,8,182,8,8,8,63,182,8,8,63,63,8,8,8,]),'CORCHETEIZQ':([0,49,147,150,151,163,169,211,212,213,215,216,217,218,220,221,222,228,233,237,263,264,265,],[43,110,43,43,43,110,43,43,43,43,43,43,43,110,43,43,43,110,43,43,43,43,43,]),'LLAVEIZQ':([0,49,147,150,151,163,169,211,212,213,215,216,217,218,220,221,222,228,233,237,263,264,265,],[44,44,44,44,186,44,206,44,44,44,44,44,44,186,44,44,44,206,44,44,44,44,44,]),'NUMBER':([0,8,30,43,44,49,50,51,54,55,56,57,58,59,60,61,63,68,69,70,71,74,75,76,77,78,80,84,86,89,90,110,113,123,126,147,150,159,161,163,168,169,170,182,186,206,211,212,213,215,216,217,219,220,221,222,224,233,237,253,258,261,263,264,265,271,],[45,45,45,45,45,45,45,45,-75,-76,-77,-78,-79,-80,-81,-82,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-45,45,45,45,45,45,45,-44,45,45,45,45,45,45,45,45,45,45,45,45,243,45,45,45,45,45,45,45,266,45,45,45,45,272,]),'STRING':([0,8,30,43,44,49,50,51,54,55,56,57,58,59,60,61,63,68,69,70,71,74,75,76,77,78,80,84,86,89,90,110,113,123,126,147,150,159,161,163,168,169,170,182,186,206,211,212,213,215,216,217,220,221,222,224,233,237,253,261,263,264,265,],[46,46,46,46,46,46,46,46,-75,-76,-77,-78,-79,-80,-81,-82,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-45,46,46,46,46,46,46,-44,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'FLOAT':([0,8,30,43,44,49,50,51,54,55,56,57,58,59,60,61,63,68,69,70,71,74,75,76,77,78,80,84,86,89,90,110,113,123,126,147,150,159,161,163,168,169,170,182,186,206,211,212,213,215,216,217,220,221,222,224,233,237,253,261,263,264,265,],[47,47,47,47,47,47,47,47,-75,-76,-77,-78,-79,-80,-81,-82,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-45,47,47,47,47,47,47,-44,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'CADENA':([0,8,30,43,44,49,50,51,54,55,56,57,58,59,60,61,63,68,69,70,71,74,75,76,77,78,80,84,86,89,90,92,110,113,123,126,147,150,159,161,163,165,168,169,170,182,186,190,206,211,212,213,215,216,217,220,221,222,224,225,226,233,237,253,261,263,264,265,],[40,40,40,40,40,40,40,40,-75,-76,-77,-78,-79,-80,-81,-82,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,156,40,-45,40,40,40,40,40,40,-44,196,40,40,40,40,40,223,40,40,40,40,40,40,40,40,40,40,40,249,250,40,40,40,40,40,40,40,]),'$end':([1,2,3,4,6,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,32,37,40,45,46,47,48,66,67,79,93,94,96,98,102,103,104,105,108,109,111,112,114,115,117,118,119,120,125,126,127,128,129,130,131,132,134,135,136,137,138,139,140,141,143,144,154,155,157,158,160,162,166,167,173,176,179,187,188,189,194,197,198,208,227,229,230,231,232,234,235,236,238,239,240,244,245,246,247,252,256,259,260,262,267,268,269,270,],[0,-1,-2,-3,-35,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-24,-37,-38,-65,-30,-34,-31,-32,-33,-133,-30,-35,-40,-67,-83,-48,-55,-35,-39,-42,-43,-61,-58,-56,-63,-35,-119,-112,-64,-70,-84,-60,-50,-36,-22,-23,-68,-71,-66,-69,-85,-25,-26,-27,-28,-29,-41,-72,-73,-74,-106,-57,-54,-62,-134,-59,-120,-49,-91,-94,-103,-104,-107,-105,-35,-114,-131,-127,-128,-129,-130,-132,-117,-87,-89,-92,-93,-99,-100,-101,-102,-108,-118,-90,-110,-109,-116,-115,-86,-88,-98,]),'ASSIGN':([6,31,102,142,180,193,199,241,251,],[49,80,163,-47,218,163,228,218,228,]),'PUNTO':([6,],[53,]),'COMA':([6,27,31,40,45,46,47,64,65,66,67,95,96,97,99,100,114,116,117,126,127,128,129,136,137,138,139,140,141,142,156,159,171,173,192,195,196,197,198,243,248,262,266,267,],[-46,-24,81,-34,-31,-32,-33,126,-48,-30,-35,126,-48,159,126,-30,-35,168,-112,-50,-36,-22,-23,-25,-26,-27,-28,-29,126,-47,190,-53,168,-49,-51,225,226,-35,-114,258,-52,168,271,168,]),'EQUALS':([6,9,19,27,32,37,40,45,46,47,66,67,93,118,119,127,128,129,130,131,132,133,134,136,137,138,139,140,143,144,145,146,148,149,154,],[54,54,54,-24,82,54,-34,-31,-32,-33,-30,-35,-67,-64,-70,-36,-22,-23,-68,54,54,54,-69,-25,-26,-27,-28,-29,-72,-73,54,54,54,54,-74,]),'MAYORIGUAL':([6,9,19,27,32,37,40,45,46,47,66,67,93,118,119,127,128,129,130,131,132,133,134,136,137,138,139,140,143,144,145,146,148,149,154,],[55,55,55,-24,-65,55,-34,-31,-32,-33,-30,-35,-67,-64,-70,-36,-22,-23,-68,55,55,55,-69,-25,-26,-27,-28,-29,-72,-73,55,55,55,55,-74,]),'MENORIGUAL':([6,9,19,27,32,37,40,45,46,47,66,67,93,118,119,127,128,129,130,131,132,133,134,136,137,138,139,140,143,144,145,146,148,149,154,],[56,56,56,-24,-65,56,-34,-31,-32,-33,-30,-35,-67,-64,-70,-36,-22,-23,-68,56,56,56,-69,-25,-26,-27,-28,-29,-72,-73,56,56,56,56,-74,]),'LESSTHAN':([6,9,19,27,32,37,40,45,46,47,66,67,93,118,119,127,128,129,130,131,132,133,134,136,137,138,139,140,143,144,145,146,148,149,154,],[57,57,57,-24,-65,57,-34,-31,-32,-33,-30,-35,-67,-64,-70,-36,-22,-23,-68,57,57,57,-69,-25,-26,-27,-28,-29,-72,-73,57,57,57,57,-74,]),'MORETHAN':([6,9,19,27,32,37,40,45,46,47,66,67,93,118,119,127,128,129,130,131,132,133,134,136,137,138,139,140,143,144,145,146,148,149,154,],[58,58,58,-24,-65,58,-34,-31,-32,-33,-30,-35,-67,-64,-70,-36,-22,-23,-68,58,58,58,-69,-25,-26,-27,-28,-29,-72,-73,58,58,58,58,-74,]),'DIFERENTE':([6,9,19,27,32,37,40,45,46,47,66,67,93,118,119,127,128,129,130,131,132,133,134,136,137,138,139,140,143,144,145,146,148,149,154,],[59,59,59,-24,83,59,-34,-31,-32,-33,-30,-35,-67,-64,-70,-36,-22,-23,-68,59,59,59,-69,-25,-26,-27,-28,-29,-72,-73,59,59,59,59,-74,]),'TIMES':([6,27,37,40,45,46,47,66,67,100,102,114,127,128,129,132,136,137,138,139,140,146,149,197,199,207,],[-35,74,-30,-34,-31,-32,-33,-30,-35,-30,-35,-35,-36,74,74,-35,-25,-26,-27,-28,-29,-35,-35,-35,-35,-35,]),'DIVIDE':([6,27,37,40,45,46,47,66,67,100,102,114,127,128,129,132,136,137,138,139,140,146,149,197,199,207,],[-35,75,-30,-34,-31,-32,-33,-30,-35,-30,-35,-35,-36,75,75,-35,-25,-26,-27,-28,-29,-35,-35,-35,-35,-35,]),'EXPONENTE':([6,27,37,40,45,46,47,66,67,100,102,114,127,128,129,132,136,137,138,139,140,146,149,197,199,207,],[-35,76,-30,-34,-31,-32,-33,-30,-35,-30,-35,-35,-36,76,76,-35,-25,-26,-27,-28,-29,-35,-35,-35,-35,-35,]),'DIVISIONENTERA':([6,27,37,40,45,46,47,66,67,100,102,114,127,128,129,132,136,137,138,139,140,146,149,197,199,207,],[-35,77,-30,-34,-31,-32,-33,-30,-35,-30,-35,-35,-36,77,77,-35,-25,-26,-27,-28,-29,-35,-35,-35,-35,-35,]),'MOD':([6,27,37,40,45,46,47,66,67,100,102,114,127,128,129,132,136,137,138,139,140,146,149,197,199,207,],[-35,78,-30,-34,-31,-32,-33,-30,-35,-30,-35,-35,-36,78,78,-35,-25,-26,-27,-28,-29,-35,-35,-35,-35,-35,]),'PLUS':([6,9,27,37,40,45,46,47,65,66,67,79,96,100,102,103,114,117,118,124,127,128,129,130,132,133,136,137,138,139,140,146,149,173,197,198,199,200,207,209,],[-35,68,-24,-30,-34,-31,-32,-33,68,-30,-35,68,68,-30,-35,68,-35,68,68,68,-36,-22,-23,68,-35,68,-25,-26,-27,-28,-29,-35,-35,68,-35,68,-35,68,-35,68,]),'MINUS':([6,9,27,37,40,45,46,47,65,66,67,79,96,100,102,103,114,117,118,124,127,128,129,130,132,133,136,137,138,139,140,146,149,173,197,198,199,200,207,209,],[-35,69,-24,-30,-34,-31,-32,-33,69,-30,-35,69,69,-30,-35,69,-35,69,69,69,-36,-22,-23,69,-35,69,-25,-26,-27,-28,-29,-35,-35,69,-35,69,-35,69,-35,69,]),'ELSE':([6,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,32,37,40,45,46,47,66,67,79,93,94,96,98,102,103,104,105,108,109,111,112,115,118,119,120,125,126,127,128,129,130,131,132,134,135,136,137,138,139,140,141,143,144,154,155,157,158,160,166,167,173,176,179,187,188,189,194,208,227,229,230,231,232,235,236,238,239,240,244,245,246,247,256,259,260,268,269,270,],[-35,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-24,-37,-38,-65,-30,-34,-31,-32,-33,-30,-35,-40,-67,-83,-48,-55,-35,-39,-42,-43,-61,-58,-56,-63,-119,-64,-70,-84,-60,-50,-36,-22,-23,-68,-71,-66,-69,-85,-25,-26,-27,-28,-29,-41,-72,-73,-74,-106,-57,-54,-62,-59,-120,-49,214,-94,-103,-104,-107,-105,-131,-127,-128,-129,-130,-132,254,255,-92,-93,-99,-100,-101,-102,-108,-90,-110,-109,-86,-88,-98,]),'RETURN':([6,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,32,37,40,45,46,47,66,67,79,93,94,96,98,102,103,104,105,108,109,111,112,115,118,119,120,125,126,127,128,129,130,131,132,134,135,136,137,138,139,140,141,143,144,154,155,157,158,160,166,167,173,176,179,187,188,189,194,208,227,229,230,231,232,234,235,236,238,239,240,244,245,246,247,252,256,259,260,268,269,270,],[-35,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-24,-37,-38,-65,-30,-34,-31,-32,-33,-30,-35,-40,-67,-83,-48,-55,-35,-39,-42,-43,-61,-58,-56,-63,-119,-64,-70,-84,-60,-50,-36,-22,-23,-68,-71,-66,-69,-85,-25,-26,-27,-28,-29,-41,-72,-73,-74,-106,-57,-54,-62,-59,-120,-49,-91,-94,-103,-104,-107,-105,-131,-127,-128,-129,-130,-132,253,-87,-89,-92,-93,-99,-100,-101,-102,-108,261,-90,-110,-109,-86,-88,-98,]),'AND':([6,19,20,27,32,40,45,46,47,66,67,93,94,118,119,120,127,128,129,130,131,132,134,135,136,137,138,139,140,143,144,145,148,154,],[60,60,60,-24,-65,-34,-31,-32,-33,-30,-35,-67,-83,-64,-70,-84,-36,-22,-23,-68,60,-66,-69,-85,-25,-26,-27,-28,-29,-72,-73,60,60,-74,]),'OR':([6,19,20,27,32,40,45,46,47,66,67,93,94,118,119,120,127,128,129,130,131,132,134,135,136,137,138,139,140,143,144,145,148,154,],[61,61,61,-24,-65,-34,-31,-32,-33,-30,-35,-67,-83,-64,-70,-84,-36,-22,-23,-68,61,-66,-69,-85,-25,-26,-27,-28,-29,-72,-73,61,61,-74,]),'RPAREN':([27,32,40,45,46,47,50,64,65,66,67,91,93,96,98,108,109,111,112,114,116,117,118,119,123,124,125,126,127,128,129,130,131,132,134,136,137,138,139,140,143,144,145,146,148,149,152,153,154,156,157,158,160,164,166,170,171,173,197,198,199,200,201,202,203,204,205,207,209,223,242,243,249,250,266,272,],[-24,-65,-34,-31,-32,-33,115,125,127,-30,-35,155,-67,-48,-55,-61,-58,-56,-63,-35,167,-112,-64,-70,172,127,-60,-50,-36,-22,-23,-68,-71,-66,-69,-25,-26,-27,-28,-29,-72,-73,174,175,177,178,187,188,-74,189,-57,-54,-62,194,-59,208,210,-49,-35,-114,227,229,230,-121,-122,-123,-124,231,232,247,257,-95,259,260,-96,-97,]),'CORCHETEDER':([27,40,45,46,47,66,67,95,96,110,126,127,128,129,136,137,138,139,140,173,],[-24,-34,-31,-32,-33,-30,-35,157,-48,166,-50,-36,-22,-23,-25,-26,-27,-28,-29,-49,]),'LLAVEDER':([27,40,44,45,46,47,66,67,96,97,99,100,126,127,128,129,136,137,138,139,140,159,173,192,206,248,],[-24,-34,98,-31,-32,-33,-30,-35,-48,158,160,-30,-50,-36,-22,-23,-25,-26,-27,-28,-29,-53,-49,-51,98,-52,]),'DOSPUNTOS':([40,45,46,47,67,85,87,100,108,109,112,125,127,157,160,166,172,174,175,177,178,180,183,184,185,191,210,214,254,255,257,],[-34,-31,-32,-33,-35,147,150,161,-61,-58,-63,-60,-36,-57,-62,-59,211,212,213,215,216,217,220,221,222,224,233,237,263,264,265,]),'AS':([48,],[101,]),'APPEND':([53,],[121,]),'REMOVE':([53,],[122,]),'IN':([88,],[151,]),'RANGE':([151,],[181,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cuerpo':([0,],[1,]),'import':([0,],[2,]),'funcionDeclaracion':([0,],[3,]),'cuerpoEstructura':([0,147,150,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[4,176,179,234,235,236,238,239,240,244,245,246,252,256,268,269,270,]),'expression':([0,8,30,43,44,49,50,51,63,70,71,80,84,86,110,123,126,147,150,168,169,170,182,186,206,211,212,213,215,216,217,220,221,222,233,237,253,261,263,264,265,],[9,65,79,96,96,103,117,118,124,130,133,96,133,133,96,117,173,9,9,198,200,209,96,96,96,9,9,9,9,9,9,9,9,9,9,9,117,117,9,9,9,]),'comentario':([0,147,150,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'asignacion':([0,147,150,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'if':([0,147,150,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'while':([0,147,150,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'for':([0,147,150,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'print':([0,147,150,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'funcion':([0,49,147,150,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[16,105,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'inputF':([0,147,150,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'openF':([0,147,150,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'comparacion':([0,71,84,86,147,150,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[19,131,145,148,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'operacionConectoresLogicos':([0,147,150,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'tupla':([0,49,147,150,151,163,169,211,212,213,215,216,217,218,220,221,222,228,233,237,263,264,265,],[21,108,21,21,184,108,203,21,21,21,21,21,21,108,21,21,21,108,21,21,21,21,21,]),'lista':([0,49,147,150,151,163,169,211,212,213,215,216,217,218,220,221,222,228,233,237,263,264,265,],[22,109,22,22,183,109,202,22,22,22,22,22,22,109,22,22,22,109,22,22,22,22,22,]),'diccionario':([0,49,147,150,163,169,211,212,213,215,216,217,220,221,222,228,233,237,263,264,265,],[23,111,23,23,111,205,23,23,23,23,23,23,23,23,23,111,23,23,23,23,23,]),'conjunto':([0,49,147,150,151,163,169,211,212,213,215,216,217,218,220,221,222,228,233,237,263,264,265,],[24,112,24,24,185,112,204,24,24,24,24,24,24,112,24,24,24,112,24,24,24,24,24,]),'append':([0,147,150,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'remove':([0,147,150,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'term':([0,8,30,43,44,49,50,51,63,68,69,70,71,80,84,86,110,123,126,147,150,168,169,170,182,186,206,211,212,213,215,216,217,220,221,222,233,237,253,261,263,264,265,],[27,27,27,27,27,27,27,27,27,128,129,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'multipleAsignacion':([0,49,147,150,163,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[30,113,30,30,113,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'valoresID':([0,147,150,211,212,213,215,216,217,220,221,222,233,237,263,264,265,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'factor':([0,8,30,43,44,49,50,51,63,68,69,70,71,74,75,76,77,78,80,84,86,89,90,110,123,126,147,150,159,161,168,169,170,182,186,206,211,212,213,215,216,217,220,221,222,224,233,237,253,261,263,264,265,],[37,66,66,66,100,66,66,66,66,66,66,66,37,136,137,138,139,140,66,37,37,152,154,66,66,66,37,37,191,192,66,66,66,66,66,100,37,37,37,37,37,37,37,37,37,248,37,37,66,66,37,37,37,]),'operadorLogico':([6,9,19,37,131,132,133,145,146,148,149,],[51,70,72,90,72,51,70,72,51,72,51,]),'conectoresLogicos':([6,19,20,131,145,148,],[52,71,73,71,71,71,]),'valoresComa':([8,43,44,80,110,182,186,206,],[64,95,99,141,95,64,99,99,]),'valoresDic':([44,206,],[97,97,]),'parametros':([50,123,253,261,],[116,171,262,267,]),'datos':([169,],[201,]),'dentroFor':([219,],[242,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> cuerpo","S'",1,None,None,None),
  ('cuerpo -> import','cuerpo',1,'p_cuerpo','sintatico.py',9),
  ('cuerpo -> funcionDeclaracion','cuerpo',1,'p_cuerpo','sintatico.py',10),
  ('cuerpo -> cuerpoEstructura','cuerpo',1,'p_cuerpo','sintatico.py',11),
  ('cuerpoEstructura -> expression','cuerpoEstructura',1,'p_cuerpoEstructuras','sintatico.py',15),
  ('cuerpoEstructura -> comentario','cuerpoEstructura',1,'p_cuerpoEstructuras','sintatico.py',16),
  ('cuerpoEstructura -> asignacion','cuerpoEstructura',1,'p_cuerpoEstructuras','sintatico.py',17),
  ('cuerpoEstructura -> if','cuerpoEstructura',1,'p_cuerpoEstructuras','sintatico.py',18),
  ('cuerpoEstructura -> while','cuerpoEstructura',1,'p_cuerpoEstructuras','sintatico.py',19),
  ('cuerpoEstructura -> for','cuerpoEstructura',1,'p_cuerpoEstructuras','sintatico.py',20),
  ('cuerpoEstructura -> print','cuerpoEstructura',1,'p_cuerpoEstructuras','sintatico.py',21),
  ('cuerpoEstructura -> funcion','cuerpoEstructura',1,'p_cuerpoEstructuras','sintatico.py',22),
  ('cuerpoEstructura -> inputF','cuerpoEstructura',1,'p_cuerpoEstructuras','sintatico.py',23),
  ('cuerpoEstructura -> openF','cuerpoEstructura',1,'p_cuerpoEstructuras','sintatico.py',24),
  ('cuerpoEstructura -> comparacion','cuerpoEstructura',1,'p_cuerpoEstructuras','sintatico.py',25),
  ('cuerpoEstructura -> operacionConectoresLogicos','cuerpoEstructura',1,'p_cuerpoEstructuras','sintatico.py',26),
  ('cuerpoEstructura -> tupla','cuerpoEstructura',1,'p_cuerpoEstructuras','sintatico.py',27),
  ('cuerpoEstructura -> lista','cuerpoEstructura',1,'p_cuerpoEstructuras','sintatico.py',28),
  ('cuerpoEstructura -> diccionario','cuerpoEstructura',1,'p_cuerpoEstructuras','sintatico.py',29),
  ('cuerpoEstructura -> conjunto','cuerpoEstructura',1,'p_cuerpoEstructuras','sintatico.py',30),
  ('cuerpoEstructura -> append','cuerpoEstructura',1,'p_cuerpoEstructuras','sintatico.py',31),
  ('cuerpoEstructura -> remove','cuerpoEstructura',1,'p_cuerpoEstructuras','sintatico.py',32),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','sintatico.py',37),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','sintatico.py',42),
  ('expression -> term','expression',1,'p_expression_term','sintatico.py',47),
  ('term -> term TIMES factor','term',3,'p_term_times','sintatico.py',51),
  ('term -> term DIVIDE factor','term',3,'p_term_div','sintatico.py',56),
  ('term -> term EXPONENTE factor','term',3,'p_term_cuadrado','sintatico.py',61),
  ('term -> term DIVISIONENTERA factor','term',3,'p_term_divEntera','sintatico.py',66),
  ('term -> term MOD factor','term',3,'p_term_Mod','sintatico.py',71),
  ('term -> factor','term',1,'p_term_factor','sintatico.py',76),
  ('factor -> NUMBER','factor',1,'p_factor_num','sintatico.py',80),
  ('factor -> STRING','factor',1,'p_factor_num','sintatico.py',81),
  ('factor -> FLOAT','factor',1,'p_factor_num','sintatico.py',82),
  ('factor -> CADENA','factor',1,'p_factor_num','sintatico.py',83),
  ('factor -> ID','factor',1,'p_factor_num','sintatico.py',84),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','sintatico.py',89),
  ('comentario -> COMMENT','comentario',1,'p_comentario','sintatico.py',93),
  ('comentario -> COMMENTS','comentario',1,'p_comentario','sintatico.py',94),
  ('asignacion -> ID ASSIGN expression','asignacion',3,'p_asignacion','sintatico.py',98),
  ('asignacion -> multipleAsignacion expression','asignacion',2,'p_asignacion','sintatico.py',99),
  ('asignacion -> valoresID ASSIGN valoresComa','asignacion',3,'p_asignacion','sintatico.py',100),
  ('asignacion -> ID ASSIGN BOOLEAN','asignacion',3,'p_asignacion','sintatico.py',101),
  ('asignacion -> ID ASSIGN funcion','asignacion',3,'p_asignacion','sintatico.py',102),
  ('multipleAsignacion -> ID ASSIGN','multipleAsignacion',2,'p_multipleAsignacion','sintatico.py',106),
  ('multipleAsignacion -> ID ASSIGN multipleAsignacion','multipleAsignacion',3,'p_multipleAsignacion','sintatico.py',107),
  ('valoresID -> ID','valoresID',1,'p_valoresID','sintatico.py',110),
  ('valoresID -> valoresID COMA ID','valoresID',3,'p_valoresID','sintatico.py',111),
  ('valoresComa -> expression','valoresComa',1,'p_valoresComa','sintatico.py',114),
  ('valoresComa -> valoresComa COMA expression','valoresComa',3,'p_valoresComa','sintatico.py',115),
  ('valoresComa -> valoresComa COMA','valoresComa',2,'p_valoresComa','sintatico.py',116),
  ('valoresDic -> factor DOSPUNTOS factor','valoresDic',3,'p_valoresDic','sintatico.py',120),
  ('valoresDic -> valoresDic COMA factor DOSPUNTOS factor','valoresDic',5,'p_valoresDic','sintatico.py',121),
  ('valoresDic -> valoresDic COMA','valoresDic',2,'p_valoresDic','sintatico.py',122),
  ('diccionario -> LLAVEIZQ valoresDic LLAVEDER','diccionario',3,'p_diccionario','sintatico.py',126),
  ('diccionario -> LLAVEIZQ LLAVEDER','diccionario',2,'p_diccionario','sintatico.py',127),
  ('diccionario -> ID ASSIGN diccionario','diccionario',3,'p_diccionario','sintatico.py',128),
  ('lista -> CORCHETEIZQ valoresComa CORCHETEDER','lista',3,'p_lista','sintatico.py',132),
  ('lista -> ID ASSIGN lista','lista',3,'p_lista','sintatico.py',133),
  ('lista -> ID ASSIGN CORCHETEIZQ CORCHETEDER','lista',4,'p_lista','sintatico.py',134),
  ('tupla -> LPAREN valoresComa RPAREN','tupla',3,'p_tupla','sintatico.py',138),
  ('tupla -> ID ASSIGN tupla','tupla',3,'p_tupla','sintatico.py',139),
  ('conjunto -> LLAVEIZQ valoresComa LLAVEDER','conjunto',3,'p_conjunto','sintatico.py',143),
  ('conjunto -> ID ASSIGN conjunto','conjunto',3,'p_conjunto','sintatico.py',144),
  ('comparacion -> ID operadorLogico expression','comparacion',3,'p_comparacion','sintatico.py',148),
  ('comparacion -> BOOLEAN','comparacion',1,'p_comparacion','sintatico.py',149),
  ('comparacion -> comparacion conectoresLogicos ID','comparacion',3,'p_comparacion','sintatico.py',150),
  ('comparacion -> NOTS BOOLEAN','comparacion',2,'p_comparacion','sintatico.py',151),
  ('comparacion -> expression operadorLogico expression','comparacion',3,'p_comparacion','sintatico.py',152),
  ('comparacion -> comparacion operadorLogico ID','comparacion',3,'p_comparacion','sintatico.py',153),
  ('comparacion -> ID operadorLogico BOOLEAN','comparacion',3,'p_comparacion','sintatico.py',154),
  ('comparacion -> comparacion conectoresLogicos comparacion','comparacion',3,'p_comparacion','sintatico.py',155),
  ('comparacion -> BOOLEAN EQUALS BOOLEAN','comparacion',3,'p_comparacion','sintatico.py',156),
  ('comparacion -> BOOLEAN DIFERENTE BOOLEAN','comparacion',3,'p_comparacion','sintatico.py',157),
  ('comparacion -> factor operadorLogico factor','comparacion',3,'p_comparacion','sintatico.py',158),
  ('operadorLogico -> EQUALS','operadorLogico',1,'p_operadorLogico','sintatico.py',164),
  ('operadorLogico -> MAYORIGUAL','operadorLogico',1,'p_operadorLogico','sintatico.py',165),
  ('operadorLogico -> MENORIGUAL','operadorLogico',1,'p_operadorLogico','sintatico.py',166),
  ('operadorLogico -> LESSTHAN','operadorLogico',1,'p_operadorLogico','sintatico.py',167),
  ('operadorLogico -> MORETHAN','operadorLogico',1,'p_operadorLogico','sintatico.py',168),
  ('operadorLogico -> DIFERENTE','operadorLogico',1,'p_operadorLogico','sintatico.py',169),
  ('conectoresLogicos -> AND','conectoresLogicos',1,'p_conectoresLogicos','sintatico.py',173),
  ('conectoresLogicos -> OR','conectoresLogicos',1,'p_conectoresLogicos','sintatico.py',174),
  ('operacionConectoresLogicos -> NOT ID','operacionConectoresLogicos',2,'p_operacionConectoresLogicos','sintatico.py',177),
  ('operacionConectoresLogicos -> ID conectoresLogicos ID','operacionConectoresLogicos',3,'p_operacionConectoresLogicos','sintatico.py',178),
  ('operacionConectoresLogicos -> operacionConectoresLogicos conectoresLogicos ID','operacionConectoresLogicos',3,'p_operacionConectoresLogicos','sintatico.py',179),
  ('if -> IF LPAREN comparacion RPAREN DOSPUNTOS cuerpoEstructura ELSE DOSPUNTOS cuerpoEstructura','if',9,'p_if','sintatico.py',183),
  ('if -> IF LPAREN comparacion RPAREN DOSPUNTOS cuerpoEstructura','if',6,'p_if','sintatico.py',184),
  ('if -> IF LPAREN ID RPAREN DOSPUNTOS cuerpoEstructura ELSE DOSPUNTOS cuerpoEstructura','if',9,'p_if','sintatico.py',185),
  ('if -> IF LPAREN ID RPAREN DOSPUNTOS cuerpoEstructura','if',6,'p_if','sintatico.py',186),
  ('if -> IF ID DOSPUNTOS cuerpoEstructura ELSE DOSPUNTOS cuerpoEstructura','if',7,'p_if','sintatico.py',187),
  ('if -> IF ID DOSPUNTOS cuerpoEstructura','if',4,'p_if','sintatico.py',188),
  ('while -> WHILE LPAREN comparacion RPAREN DOSPUNTOS cuerpoEstructura','while',6,'p_while','sintatico.py',197),
  ('while -> WHILE LPAREN ID RPAREN DOSPUNTOS cuerpoEstructura','while',6,'p_while','sintatico.py',198),
  ('while -> WHILE ID DOSPUNTOS cuerpoEstructura','while',4,'p_while','sintatico.py',199),
  ('dentroFor -> NUMBER','dentroFor',1,'p_dentroFor','sintatico.py',202),
  ('dentroFor -> NUMBER COMA NUMBER','dentroFor',3,'p_dentroFor','sintatico.py',203),
  ('dentroFor -> NUMBER COMA NUMBER COMA NUMBER','dentroFor',5,'p_dentroFor','sintatico.py',204),
  ('for -> FOR ID IN RANGE LPAREN dentroFor RPAREN DOSPUNTOS cuerpoEstructura','for',9,'p_for','sintatico.py',207),
  ('for -> FOR ID IN ID DOSPUNTOS cuerpoEstructura','for',6,'p_for','sintatico.py',208),
  ('for -> FOR ID IN lista DOSPUNTOS cuerpoEstructura','for',6,'p_for','sintatico.py',209),
  ('for -> FOR ID IN tupla DOSPUNTOS cuerpoEstructura','for',6,'p_for','sintatico.py',210),
  ('for -> FOR ID IN conjunto DOSPUNTOS cuerpoEstructura','for',6,'p_for','sintatico.py',211),
  ('print -> PRINT LPAREN factor RPAREN','print',4,'p_print','sintatico.py',215),
  ('print -> PRINT LPAREN ID RPAREN','print',4,'p_print','sintatico.py',216),
  ('inputF -> ID ASSIGN INPUT LPAREN RPAREN','inputF',5,'p_input','sintatico.py',220),
  ('inputF -> INPUT LPAREN RPAREN','inputF',3,'p_input','sintatico.py',221),
  ('openF -> OPEN LPAREN CADENA RPAREN','openF',4,'p_open','sintatico.py',225),
  ('openF -> OPEN LPAREN CADENA COMA CADENA RPAREN','openF',6,'p_open','sintatico.py',226),
  ('openF -> ID ASSIGN OPEN LPAREN CADENA COMA CADENA RPAREN','openF',8,'p_open','sintatico.py',227),
  ('openF -> ID ASSIGN OPEN LPAREN ID COMA CADENA RPAREN','openF',8,'p_open','sintatico.py',228),
  ('parametros -> ID','parametros',1,'p_parametros','sintatico.py',231),
  ('parametros -> expression','parametros',1,'p_parametros','sintatico.py',232),
  ('parametros -> parametros COMA ID','parametros',3,'p_parametros','sintatico.py',233),
  ('parametros -> parametros COMA expression','parametros',3,'p_parametros','sintatico.py',234),
  ('funcionDeclaracion -> DEF ID LPAREN parametros RPAREN DOSPUNTOS cuerpoEstructura RETURN parametros','funcionDeclaracion',9,'p_funcionDeclaracion','sintatico.py',237),
  ('funcionDeclaracion -> DEF ID LPAREN RPAREN DOSPUNTOS cuerpoEstructura RETURN parametros','funcionDeclaracion',8,'p_funcionDeclaracion','sintatico.py',238),
  ('funcionDeclaracion -> DEF ID LPAREN RPAREN DOSPUNTOS cuerpoEstructura','funcionDeclaracion',6,'p_funcionDeclaracion','sintatico.py',239),
  ('funcionDeclaracion -> DEF ID LPAREN parametros RPAREN DOSPUNTOS cuerpoEstructura','funcionDeclaracion',7,'p_funcionDeclaracion','sintatico.py',240),
  ('funcion -> ID LPAREN RPAREN','funcion',3,'p_funcion','sintatico.py',243),
  ('funcion -> ID LPAREN parametros RPAREN','funcion',4,'p_funcion','sintatico.py',244),
  ('datos -> lista','datos',1,'p_estructuraDatos','sintatico.py',249),
  ('datos -> tupla','datos',1,'p_estructuraDatos','sintatico.py',250),
  ('datos -> conjunto','datos',1,'p_estructuraDatos','sintatico.py',251),
  ('datos -> diccionario','datos',1,'p_estructuraDatos','sintatico.py',252),
  ('return -> RETURN expression','return',2,'p_return','sintatico.py',255),
  ('return -> RETURN NONE','return',2,'p_return','sintatico.py',256),
  ('append -> ID PUNTO APPEND LPAREN ID RPAREN','append',6,'p_append','sintatico.py',260),
  ('append -> ID PUNTO APPEND LPAREN expression RPAREN','append',6,'p_append','sintatico.py',261),
  ('append -> ID PUNTO APPEND LPAREN datos RPAREN','append',6,'p_append','sintatico.py',262),
  ('remove -> ID PUNTO REMOVE LPAREN ID RPAREN','remove',6,'p_remove','sintatico.py',266),
  ('remove -> ID PUNTO REMOVE LPAREN RPAREN','remove',5,'p_remove','sintatico.py',267),
  ('remove -> ID PUNTO REMOVE LPAREN expression RPAREN','remove',6,'p_remove','sintatico.py',268),
  ('import -> IMPORT ID','import',2,'p_import','sintatico.py',271),
  ('import -> IMPORT ID AS ID','import',4,'p_import','sintatico.py',272),
]
