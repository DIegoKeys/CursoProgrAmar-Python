import tkinter
from tkinter import *

class MyWindow:
    def __init__(self,tkjanela):
        btnWidth = 30
        self.btnMensagem = Button.configure(tkjanela,text="Parabens primiero texto",command=self.mensagem, width=btnWidth)
tkjanela = tkinter.Tk()
MyWindow(tkjanela)
tkjanela.geometry("600x500")
tkjanela.title("Python Test Window")
tkjanela.mainloop()
