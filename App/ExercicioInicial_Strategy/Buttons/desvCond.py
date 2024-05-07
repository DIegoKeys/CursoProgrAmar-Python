import tkinter
from tkinter import messagebox
from modelButton import ButtonAction

class DesvCond(ButtonAction):
    @staticmethod
    def acaoDeEvento():
        resultado = tkinter.messagebox.askyesno('Sim ou Não?','Gostaria de fornecer seus dados pra nossa companhia?')
        if resultado:
            tkinter.messagebox.showinfo('Resposta sim','Seus dados foram fornecidos para companhia!')
        else:
            tkinter.messagebox.showinfo('Resposta não', 'Seus dados não foram fornecidos para companhia!')