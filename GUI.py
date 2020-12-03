from lexicoPython import analizar
from sintatico import analizarS
import tkinter as tk
from tkinter import *
from tkinter import ttk, font
from disenio import * 
import ply

def analizador_lexico():
    respuesta.configure(state = NORMAL)
    respuesta.delete("1.0","end-1c")
    text_input = texto.get("1.0","end-1c")
    lista = text_input.split("\n")
    z =0
    for linea in lista:
        z = z+1
        igual = True
        if(linea != ""):
            for i in analizar(linea):
                print(analizar(linea))
                if(i=="Ilegal" and igual):
                    rep = "-Error en esta línea Carácter no definido" + "\n"+ " "+str(z)+" : "+linea + 2*"\n" 
                    respuesta.insert(END,rep)
                    igual = False
    respuesta.tag_configure("red", foreground="red")
    find(respuesta,"-Error en esta línea Carácter no definido")
    labellexico["text"] = "Se analizó el léxico"
    respuesta.configure(state = DISABLED)
    

def analizador_sintactico():
    respuesta.configure(state = NORMAL)
    respuesta.delete("1.0","end-1c")
    text_input = texto.get("1.0","end-1c")
    lista = text_input.split("\n")
    z =0
    for linea in lista:
        z = z+1
        if(linea != ""):
            result = analizarS(linea)
            if(result == None):
                rep = "-Error de sintaxis en esta línea " + "\n"+ " "+str(z)+" : "+linea + 2*"\n" 
                respuesta.insert(END,rep)   
    respuesta.tag_configure("red", foreground="red")
    find(respuesta,"-Error de sintaxis en esta línea ")
    labellexico["text"] = "Se analizó la sintaxis"
    respuesta.configure(state = DISABLED)
    

def on_text_click(event):
    #function that gets called whenever text is clicked
    if texto.get("1.0","end-1c") == 'Ingrese su código aqui...':
       texto.delete("1.0", END) # delete all the text in the entry
       texto.insert(INSERT, '') #Insert blank for user input
       texto.config(fg = 'black')
def on_focusout(event):
    if texto.get("1.0","end-1c") == '':
        texto.insert(INSERT, 'Ingrese su código aqui...')
        texto.config(fg = 'grey')


app = tk.Tk()
app.title("Analizador")
app.geometry('1220x800')
app.resizable(width=FALSE,height=FALSE)
fuente = font.Font(weight='bold',family="times", size=24,slant="italic")
app.config(bd=24,relief="sunken")
label = tk.Label(app,text="Bienvenidos al Analizador",font=fuente)
label.pack(side=TOP)
#textArea
labels=tk.Frame()
labelt = tk.Label(labels,text="Ingrese Código",font=fuente, relief="groove", borderwidth=5,fg="red")
labelt3 = tk.Label(labels,text="Respuesta",font=fuente, relief="groove", borderwidth=5,fg="red")
sep = ttk.Separator(labels,orient="vertical").grid(row=0,column=1, sticky="sn",ipadx=200)
labelt.grid(row=0,column=0)
labelt3.grid(row=0,column=3)
labels.pack()

textos = tk.Frame(app)
fuente2 = ("Consolas",11,"italic")
texto = tk.Text(textos)
scrollbar = Scrollbar(texto)
texto.config(font=fuente2,height = 25, width = 70,background = "#C6C2C6", yscrollcommand=scrollbar.set)
texto.insert(INSERT, 'Ingrese su código aqui...')
texto.bind('<FocusIn>', on_text_click)
texto.bind('<FocusOut>', on_focusout)
texto.config(fg = 'grey')

scrollbar.config(command=texto.yview)
#scrollbar.pack(side=RIGHT, fill=Y)
respuesta = tk.Text(textos)
scrolRes = Scrollbar()
respuesta.config(font=fuente2,height = 25, width = 70,background = "#C6C2C6", yscrollcommand=scrolRes.set)
scrolRes.config(command=respuesta.yview)
scrolRes.pack(side=RIGHT, fill=Y)
texto.grid(row=0,column=0)
respuesta.grid(row=0,column=3)
respuesta.configure(state = DISABLED)
sep = ttk.Separator(textos,orient="vertical").grid(row=0,column=2, sticky="sn",ipadx=10)

textos.pack()

#botones
botones = tk.Frame()
imgSintactico = PhotoImage(file='lexicopython\sintactico.png')
imgSintactico = imgSintactico.subsample(2,2)
imgLexico = PhotoImage(file='lexicopython\lexico.png')
imgLexico = imgLexico.subsample(2,2)
lexico = tk.Button(botones,text="Anlizador Lexico",image=imgLexico,command=analizador_lexico, borderwidth=15, relief="raised", height = 120, width = 120)
toolLexico = CreateToolTip(lexico,"Analizar Léxico")
sintactico = tk.Button(botones,text="Anlizador Sintáctico",image=imgSintactico,command=analizador_sintactico, borderwidth=15, relief="raised", height = 120, width = 120)
toolSintctico = CreateToolTip(sintactico,"Analizar Sintaxis")
lexico.grid(row=0,column=0)
sintactico.grid(row=0,column=3)
botones.config(width=100,height=100)
sep = ttk.Separator(botones,orient="vertical").grid(row=0,column=2, sticky="sn",ipadx=10)
botones.pack(side=LEFT)
labellexico = tk.Label(text="",font=fuente, borderwidth=5,fg="blue")
labellexico.pack()





app.mainloop()
print("programa termino")
