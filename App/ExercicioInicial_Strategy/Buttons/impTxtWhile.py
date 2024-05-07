import tkinter
from tkinter import messagebox, END
from modelButton import ButtonAction
from tkinter import Listbox
class ImpTxtWhile(ButtonAction):
    @staticmethod
    def acaoDeEvento(listBox: Listbox):
        listBox.delete(0, END)
        with open("..\\..\\preferencias.txt") as arquivo:
            linhaLida = arquivo.readline()
            while linhaLida != '':
                listBox.insert(END,linhaLida)
                linhaLida = arquivo.readline()
            arquivo.close()

