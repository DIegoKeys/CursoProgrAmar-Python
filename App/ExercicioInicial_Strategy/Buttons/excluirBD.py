import tkinter
from tkinter import messagebox, END

import pyodbc

from modelButton import ButtonAction
from tkinter import ttk


class ExcluirBD(ButtonAction):


    @staticmethod
    def refresh_treeview(treeView):
        treeView.delete(*treeView.get_children())
        # Similar ao código anterior para popular a Treeview
        conn_str = (r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
                    r"DBQ=..\..\Preferencias_1_11032021.accdb;")
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Busca atualizada de registros
        strSql = "SELECT ID,Descricao FROM Preferencias_3"
        cursor.execute(strSql)
        records = cursor.fetchall()
        cursor.close()
        conn.close()

        # Limpa a Treeview antes de recarregar


        for linhaBD in records:
            treeView.insert('', 'end', values=list(linhaBD))



    @staticmethod
    def acaoDeEvento(treeView: ttk.Treeview):
        treeView.heading("ID", text="ID")
        treeView.column("ID", width=100, anchor=tkinter.W)
        treeView.heading("Descricao", text="Descricao")
        treeView.column("Descricao", width=100, anchor=tkinter.W)
        selected_item = treeView.focus()
        if selected_item:
            item=treeView.item(selected_item)
            id_selected = item['values'][0]
            # Conectar ao banco de dados
            conn_str = (r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
                        r"DBQ=..\..\Preferencias_1_11032021.accdb;")
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()

            # Comando SQL para deletar o registro selecionado
            strSql = "DELETE FROM Preferencias_3 WHERE ID = ?"
            cursor.execute(strSql, id_selected)
            conn.commit()  # Confirma a transação

            cursor.close()
            conn.close()

        ExcluirBD.refresh_treeview(treeView)