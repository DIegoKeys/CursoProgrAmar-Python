import tkinter
from tkinter import messagebox, END
from modelButton import ButtonAction
from tkinter import Listbox


class ImpTxtForeach(ButtonAction):
    @staticmethod
    def acaoDeEvento(listBox: Listbox):
        listBox.delete(0,END)
        with open("..\\..\\preferencias.txt") as arquivo:
            listPreferencias = arquivo.readlines()
            [listBox.insert(END, preferencia) for preferencia in listPreferencias]
            # for preferencia in listPreferencias:
            #     listBox.insert(END,preferencia)
            arquivo.close()


