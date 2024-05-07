import tkinter
from tkinter import messagebox, END

import pyodbc

from modelButton import ButtonAction
from tkinter import Listbox


class ImpBDConectado(ButtonAction):
    @staticmethod
    def acaoDeEvento(listBox: Listbox):
        listBox.delete(0, END)
        conn_str = (r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
                    r"DBQ=..\..\Preferencias_1_11032021.accdb;")
        objConn = pyodbc.connect(conn_str)
        objLeitorBD = objConn.cursor()

        strSql = "SELECT Descricao FROM Preferencias_1_Manual_Toscano"

        objLeitorBD.execute(strSql)
        record = objLeitorBD.fetchone()

        while record != None:
            listBox.insert(END, record.Descricao)
            record = objLeitorBD.fetchone()

        objLeitorBD.close()
        objConn.close()


