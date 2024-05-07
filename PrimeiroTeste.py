import tkinter.messagebox
from tkinter import *

class MinhaJanela:
    def __init__(self, tkJanela):
        self.listPreferencias = list(open("H:\ToscanoAulas\preferencias.txt"))
        self.btnMensagem = Button(tkJanela, text='Mensagem', command=self.mensagem)
        self.btnDesvCond = Button(tkJanela, text='DesvCond',command=self.desvCond)
        self.btnDesvCondEncad = Button(tkJanela, text='DesvCondEncad',command=self.desvCondEncad)
        self.btnMatchCase = Button(tkJanela,text='MatchCase',command=self.matchCase)
        self.btnImpTxtForeach = Button(tkJanela, text='ImpTxtForeach', command=self.impTxtForeach)
        self.btnImpTxtFor = Button(tkJanela, text='ImpTxtFor', command=self.impTxtFor)
        self.brnImpTxtWhile = Button(tkJanela,text='ImpTxtWhile',command=self.impTxtWhile)
        self.lstbxPreferencias = Listbox(tkJanela,height=15,width=30)
        self.lstbxPreferencias.grid(row=0, column=0)
        self.lstbxPreferencias.place(x=120,y=10)
        self.btnMensagem.place(x=10, y=10)
        self.btnDesvCond.place(x=10, y=40)
        self.btnDesvCondEncad.place(x=10, y=70)
        self.btnMatchCase.place(x=10, y=100)
        self.btnImpTxtForeach.place(x=10, y=130)
        self.btnImpTxtFor.place(x=10,y=160)
        self.brnImpTxtWhile.place(x=10,y=190)




    def mensagem(self):
        tkinter.messagebox.showinfo(message='Parebéns você apertou o botão')


    def desvCond(self):
        resultado = tkinter.messagebox.askyesno(message='Gostaria de fornecer seus dados para nossa companhia?')
        if resultado:
            tkinter.messagebox.showinfo(message='Seus dados foram fornecidos para companhia!')
        else:
            tkinter.messagebox.showinfo(message='Seus dados não foram fornecidos para companhia!')
    def desvCondEncad(self):
        resultado = tkinter.messagebox.askyesnocancel(message='Gostaria de fornecer seus dados para nossa companhia?')
        if resultado:
            tkinter.messagebox.showinfo(message='Seus dados foram fornecidos para companhia!')
        elif not resultado:
            tkinter.messagebox.showinfo(message='Seus dados não foram fornecidos para companhia!')
        else:
            tkinter.messagebox.showinfo(message='Processo Cancelado!')


    def matchCase(self):
        resultado = tkinter.messagebox.askyesnocancel(message='Gostaria de fornecer seus dados para nossa companhia?')
        match resultado:
            case True:
                tkinter.messagebox.showinfo(message='Seus dados foram fornecidos para companhia!')
            case False:
                tkinter.messagebox.showinfo(message='Seus dados não foram fornecidos para companhia!')
            case None:
                tkinter.messagebox.showinfo(message='Processo Cancelado!')
            case _:
                tkinter.messagebox.showinfo(message='Processo Cancelado!')
    def impTxtForeach(self):
        self.lstbxPreferencias.delete(0,END)
        [self.lstbxPreferencias.insert(END,x) for x in self.listPreferencias]
    def impTxtFor(self):
        self.lstbxPreferencias.delete(0,END)
        [self.lstbxPreferencias.insert(END,self.listPreferencias[index]) for index in range(len(self.listPreferencias))]


    def impTxtWhile(self):
        self.lstbxPreferencias.delete(0, END)
        listIndex = 0
        while True:
            self.lstbxPreferencias.insert(END,self.listPreferencias[listIndex])
            if listIndex + 1 == len(self.listPreferencias):
                break
            listIndex += 1



objJanela = Tk()
objMinhaJanela = MinhaJanela(objJanela)
objJanela.title('Hello Python')
objJanela.geometry("400x300+10+10")
objJanela.mainloop()