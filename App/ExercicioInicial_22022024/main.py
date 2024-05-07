import tkinter
import tkinter.messagebox
from tkinter import *

class App():
    def __init__(self,tkJanela):
        self.lstbxPreferencias = Listbox(tkJanela,width=55,height=13)
        self.btnMensagem = Button(tkJanela,text="Mensagem",command=self.mensagem,width=30)
        self.btnDesvCond = Button(tkJanela, text="Desvio Condicional", command=self.desvCond, width=30)
        self.btnDesvCondEncad = Button(tkJanela, text="Desvio Condicional Encadeado", command=self.desvCondEncad, width=30)
        self.btnMatchCase = Button(tkJanela, text="Match Case", command=self.matchCase, width=30)
        self.btnImpTxtWhile = Button(tkJanela, text="Importar Texto While", command=self.impTxtWhile, width=30)
        self.btnImpTxtFor = Button(tkJanela, text="Importar Texto For", command=self.impTxtFor, width=30)
        self.btnImpTxtForeach = Button(tkJanela, text="Importar Texto Foreach", command=self.impTxtForeach, width=30)
        self.btnImpBDConectado = Button(tkJanela, text="Importar BD Conectado", command=self.impBDConectado, width=30)
        self.lstbxPreferencias.place(x=250,y=10)
        self.btnMensagem.place(x=10,y=10)
        self.btnDesvCond.place(x=10,y=40)
        self.btnDesvCondEncad.place(x=10,y=70)
        self.btnMatchCase.place(x=10,y=100)
        self.btnImpTxtWhile.place(x=10,y=130)
        self.btnImpTxtFor.place(x=10,y=160)
        self.btnImpTxtForeach.place(x=10,y=190)
        self.btnImpBDConectado.place(x=10,y=220)

    def mensagem(self):
        tkinter.messagebox.showinfo('Mensagem','Parabéns pelo primeiro Botão')
    def desvCond(self):
        resultado = tkinter.messagebox.askokcancel('Desvio Condicional','Gostaria de Fornecer seus dados')
        if resultado:
            tkinter.messagebox.showinfo('Resposta Ok','Obrigado por fornecer os dados')
        else:
            tkinter.messagebox.showinfo('Resposta Cancelar','Operação Cancelada')
    def desvCondEncad(self):
        resultado = tkinter.messagebox.askyesnocancel('Desvio Condicional', 'Gostaria de Fornecer seus dados')
        if resultado:
            tkinter.messagebox.showinfo('Resposta Sim', 'Obrigado por fornecer os dados')
        elif resultado is False:
            tkinter.messagebox.showinfo('Resposta Não', 'Operação não concluida')
        else:
            tkinter.messagebox.showinfo('Resposta Cancelar', 'Operação Cancelada')
    def matchCase(self):
        resultado = tkinter.messagebox.askyesnocancel('Desvio Condicional', 'Gostaria de Fornecer seus dados')

        match resultado:
            case True:
                tkinter.messagebox.showinfo('Resposta Sim', 'Obrigado por fornecer os dados')
            case False:
                tkinter.messagebox.showinfo('Resposta Não', 'Operação não concluida')
            case None:
                tkinter.messagebox.showinfo('Resposta Cancelar', 'Operação Cancelada')
            case _:
                tkinter.messagebox.showinfo('Resposta Error', 'Operação Cancelada')


    def impTxtWhile(self):
        self.lstbxPreferencias.delete(0,END)
        with open("H:\\ToscanoAulas\\preferencias.txt") as arquivo:
            linhaLida = arquivo.readline()
            while linhaLida != '':
                self.lstbxPreferencias.insert(END,linhaLida)
                linhaLida = arquivo.readline()
            arquivo.close()
    def impTxtFor(self):
        self.lstbxPreferencias.delete(0, END)
        with open("H:\\ToscanoAulas\\preferencias.txt") as arquivo:
            linhasLidas = arquivo.readlines()
            [self.lstbxPreferencias.insert(END,linhasLidas[x]) for x in range(len(linhasLidas))]
            arquivo.close()
    def impTxtForeach(self):
        self.lstbxPreferencias.delete(0, END)
        with open("H:\\ToscanoAulas\\preferencias.txt") as arquivo:
            linhasLidas = arquivo.readlines()
            [self.lstbxPreferencias.insert(END, x) for x in linhasLidas]
            arquivo.close()
    def impBDConectado(self):
        pass

tkJanela = Tk()
App(tkJanela)
tkJanela.geometry('600x250+10+10')
tkJanela.title('Janela')
tkJanela.mainloop()