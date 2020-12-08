import numpy

lista = []
entrada = input()
nombreArchivo = "archivo.py"
if(entrada != ""): 
    archivo = open(entrada,'r')
else:
    archivo = open(nombreArchivo,'r')
a = b = 0
bandera = True
for linea in archivo:
    a = a + 1