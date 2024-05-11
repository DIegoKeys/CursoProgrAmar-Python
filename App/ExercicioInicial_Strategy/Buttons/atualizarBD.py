import tkinter
from tkinter import messagebox, END, simpledialog

import pyodbc

from modelButton import ButtonAction
from tkinter import ttk


class AtualizarBD(ButtonAction):


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
            selected_item = treeView.focus()
            if selected_item:
                item=treeView.item(selected_item)
                id_selected = item['values'][0]
                descricao_selected = item['values'][1]


                resposta = simpledialog.askstring("Atualizar",f"Atualizar a descrição {descricao_selected} para:",)
                if resposta is not None and resposta != "":
                    conn_str = (r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
                                r"DBQ=..\..\Preferencias_1_11032021.accdb;")
                    conn = pyodbc.connect(conn_str)
                    cursor = conn.cursor()

                    # Comando SQL para deletar o registro selecionado
                    strSql = "UPDATE Preferencias_3 SET Descricao = ? WHERE ID = ?"
                    cursor.execute(strSql, (resposta, id_selected))
                    conn.commit()  # Confirma a transação

                    cursor.close()
                    conn.close()
                    messagebox.showinfo("Sucesso", "A descrição foi atualizada com sucesso!!!")
                else:
                    messagebox.showinfo("Vazio", "A descrição fornecida está fazia digite alguma descrição valida!!")

                # Conectar ao banco de dados



            AtualizarBD.refresh_treeview(treeView)
        except Exception as e:
            messagebox.showinfo("Erro ao Atualizar a descrição!" + str(e))
