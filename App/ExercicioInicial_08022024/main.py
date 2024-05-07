import tkinter.messagebox
from tkinter import *

class App:
    def __init__(self,tkJanela):
        self.lstbxPreferencias = Listbox(tkJanela,height=13,width=50)
        self.btnMensagem = Button(tkJanela,text='Mensagem',command=self.mensagem, width=30)
        self.btnDesvCond = Button(tkJanela,text='Desvio Condicional',command=self.desvCond,width=30)
        self.btnDesvCondEncad = Button(tkJanela, text='Desvio Condicional Encadeado', command=self.desvCondEncad, width=30)
        self.btnMatchCase = Button(tkJanela, text='Match Case', command=self.matchCase, width=30)
        self.btnImportarTxtWhile = Button(tkJanela, text='Importar Texto While', command=self.impTxtWhile, width=30)
        self.btnImportarTxtFor = Button(tkJanela, text='Importar Texto For', command=self.impTxtFor, width=30)
        self.btnImportarTxtForeach = Button(tkJanela, text='Importar Texto Foreach', command=self.impTxtForeach, width=30)
        self.lstbxPreferencias.grid(row=0,column=0)
        self.lstbxPreferencias.place(x=250,y=10)
        self.btnMensagem.place(x=10,y=10)
        self.btnDesvCond.place(x=10,y=40)
        self.btnDesvCondEncad.place(x=10,y=70)
        self.btnMatchCase.place(x=10,y=100)
        self.btnImportarTxtWhile.place(x=10,y=130)
        self.btnImportarTxtFor.place(x=10,y=160)
        self.btnImportarTxtForeach.place(x=10,y=190)
    def mensagem(self):
        tkinter.messagebox.showinfo(message='Parabéns você apertou o botão')
    def desvCond(self):
        resultado = tkinter.messagebox.askyesno('Sim ou Não?','Gostaria de fornecer seus dados?')
        if resultado:
            tkinter.messagebox.showinfo('Resposta Sim','Obrigado por fornecer suas informações')
        else:
            tkinter.messagebox.showinfo('Resposta Não','Infelizmente não foi possivel obter seus dados')

    def desvCondEncad(self):
        resultado = tkinter.messagebox.askyesnocancel('Sim ou Não ou Cancelar?','Gostaria de fornecer sus dados?')
        if resultado:
            tkinter.messagebox.showinfo('Resposta Sim','Obrigado por fornecer suas informações')
        elif resultado is False:
            tkinter.messagebox.showinfo('Resposta Não', 'Infelizmente não foi possivel obter seus dados')
        else:
            tkinter.messagebox.showinfo('Resposta Cancelar', 'Processo Cancelado')

    def matchCase(self):
        resultado = tkinter.messagebox.askyesnocancel('Sim ou Não ou Cancelar?','Gostaria de fornecer sus dados?')
        match resultado:
            case True:
                tkinter.messagebox.showinfo('Resposta Sim', 'Obrigado por fornecer suas informações')
            case False:
                tkinter.messagebox.showinfo('Resposta Sim', 'Obrigado por fornecer suas informações')
            case None:
                tkinter.messagebox.showinfo('Resposta Cancelar', 'Processo Cancelado')
            case _:
                tkinter.messagebox.showinfo('Resposta Error', 'Processo Cancelado !!Error!!')
    def impTxtWhile(self):
        self.lstbxPreferencias.delete(0,END)
        with open('H:\\ToscanoAulas\\preferencias.txt') as arquivo:
            linhasLida = arquivo.readline()
            while linhasLida != '':
                self.lstbxPreferencias.insert(END,linhasLida)
                linhasLida = arquivo.readline()
            arquivo.close()
    def impTxtFor(self):
        self.lstbxPreferencias.delete(0, END)
        with open('H:\\ToscanoAulas\\preferencias.txt') as arquivo:
            list = arquivo.readlines()
            [self.lstbxPreferencias.insert(END,list[x]) for x in range(0,len(list))]

        arquivo.close()
    def impTxtForeach(self):
        self.lstbxPreferencias.delete(0, END)
        with open('H:\\ToscanoAulas\\preferencias.txt') as arquivo:
            list = arquivo.readlines()
            [self.lstbxPreferencias.insert(END,x) for x in list]
        arquivo.close()


objJanela = Tk()
App(objJanela)
objJanela.title('App Python')
objJanela.geometry('600x250+10+10')
objJanela.mainloop()
