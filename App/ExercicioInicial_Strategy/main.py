import inspect

import pyodbc
import tkinter.messagebox
from tkinter import *
from buttonEnum import *




class MinhaJanela:
    def __init__(self,tkJanela):
        self.lstbxPreferencias = Listbox(tkJanela, height=13, width=50)
        # self.btnMensagem = Button(tkJanela, text='Mensagem',command=self.eventoMensagem,width=30)
        # self.btnDesvCond= Button(tkJanela,text='Desvio Condicional', command=self.eventoDesvCond,width=30)
        # self.btnDesvCondEncad = Button(tkJanela, text='Desvio Condicional Encadeado',command=self.eventButton,width=30)
        # self.btnMatchCase = Button(tkJanela,text='Match Case',command=self.eventButton,width=30)
        # self.btnImportarTxtWhile = Button(tkJanela,text='Importar Texto While',command=self.eventButton,width=30)
        # self.btnImportarTxtFor = Button(tkJanela,text='Importar Texto For',command=self.eventButton,width=30)
        # self.btnImportarTxtForeach = Button(tkJanela, text='Impartar Texto Foreach', command=self.eventButton,width=30)
        # self.btnImportarBDConectado = Button(tkJanela, text='Impartar BD Conectado', command=self.eventButton,width=30)
        # self.btnImportarBDDesconectado = Button(tkJanela, text='Impartar BD Desconectado', command=self.eventButton,width=30)
        self.button_height = 1
        self.button_width = 30
        self.y_position = 10
        self.spacing = 35
        self.btnMensagem = Button(tkJanela, height=self.button_height, width=self.button_width, text="Mensagem", command=lambda btn=ButtonEnum.btnMensagem: ButtonEnum.do_task(btn))
        self.btnDesvCond = Button(tkJanela, height=self.button_height, width=self.button_width, text="Desvio Condicional", command=lambda btn=ButtonEnum.btnDesvCond: ButtonEnum.do_task(btn))
        self.btnDesvCondEncad = Button(tkJanela, height=self.button_height, width=self.button_width, text="Desvio Condicional Encadeado",
                                  command=lambda btn=ButtonEnum.btnDesvCondEncad: ButtonEnum.do_task(btn))
        self.btnMatchCase = Button(tkJanela, height=self.button_height, width=self.button_width, text="Match Case", command=lambda btn=ButtonEnum.btnMatchCase: ButtonEnum.do_task(btn))
        self.btnImpTxtWhile = Button(tkJanela, height=self.button_height, width=self.button_width, text="Importa Texto While",
                                   command=lambda btn=ButtonEnum.btnImpTxtWhile, lstbx=self.lstbxPreferencias: ButtonEnum.do_task(btn,lstbx))
        self.btnImpTxtFor = Button(tkJanela, height=self.button_height, width=self.button_width, text="Importa Texto For",
                                     command=lambda btn=ButtonEnum.btnImpTxtFor,
                                                    lstbx=self.lstbxPreferencias: ButtonEnum.do_task(btn, lstbx))
        self.btnImpTxtForeach = Button(tkJanela, height=self.button_height, width=self.button_width,
                                   text="Importa Texto Foreach",
                                   command=lambda btn=ButtonEnum.btnImpTxtForeach,
                                                  lstbx=self.lstbxPreferencias: ButtonEnum.do_task(btn, lstbx))
        self.btnImpBDConectado = Button(tkJanela, height=self.button_height, width=self.button_width,
                                       text="Importa BD Conectado",
                                       command=lambda btn=ButtonEnum.btnImpBDConectado,
                                                      lstbx=self.lstbxPreferencias: ButtonEnum.do_task(btn, lstbx))
        self.btnImpBDDesconectado = Button(tkJanela, height=self.button_height, width=self.button_width,
                                        text="Importa BD Desconectado",
                                        command=lambda btn=ButtonEnum.btnImpBDDesconectado,
                                                       lstbx=self.lstbxPreferencias: ButtonEnum.do_task(btn, lstbx))

        self.btnMensagem.place(x=10,y=self.y_position)
        self.btnDesvCond.place(x=10,y=self.y_position + self.spacing)
        self.btnDesvCondEncad.place(x=10, y=self.y_position + self.spacing*2)
        self.btnMatchCase.place(x=10,y= self.y_position + self.spacing*3)
        self.btnImpTxtWhile.place(x=10, y=self.y_position + self.spacing * 4)
        self.btnImpTxtFor.place(x=10, y=self.y_position + self.spacing * 5)
        self.btnImpTxtForeach.place(x=10, y=self.y_position + self.spacing * 6)
        self.btnImpBDConectado.place(x=10, y=self.y_position + self.spacing * 7)
        self.btnImpBDDesconectado.place(x=10, y=self.y_position + self.spacing * 8)

        # for btn in ButtonEnum:
        #     button = Button(tkJanela, text=f"Button {btn.name}", command=lambda b=btn: ButtonEnum.do_task(b))
        #     button.place(x=10, y=self.y_position, width=self.button_width, height=self.button_height)
        #     self.y_position += self.spacing
        self.lstbxPreferencias.grid(row=0,column=0)
        self.lstbxPreferencias.place(x=250,y=10)
        # self.btnMensagem.place(x=10,y=10)
        # self.btnDesvCond.place(x=10, y=40)
        # self.btnDesvCondEncad.place(x=10, y=70)
        # self.btnMatchCase.place(x=10,y=100)
        # self.btnImportarTxtWhile.place(x=10,y=130)
        # self.btnImportarTxtFor.place(x=10, y=160)
        # self.btnImportarTxtForeach.place(x=10, y=190)
        # self.btnImportarBDConectado.place(x=10, y=220)
        # self.btnImportarBDDesconectado.place(x=10, y=250)

    @staticmethod
    def preencherListBox(listPreferencias, self=None):
        [self.lstbxPreferencias.insert(END, preferencia) for preferencia in listPreferencias]

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
