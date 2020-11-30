import tkinter as tk
from tkinter import *

class CreateToolTip(object):
    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)
    def enter(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx()
        y += self.widget.winfo_rooty()
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',background='white', relief='solid', borderwidth=1,font=("times", "12", "normal"))
        label.pack(ipadx=1)
    def close(self, event=None):
        if self.tw:
            self.tw.destroy()

def find(respuesta,Cadena): 
    respuesta.tag_remove('found', '1.0', END)  
    busca = Cadena 
    if busca: 
        indice = '1.0'
        while 1: 
            indice = respuesta.search(busca, indice, nocase=1,stopindex=END)  
            if not indice: break
            lastindice = '%s+%dc' % (indice, len(busca))  
            respuesta.tag_add('found', indice, lastindice)  
            indice = lastindice 
        respuesta.tag_config('found', foreground='red',background="yellow")  