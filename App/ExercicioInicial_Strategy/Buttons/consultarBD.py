import tkinter
from tkinter import messagebox, END

import pyodbc

from modelButton import ButtonAction
from tkinter import ttk


class ConsultarBD(ButtonAction):
    @staticmethod
    def acaoDeEvento(treeView: ttk.Treeview):
        #Montagem da treeView
        cols = ["Descricao"]
        colsSize = [100]
        colsAnchor = [tkinter.W]

        #treeView.pack(side='right')

        # for i in range(len(cols)):
        #     treeView.heading(cols[i])
        #     treeView.column(cols[i], width=colsSize[i], anchor=colsAnchor[i])

        treeView.heading("Descricao", text="Descricao")
        treeView.column("Descricao", width=100, anchor=tkinter.W)

        #Deleto todos os elementos existentes anteriormente na treeView para zerá-la
        treeView.delete(*treeView.get_children())

        #Consultar BD Desconectado no Back-End
        conn_str = (r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
                    r"DBQ=..\..\Preferencias_1_11032021.accdb;")
        objConn = pyodbc.connect(conn_str)
        objLeitorBD = objConn.cursor()

        strSql = "SELECT Descricao FROM Preferencias_1_Manual_Toscano"

        objLeitorBD.execute(strSql)
        records = objLeitorBD.fetchall()

        objLeitorBD.close()
        objConn.close()

        #Alimentação da treeView no Front-End
        for linhaBD in records:
            treeView.insert('','end', values=list(linhaBD))

        #Configura aparência e apresentação do Grid
        estiloDtgdvwTrvw = ttk.Style()
        estiloDtgdvwTrvw.theme_use('clam')
        estiloDtgdvwTrvw.configure("Treeview.Heading", font="Robolt 10 bold", background="white", foreground="blue")
        estiloDtgdvwTrvw.configure("Treeview", font="Robolt 10 bold", background="white", foreground="blue")

        # barraDeRolagem = tkinter.Scrollbar(treeView.master, orient="vertical", command=treeView.yview)
        # barraDeRolagem.place(x=474, y=427, width=20, height=155)
        #
        # treeView.configure(yscrollcommand=barraDeRolagem.set)


