import tkinter
from tkinter import messagebox
from modelButton import ButtonAction

class DesvCondEncad(ButtonAction):
    @staticmethod
    def acaoDeEvento():
        resultado = tkinter.messagebox.askyesnocancel('Sim ou Não ou Cancelar?',
                                                      'Gostaria de fornecer seus dados pra nossa companhia?')
        if resultado:
            tkinter.messagebox.showinfo('Resposta sim', 'Seus dados foram fornecidos para companhia!')
        elif resultado is False:
            tkinter.messagebox.showinfo('Resposta não', 'Seus dados não foram fornecidos para companhia!')
        else:
            tkinter.messagebox.showinfo('Resposta Cancelar',
                                        'Seus dados não foram fornecidos para companhia! Cancelado')