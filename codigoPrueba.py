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

def funcion(a,b):
    z = a + b
    return z

for linea in archivo:
    a = a + 1
    if ( b > a and bandera):
        print(linea)
        lista.append(linea)
    else:
        lista.remove()
        z = funcion(a,b)
        print(z)