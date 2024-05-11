import tkinter
from tkinter import messagebox, END, simpledialog

import pyodbc

from modelButton import ButtonAction
from tkinter import ttk


class IncluirBD(ButtonAction):
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
        try:

            resposta = simpledialog.askstring("Incluir", f"Incluir uma descrição:", )
            if resposta is not None and resposta != "":
                conn_str = (r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
                            r"DBQ=..\..\Preferencias_1_11032021.accdb;")
                conn = pyodbc.connect(conn_str)
                cursor = conn.cursor()
                # Comando SQL para deletar o registro selecionado
                strSql = "INSERT INTO Preferencias_3 (Descricao) VALUES (?)"
                cursor.execute(strSql, resposta)
                conn.commit()  # Confirma a transação
                cursor.close()
                conn.close()
                messagebox.showinfo("Sucesso", "A descrição foi incluida com sucesso!!!")
            else:
                messagebox.showinfo("Vazio", "A descrição fornecida está fazia digite alguma descrição valida!!")
            # Conectar ao banco de dados


            IncluirBD.refresh_treeview(treeView)
        except Exception as e:
            messagebox.showinfo("Erro ao Atualizar a descrição!" + str(e))
