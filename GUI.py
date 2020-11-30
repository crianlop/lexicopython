import tkinter as tk
from tkinter import *
from tkinter import ttk, font
from tkinter.ttk import Style
from PIL import Image, ImageChops, ImageEnhance, ImageOps
from disenio import CreateToolTip

def analizador_lexico():
    text_input = texto.get("1.0","end-1c")
    if(text_input != " "):
        print(text_input)

def analizador_sintactico():
    text_input = texto.get("1.0","end-1c")
    if(text_input != " "):
        print(text_input)

def on_text_click(event):
    #function that gets called whenever text is clicked
    if texto.get("1.0","end-1c") == 'Ingrese su codigo aqui...':
       texto.delete("1.0", END) # delete all the text in the entry
       texto.insert(INSERT, '') #Insert blank for user input
       texto.config(fg = 'black')
def on_focusout(event):
    if texto.get("1.0","end-1c") == '':
        texto.insert(INSERT, 'Ingrese su codigo aqui...')
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
textos = tk.Frame(app)

texto = tk.Text(textos)
scrollbar = Scrollbar(texto)
texto.config(height = 25, width = 70,background = "#C6C2C6", yscrollcommand=scrollbar.set)
texto.insert(INSERT, 'Ingrese su codigo aqui...')
texto.bind('<FocusIn>', on_text_click)
texto.bind('<FocusOut>', on_focusout)
texto.config(fg = 'grey')

scrollbar.config(command=texto.yview)
#scrollbar.pack(side=RIGHT, fill=Y)
respuesta = tk.Text(textos)
scrolRes = Scrollbar()
respuesta.config(height = 25, width = 70,background = "#C6C2C6", yscrollcommand=scrolRes.set)
scrolRes.config(command=respuesta.yview)
scrolRes.pack(side=RIGHT, fill=Y)
respuesta.grid(row=0,column=0)
texto.grid(row=0,column=3)
sep = ttk.Separator(textos,orient="vertical").grid(row=0,column=2, sticky="sn",ipadx=10)

textos.pack()

#botones
botones = tk.Frame()
imgSintactico = PhotoImage(file='sintactico.png')
imgLexico = PhotoImage(file='lexico.png')
lexico = tk.Button(botones,text="Anlizador Lexico",image=imgLexico,command=analizador_lexico, borderwidth=15, relief="raised")
toolLexico = CreateToolTip(lexico,"Analizar Lexico")
sintactico = tk.Button(botones,text="Anlizador Sintactico",image=imgSintactico,command=analizador_sintactico, borderwidth=15, relief="raised")
toolSintctico = CreateToolTip(sintactico,"Analizar Sintaxis")
lexico.grid(row=0,column=0)
sintactico.grid(row=0,column=3)
botones.config(width=100,height=100)
sep = ttk.Separator(botones,orient="vertical").grid(row=0,column=2, sticky="sn",ipadx=10)
botones.pack(side=LEFT)






app.mainloop()
print("programa termino")
#text_input = TextArea.get("1.0","end-1c")