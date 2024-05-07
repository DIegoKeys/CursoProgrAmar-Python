import pyodbc
import tkinter.messagebox

from tkinter import *


class MinhaJanela:
    def __init__(self,janela):
        self.defaultWidth = 30
        self.lstbxPreferencias = Listbox(janela,width=50,height=18)
        self.btnMensagem = Button(janela,text="Mensagem",command=self.mensagem, width=self.defaultWidth)
        self.btnDesvCond = Button(janela, text="Desvio Condicinal", command=self.desvCond, width=self.defaultWidth)
        self.btnDesvCondEncad = Button(janela, text="Desvio Condicional Encadeado", command=self.desvCondEncad, width=self.defaultWidth)
        self.btnMatchCase = Button(janela, text="Match Case", command=self.matchCase, width=self.defaultWidth)
        self.btnImpTxtWhile = Button(janela, text="Importar Texto While", command=self.impTxtWhile, width=self.defaultWidth)
        self.btnImpTxtFor = Button(janela, text="Importar Texto For", command=self.impTxtFor, width=self.defaultWidth)
        self.btnImpTxtForeach = Button(janela, text="Importar Texto Foreach", command=self.impTxtFoeach, width=self.defaultWidth)
        self.btnImpBDConectado = Button(janela, text="Importar BD Conectado", command=self.impBDConectado, width=self.defaultWidth)
        self.btnImpBDDesconectado = Button(janela, text="Importar BD Desconectado", command=self.impBDDesconectado, width=self.defaultWidth)
        self.lstbxPreferencias.grid(column=0,row=0)
        self.lstbxPreferencias.place(x=250,y=10)
        self.placeButtons(janela,10,33)

    def mensagem(self):
        tkinter.messagebox.showinfo("Mensagem","Parabéns mensagem!!")
    def desvCond(self):
        resultado = tkinter.messagebox.askokcancel("Escolher Ok ou Cancelar","Escolha entre Ok ou Cancelar")

        if resultado:
            tkinter.messagebox.showinfo("Resposta Ok","Respondeu Ok")
        else:
            tkinter.messagebox.showinfo("Respondeu Cancelar","Resposta Cancelar")

    def desvCondEncad(self):
        resultado = tkinter.messagebox.askyesnocancel("Escolher Sim ou Não ou Cancelar", "Escolha entre Sim ou Não ou Cancelar")

        if resultado:
            tkinter.messagebox.showinfo("Resposta Sim", "Respondeu Sim")
        elif resultado is False:
            tkinter.messagebox.showinfo("Respondeu Não", "Resposta Não")
        else:
            tkinter.messagebox.showinfo("Respondeu Cancelar", "Resposta Cancelar")
    def matchCase(self):
        resultado = tkinter.messagebox.askyesnocancel("Escolher Sim ou Não ou Cancelar",
                                                      "Escolha entre Sim ou Não ou Cancelar")
        match resultado:
            case True:
                tkinter.messagebox.showinfo("Resposta Sim", "Respondeu Sim")
            case False:
                tkinter.messagebox.showinfo("Respondeu Não", "Resposta Não")
            case None:
                tkinter.messagebox.showinfo("Respondeu Cancelar", "Resposta Cancelar")
            case _:
                tkinter.messagebox.showinfo("Erro na Resposta", "Erro na Resposta")

    def impTxtWhile(self):
        self.lstbxPreferencias.delete(0,END)
        with open("H:\\ToscanoAulas\\preferencias.txt") as arquivo:
            strLinhaLida = arquivo.readline()

            while strLinhaLida != "":
                self.lstbxPreferencias.insert(END,strLinhaLida)
                strLinhaLida = arquivo.readline()
            arquivo.close()
    def impTxtFor(self):
        self.lstbxPreferencias.delete(0, END)
        with open("H:\\ToscanoAulas\\preferencias.txt") as arquivo:
            listPreferencias = arquivo.readlines()
            [self.lstbxPreferencias.insert(END,listPreferencias[index]) for index in range(len(listPreferencias))]
            arquivo.close()
    def impTxtFoeach(self):
        self.lstbxPreferencias.delete(0, END)
        with open("H:\\ToscanoAulas\\preferencias.txt") as arquivo:
            listPreferencias = arquivo.readlines()
            [self.lstbxPreferencias.insert(END, index) for index in listPreferencias]
            arquivo.close()
    def impBDConectado(self):
        self.lstbxPreferencias.delete(0, END)
        conn_str = (r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
                    r"DBQ=H:\ToscanoAulas\ToscanoOLDPROJECTS\CursoProgramação\Preferencias_1_11032021.accdb;")
        objConn = pyodbc.connect(conn_str)
        objLeitorBD = objConn.cursor()
        strsql =  "SELECT Descricao FROM Preferencias_1_Manual_Toscano"

        objLeitorBD.execute(strsql)
        record = objLeitorBD.fetchone()
        while record != None:
            self.lstbxPreferencias.insert(END,record.Descricao)
            record = objLeitorBD.fetchone()
        objLeitorBD.close()
        objConn.close()
    def impBDDesconectado(self):
        self.lstbxPreferencias.delete(0, END)
        conn_str = (r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
                    r"DBQ=H:\ToscanoAulas\ToscanoOLDPROJECTS\CursoProgramação\Preferencias_1_11032021.accdb;")
        objConn = pyodbc.connect(conn_str)
        objLeitorBD = objConn.cursor()
        strsql = "SELECT Descricao FROM Preferencias_1_Manual_Toscano"

        objLeitorBD.execute(strsql)
        records = objLeitorBD.fetchall()
        objLeitorBD.close()
        objConn.close()
        for record in records:
            self.lstbxPreferencias.insert(END, record.Descricao)

    def placeButtons(self, janela: Tk, initial_position: int, space_between: int):
        new_y_position = initial_position
        for button in janela.children.items():
            if isinstance(button[1],Button):
                button[1].place(x=initial_position, y=new_y_position)
                new_y_position += space_between


objJanela = Tk()
MinhaJanela(objJanela)
objJanela.geometry("570x330")
objJanela.title("Minha Janela")
objJanela.mainloop()