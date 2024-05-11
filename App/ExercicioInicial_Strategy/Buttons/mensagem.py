import sys
import tkinter.messagebox

sys.path.append('..\\..\\..\\CursoProgrAmar-Python\\App\\ExercicioInicial_Strategy\\Buttons')

import modelButton


class Mensagem(modelButton.ButtonAction):
    @staticmethod
    def acaoDeEvento():
        tkinter.messagebox.showinfo("Mensagem","Parabens primiero texto")
