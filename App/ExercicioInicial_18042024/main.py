import pyodbc
import tkinter.messagebox
from tkinter import *


class MyWindow:
    def __init__(self,tkJanela):
        self.dfwidth = 30
        self.lstbxPreferencias = Listbox(tkJanela,height=50,width=18)
        self.btnMensagem = Button(tkJanela,text="Mensagem",command=self.mensagem,width=self.dfwidth)
        self.btnDesvCond = Button(tkJanela, text="Mensagem", command=self.desvCond, width=self.dfwidth)
        self.btnDesvCondEncad = Button(tkJanela, text="Mensagem", command=self.desvCondEncad, width=self.dfwidth)
        self.btnMatchCase = Button(tkJanela, text="Mensagem", command=self.matchCase, width=self.dfwidth)
        self.btnImpTxtWhile = Button(tkJanela, text="Mensagem", command=self.impTxtWhile, width=self.dfwidth)
        self.btnImpTxtFor = Button(tkJanela, text="Mensagem", command=self.impTxtFor, width=self.dfwidth)
        self.btnImpTxtForeach = Button(tkJanela, text="Mensagem", command=self.impTxtForeach, width=self.dfwidth)
        self.btnImpBDConectado = Button(tkJanela, text="Mensagem", command=self.impBDConectado, width=self.dfwidth)
        self.btnImpBDDesconectado = Button(tkJanela, text="Mensagem", command=self.impBDDesconectado, width=self.dfwidth)
        self.lstbxPreferencias.grid(collumn=0,row=0)
        self.lstbxPreferencias.place(x=250,y=10)
        self.placeButtons(10,33)

    def mensagem(self):
        tkinter.messagebox.showinfo("Mensagem","Parabéns Primeiro Botão")
    def desvCond(self):
        result = tkinter.messagebox.askokcancel("Ok ou Cancelar","Responda Ok ou Cancelar")

        if result:
            tkinter.messagebox.showinfo("Resposta Ok", "Respondeu Ok")
        else:
            tkinter.messagebox.showinfo("Resposta Cancelar", "Respondeu Cancelar")

    def desvCondEncad(self):
        result = tkinter.messagebox.askyesnocancel("Yes ou No ou Cancelar", "Responda Yes ou No ou Cancelar")

        if result:
            tkinter.messagebox.showinfo("Resposta Yes", "Respondeu Yes")
        elif result is False:
            tkinter.messagebox.showinfo("Resposta No", "Respondeu No")
        else:
            tkinter.messagebox.showinfo("Resposta Cancel", "Respondeu Cancel")

    def matchCase(self):
        result = tkinter.messagebox.askyesnocancel("Yes ou No ou Cancelar", "Responda Yes ou No ou Cancelar")
        match result:
            case True:
                tkinter.messagebox.showinfo("Resposta Yes", "Respondeu Yes")
            case False:
                tkinter.messagebox.showinfo("Resposta No", "Respondeu No")
            case None:
                tkinter.messagebox.showinfo("Resposta Cancel", "Respondeu Cancel")
            case _:
                tkinter.messagebox.showinfo("Algo deu errado","Responda as opções possiveis")
    def impTxtWhile(self):
        self.lstbxPreferencias.delete(0,END)
        with open("H:\\ToscanoAulas\\preferencias.txt") as arquivo:
            strLinhaLida = arquivo.readline()

            while strLinhaLida != "" or strLinhaLida is not None:
                self.lstbxPreferencias.insert(END,strLinhaLida)
                strLinhaLida = arquivo.readline()
            arquivo.close()

    def impTxtFor(self):
        self.lstbxPreferencias.delete(0, END)
        with open("H:\\ToscanoAulas\\preferencias.txt") as arquivo:
            strLinhasLidas = arquivo.readlines()
            [self.lstbxPreferencias.insert(END,strLinhasLidas[index]) for index in range(len(strLinhasLidas))]
        arquivo.close()
    def impTxtForeach(self):
        self.lstbxPreferencias.delete(0, END)
        with open("H:\\ToscanoAulas\\preferencias.txt") as arquivo:
            strLinhasLidas = arquivo.readlines()
            [self.lstbxPreferencias.insert(END,linha) for linha in strLinhasLidas]
        arquivo.close()

    def impBDConectado(self):
        self.lstbxPreferencias.delete(0, END)


