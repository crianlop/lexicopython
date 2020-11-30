import tkinter as tk
from tkinter import *
from tkinter import ttk, font
from PIL import Image, ImageChops, ImageEnhance, ImageOps

def analizador_lexico():
    text_input = texto.get("1.0","end-1c")
    print(text_input)

def analizador_sintactico():
    text_input = texto.get("1.0","end-1c")
    print(text_input)

app = tk.Tk()
app.title("Analizador")
app.geometry('1000x800')
fuente = font.Font(weight='bold')
app.config(bd=24,relief="sunken")
label = tk.Label(app,text="Bienvenidos al Analizador",font=fuente)
label.pack(side=TOP)
#textArea
texto = tk.Text(app)
scrollbar = Scrollbar()
texto.config(height = 25, width = 70,background = "#C6C2C6", yscrollcommand=scrollbar.set)
scrollbar.config(command=texto.yview)
scrollbar.pack(side=RIGHT, fill=Y)
texto.pack(padx = 10, pady = 10)
botones = tk.Frame()
imgSintactico = PhotoImage(file='sintactico.png')
imgLexico = PhotoImage(file='lexico.png')
#imgLexico.subsample(2)
lexico = tk.Button(botones,text="Anlizador Lexico",image=imgLexico,command=analizador_lexico)
sintactico = tk.Button(botones,text="Anlizador Sintactico",image=imgSintactico,command=analizador_sintactico)
lexico.grid(row=0,column=0)
sintactico.grid(row=0,column=1)
botones.config(width=1,height=1)
botones.pack()



app.mainloop()
print("programa termino")
#text_input = TextArea.get("1.0","end-1c")