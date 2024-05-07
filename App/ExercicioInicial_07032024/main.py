



# drivers = pyodbc.drivers()
#
# print("Drivers: \n")
# for driver in drivers:
#     print(driver)
#
# conn_str = (
#     r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
#     r"DBQ=H:\ToscanoAulas\ToscanoOLDPROJECTS\CursoProgramação\Preferencias_1_11032021.accdb;"
#
# )
#
#
# try:
#     conn = pyodbc.connect(conn_str)
#     cursor = conn.cursor()
#
#     cursor.execute("SELECT * FROM Preferencias_1_Manual_Toscano")
#     rows = cursor.fetchall()
#
#     for row in rows:
#         print(row)
#
#     cursor.close()
#     conn.close()
# except pyodbc.Error as e:
#     print("Erro ao conectar com o banco", e)

import pyodbc
import tkinter.messagebox
from tkinter import *



class MinhaJanela:
    def __init__(self,tkJanela):
        self.lstbxPreferencias = Listbox(tkJanela, height=13, width=50)
        self.btnMensagem = Button(tkJanela, text='Mensagem',command=self.mensagem,width=30)
        self.btnDesvCond= Button(tkJanela,text='Desvio Condicional', command=self.desvCond,width=30)
        self.btnDesvCondEncad = Button(tkJanela, text='Desvio Condicional Encadeado',command=self.desvCondEncad,width=30)
        self.btnMatchCase = Button(tkJanela,text='Match Case',command=self.matchCase,width=30)
        self.btnImportarTxtWhile = Button(tkJanela,text='Importar Texto While',command=self.impTxtWhile,width=30)
        self.btnImportarTxtFor = Button(tkJanela,text='Importar Texto For',command=self.impTxtFor,width=30)
        self.btnImportarTxtForeach = Button(tkJanela, text='Impartar Texto Foreach', command=self.impTxtForeach,width=30)
        self.btnImportarBDConectado = Button(tkJanela, text='Impartar BD Conectado', command=self.impBDConectado,width=30)
        self.btnImportarBDDesconectado = Button(tkJanela, text='Impartar BD Desconectado', command=self.impBDDesconectado,width=30)
        self.lstbxPreferencias.grid(row=0,column=0)
        self.lstbxPreferencias.place(x=250,y=10)
        self.btnMensagem.place(x=10,y=10)
        self.btnDesvCond.place(x=10, y=40)
        self.btnDesvCondEncad.place(x=10, y=70)
        self.btnMatchCase.place(x=10,y=100)
        self.btnImportarTxtWhile.place(x=10,y=130)
        self.btnImportarTxtFor.place(x=10, y=160)
        self.btnImportarTxtForeach.place(x=10, y=190)
        self.btnImportarBDConectado.place(x=10, y=220)
        self.btnImportarBDDesconectado.place(x=10, y=250)
    def mensagem(self):
        tkinter.messagebox.showinfo(message='Parabéns você apertou o botão')
    def desvCond(self):
        resultado = tkinter.messagebox.askyesno('Sim ou Não?','Gostaria de fornecer seus dados pra nossa companhia?')
        if resultado:
            tkinter.messagebox.showinfo('Resposta sim','Seus dados foram fornecidos para companhia!')
        else:
            tkinter.messagebox.showinfo('Resposta não', 'Seus dados não foram fornecidos para companhia!')
    def desvCondEncad(self):
        resultado = tkinter.messagebox.askyesnocancel('Sim ou Não ou Cancelar?','Gostaria de fornecer seus dados pra nossa companhia?')
        if resultado:
            tkinter.messagebox.showinfo('Resposta sim', 'Seus dados foram fornecidos para companhia!')
        elif resultado is False:
            tkinter.messagebox.showinfo('Resposta não', 'Seus dados não foram fornecidos para companhia!')
        else:
            tkinter.messagebox.showinfo('Resposta Cancelar', 'Seus dados não foram fornecidos para companhia! Cancelado')
    def matchCase(self):
        resultado = tkinter.messagebox.askyesnocancel('Sim ou Não ou Cancelar?','Gostaria de fornecer seus dados pra nossa companhia?')
        match resultado:
            case True:
                tkinter.messagebox.showinfo('Resposta sim', 'Seus dados foram fornecidos para companhia!')
            case False:
                tkinter.messagebox.showinfo('Resposta não', 'Seus dados não foram fornecidos para companhia!')
            case None:
                tkinter.messagebox.showinfo('Resposta Cancelar', 'Seus dados não foram fornecidos para companhia! Cancelado')
            case _:
                tkinter.messagebox.showinfo('Resposta Cancelar', 'Seus dados não foram fornecidos para companhia! Cancelado')
    def impTxtWhile(self):
        self.lstbxPreferencias.delete(0, END)
        with open("H:\\ToscanoAulas\\preferencias.txt") as arquivo:
            linhaLida = arquivo.readline()
            while linhaLida != '':
                self.lstbxPreferencias.insert(END,linhaLida)
                linhaLida = arquivo.readline()
            arquivo.close()


    def impTxtFor(self):
        with open("H:\\ToscanoAulas\\preferencias.txt") as arquivo:
            self.lstbxPreferencias.delete(0,END)
            listPreferencias = arquivo.readlines()
            [self.lstbxPreferencias.insert(END,listPreferencias[index]) for index in range(len(listPreferencias))]
            arquivo.close()

    def impTxtForeach(self):
        with open("H:\\ToscanoAulas\\preferencias.txt") as arquivo:
            self.lstbxPreferencias.delete(0,END)
            listPreferencias = arquivo.readlines()
            [self.lstbxPreferencias.insert(END,index) for index in listPreferencias]
            arquivo.close()

    def impBDConectado(self):
        self.lstbxPreferencias.delete(0, END)
        conn_str = (r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
                    r"DBQ=H:\ToscanoAulas\ToscanoOLDPROJECTS\CursoProgramação\Preferencias_1_11032021.accdb;")
        objConn = pyodbc.connect(conn_str)
        objLeitorBD = objConn.cursor()

        strSql = "SELECT Descricao FROM Preferencias_1_Manual_Toscano"

        objLeitorBD.execute(strSql)
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

        strSql = "SELECT Descricao FROM Preferencias_1_Manual_Toscano"

        objLeitorBD.execute(strSql)
        records = objLeitorBD.fetchall()

        objLeitorBD.close()
        objConn.close()

        for record in records:
            self.lstbxPreferencias.insert(END,record[0])



objJanela = Tk()
objMinhaJanela = MinhaJanela(objJanela)
objJanela.title('Hello Python')
objJanela.geometry("600x350+10+10")
objJanela.mainloop()


