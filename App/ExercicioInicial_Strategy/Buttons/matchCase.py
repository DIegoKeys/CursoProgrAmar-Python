import tkinter
from tkinter import messagebox
from modelButton import ButtonAction

class MatchCase(ButtonAction):
    @staticmethod
    def acaoDeEvento():
        resultado = tkinter.messagebox.askyesnocancel('Sim ou Não ou Cancelar?',
                                                      'Gostaria de fornecer seus dados pra nossa companhia?')
        match resultado:
            case True:
                tkinter.messagebox.showinfo('Resposta sim', 'Seus dados foram fornecidos para companhia!')
            case False:
                tkinter.messagebox.showinfo('Resposta não', 'Seus dados não foram fornecidos para companhia!')
            case None:
                tkinter.messagebox.showinfo('Resposta Cancelar',
                                            'Seus dados não foram fornecidos para companhia! Cancelado')
            case _:
                tkinter.messagebox.showinfo('Resposta Cancelar',
                                            'Seus dados não foram fornecidos para companhia! Cancelado')