import pyodbc
import tkinter.messagebox
from tkinter import *

class MyWindow:
    def __init__(self,tkjanela):
        self.defaultWidth = 30
        self.lstbxPreferencias = Listbox(tkjanela, height=18,width=50)
        self.btnMensagem = Button(tkjanela, text="Mensagem", command=self.mensagem, width=self.defaultWidth)
        self.btnDesvCond = Button(tkjanela, text="Desvio Condicional", command=self.desvCond, width=self.defaultWidth)
        self.btnDesvCondEncad = Button(tkjanela, text="Desvio Concidional Encadeado", command=self.desvCondEncad, width=self.defaultWidth)
        self.btnMatchCase = Button(tkjanela, text="Match Case", command=self.matchCase, width=self.defaultWidth)
        self.btnImpTxtWhile = Button(tkjanela, text="Importar Texto While", command=self.impTxtWhile, width=self.defaultWidth)
        self.btnImpTxtFor = Button(tkjanela, text="Importar Texto For", command=self.impTxtFor, width=self.defaultWidth)
        self.btnImpTxtForeach = Button(tkjanela, text="Importar Texot Foreach", command=self.impTxtForeach, width=self.defaultWidth)
        self.btnImpBDConectado = Button(tkjanela, text="Importar BD Conectado", command=self.impBDConectado, width=self.defaultWidth)
        self.btnImpBDDesconectado = Button(tkjanela, text="Importar BD Desconectado", command=self.impBDDesconectado, width=self.defaultWidth)
        self.lstbxPreferencias.grid(row=0,column=0)
        self.lstbxPreferencias.place(x=250,y=10)
        self.placeButtons(tkjanela,10,33)

    def mensagem(self):
        tkinter.messagebox.showinfo(message="Parabéns pelo botão")

    def desvCond(self):
        resultado = tkinter.messagebox.askokcancel("Ok ou Cancel","Seus dados foram fornecidos a empresa")
        if resultado:
            tkinter.messagebox.showinfo("Resposta Ok","Obrigado por aceitar")
        else:
            tkinter.messagebox.showinfo("Resposta Cancelar","Infelizmente seus dados já foram fornecidos. :)")

    def desvCondEncad(self):
        resultado = tkinter.messagebox.askyesnocancel("Sim, Não ou Cancel","Gostaria de fornecer o endereço da sua casa?")
        if resultado:
            tkinter.messagebox.showinfo("Resposta Sim","Obrigado por aceitar")
        elif resultado is False:
            tkinter.messagebox.showinfo("Resposta Não","Infelizmente seus dados já foram fornecidos. :)")
        else:
            tkinter.messagebox.showinfo("Resposta Cancelar","Infelizmente seus dados já foram fornecidos. :)")

    def matchCase(self):
        resultado = tkinter.messagebox.askyesnocancel("Sim, Não ou Cancel","Gostaria de fornecer o endereço da sua casa?")
        match resultado:
            case True:
                tkinter.messagebox.showinfo("Resposta Sim","Obrigado por aceitar")
            case False:
                tkinter.messagebox.showinfo("Resposta Não","Infelizmente seus dados já foram fornecidos. :)")
            case None:
                tkinter.messagebox.showinfo("Resposta Cancelar","Respondeu Cancelar")
            case _:
                tkinter.messagebox.showinfo("Error","Erro inesperado")
    def impTxtWhile(self):
        self.lstbxPreferencias.delete(0,END)
        with open("H:\\ToscanoAulas\\preferencias.txt") as arquivo:
            linhaLida = arquivo.readline()
            while linhaLida != '':
                self.lstbxPreferencias.insert(END,linhaLida)
                linhaLida = arquivo.readline()
            arquivo.close()
    def impTxtFor(self):
        self.lstbxPreferencias.delete(0,END)
        with open("H:\\ToscanoAulas\\preferencias.txt") as arquivo:
            listPreferencias = arquivo.readlines()
            [self.lstbxPreferencias.insert(END,listPreferencias[index]) for index in range(len(listPreferencias))]
            arquivo.close()
    def impTxtForeach(self):
        self.lstbxPreferencias.delete(0, END)
        with open("H:\\ToscanoAulas\\preferencias.txt") as arquivo:
            listPreferencias = arquivo.readlines()
            [self.lstbxPreferencias.insert(END, linha) for linha in listPreferencias]
            arquivo.close()
    def impBDConectado(self):
        self.lstbxPreferencias.delete(0,END)
        conn_str = (r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
                    r"DBQ=H:\ToscanoAulas\ToscanoOLDPROJECTS\CursoProgramação\Preferencias_1_11032021.accdb;")
        objConn = pyodbc.connect(conn_str)
        objLeitorBD =objConn.cursor()

        strsql = "SELECT Descricao FROM Preferencias_1_Manual_Toscano"

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

    def placeButtons(self,tkjanela:Tk,initial_value:int, space_between_value:int):
        for button in tkjanela.children.items():
            if isinstance(button[1],Button):
                button[1].place(x=10,y=initial_value)
                initial_value += space_between_value
objWindow = Tk()
MyWindow(objWindow)
objWindow.title("Janelinha")
objWindow.geometry("570x330")
objWindow.mainloop()