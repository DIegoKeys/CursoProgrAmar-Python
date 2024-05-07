import tkinter
import tkinter.messagebox
from tkinter import *

class App:
    def __init__(self,tkJanela):
        self.lstbxPreferencias = Listbox(tkJanela, width=55,height=13)
        self.btnMensagem = Button(tkJanela,text="Mensagem",command=self.mensagem,width=30)
        self.btnDesvCond = Button(tkJanela, text="DesvCond", command=self.desvCond, width=30)
        self.btnDesvCondEncad = Button(tkJanela, text="DesvCondEncad", command=self.desvCondEncad, width=30)
        self.btnMatchCase = Button(tkJanela, text="MatchCase", command=self.matchCase, width=30)
        self.btnImportarTxtWhile = Button(tkJanela, text="ImportarTxtWhile", command=self.importarTxtWhile, width=30)
        self.btnImportarTxtFor = Button(tkJanela, text="ImportarTxtFor", command=self.importarTxtFor, width=30)
        self.btnImportarTxtForeach = Button(tkJanela, text="ImportarTxtForeach", command=self.importarTxtForeach, width=30)
        self.lstbxPreferencias.place(x=250,y=10)
        self.btnMensagem.place(x=10,y=10)
        self.btnDesvCond.place(x=10,y=40)
        self.btnDesvCondEncad.place(x=10,y=70)
        self.btnMatchCase.place(x=10,y=100)
        self.btnImportarTxtWhile.place(x=10,y=130)
        self.btnImportarTxtFor.place(x=10,y=160)
        self.btnImportarTxtForeach.place(x=10,y=190)

    def mensagem(self):
        tkinter.messagebox.showinfo("Mensagem","Parabéns pelo primiero Botão")
    def desvCond(self):
        resultado = tkinter.messagebox.askokcancel("Responda ok ou Cancelar","Gostaria de compartilhar os seus dados?")
        if resultado:
            tkinter.messagebox.showinfo("Resposta Ok", "Obrigado por compartilhar os dados")
        else:
            tkinter.messagebox.showinfo("Resposta Cancelar", "Os dados não foram compartilhados")
    def desvCondEncad(self):
        resultado = tkinter.messagebox.askyesnocancel("Responda sim ou não ou Cancelar","Gostaria de compartilhar os seus dados?")
        if resultado:
            tkinter.messagebox.showinfo("Resposta sim", "Obrigado por compartilhar os dados")
        elif resultado is False:
            tkinter.messagebox.showinfo("Resposta não", "Os dados não foram compartilhados")
        else:
            tkinter.messagebox.showinfo("Resposta Cancelar", "Os dados não foram compartilhados")
    def matchCase(self):
        resultado = tkinter.messagebox.askyesnocancel("Responda sim ou não ou Cancelar","Gostaria de compartilhar os seus dados?")
        match resultado:
            case True:
                tkinter.messagebox.showinfo("Resposta sim", "Obrigado por compartilhar os dados")
            case False:
                tkinter.messagebox.showinfo("Resposta não", "Os dados não foram compartilhados")
            case None:
                tkinter.messagebox.showinfo("Resposta Cancelar", "Os dados não foram compartilhados")
            case _:
                tkinter.messagebox.showinfo("Resposta Error", "Os dados não foram compartilhados")

    def importarTxtWhile(self):
        self.lstbxPreferencias.delete(0,END)
        with open("H:\\ToscanoAulas\\preferencias.txt") as arquivo:
            linhaLida = arquivo.readline()
            while linhaLida != '':
                self.lstbxPreferencias.insert(END,linhaLida)
                linhaLida = arquivo.readline()
            arquivo.close()

    def importarTxtFor(self):
        self.lstbxPreferencias.delete(0, END)
        with open("H:\\ToscanoAulas\\preferencias.txt") as arquivo:
            list = arquivo.readlines()
            [self.lstbxPreferencias.insert(END,list[x]) for x in range(0,len(list))]
            arquivo.close()

    def importarTxtForeach(self):
        self.lstbxPreferencias.delete(0, END)
        with open("H:\\ToscanoAulas\\preferencias.txt") as arquivo:
            list = arquivo.readlines()
            [self.lstbxPreferencias.insert(END,x) for x in list]
            arquivo.close()
tkJanela = Tk()
App(tkJanela)
tkJanela.title("Janela Exercicio")
tkJanela.geometry("600x250+10+10")
tkJanela.mainloop()
