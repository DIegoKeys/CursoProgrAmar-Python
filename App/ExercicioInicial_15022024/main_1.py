import tkinter
from tkinter import *

class App:
    def __init__(self,tkJanela):
        self.lstbxPreferencias = Listbox(tkJanela, height=13,width=50)
        self.btnMensagem = Button(tkJanela, text='Mensagem',command=self.mensagem,width=30)
        self.btnDesvCond = Button(tkJanela, text='DesvCond',command=self.desvCond,width=30)
        self.btnDesvCondEncad = Button(tkJanela, text='DesvCondEncad', command=self.desvCondEncad,width=30)
        self.btnMatchCase = Button(tkJanela,text='MatchCase', command=self.matchCase, width=30)
        self.btnImportaTxtWhile = Button(tkJanela,text='ImportaTxtWhile', command=self.importaTxtWhile,width=30)
        self.btnImportaTxtFor = Button(tkJanela, text='ImportaTxtFor', command=self.importaTxtFor, width=30)
        self.btnImportaTxtForeach = Button(tkJanela, text='ImportaTxtForeach', command=self.importaTxtForeach, width=30)
        self.btnDesvCond
        self.btnDesvCondEncad
        self.btnMatchCase
        self.btnImportaTxtWhile
        self.btnImportaTxtFor
        self.btnImportaTxtForeach

tkJanela = Tk()
objJanela = App(tkJanela)
tkJanela.title('Python Aplication')
tkJanela.geometry("600x250+10+10")
tkJanela.mainloop()