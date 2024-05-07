import tkinter
from tkinter import messagebox, END
from modelButton import ButtonAction
from tkinter import Listbox


class ImpTxtFor(ButtonAction):
    @staticmethod
    def acaoDeEvento(listBox: Listbox):
        listBox.delete(0,END)
        with open("..\\..\\preferencias.txt") as arquivo:
            listPreferencias = arquivo.readlines()
            [listBox.insert(END, listPreferencias[index]) for index in range(len(listPreferencias))]
            # for index in range(len(listPreferencias)):
            #     listBox.insert(END,listPreferencias[index])
            arquivo.close()


