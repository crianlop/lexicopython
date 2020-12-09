import numpy

lista = []
entrada = input()
vacio = ""
nombreArchivo = "archivo.py"
if(entrada != vacio): 
    archivo = open(entrada,'r')
else:
    archivo = open(nombreArchivo,'r')
a = b = 0
bandera = True
for linea in archivo:
    a = a + 1