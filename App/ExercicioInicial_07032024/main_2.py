import tkinter.messagebox
from tkinter import *


class MinhaJanela:
    def __init__(self, tkjanela):
        w = 30
        self.btnMensagem = Button(tkjanela, text="Mensagem", command=self.mensagem, width=w)
        self.btnDesvCond = Button(tkjanela, text="Mensagem", command=self.mensagem, width=w)
        self.btnDesvCondEncad= Button(tkjanela, text="Mensagem", command=self.mensagem, width=w)
        self.btnMatchCase = Button(tkjanela, text="Mensagem", command=self.mensagem, width=w)
        self.btnImpTxtWhile = Button(tkjanela, text="Mensagem", command=self.mensagem, width=w)
        self.btnMensagem = Button(tkjanela, text="Mensagem", command=self.mensagem, width=w)
        self.btnMensagem = Button(tkjanela, text="Mensagem", command=self.mensagem, width=w)
        self.btnMensagem = Button(tkjanela, text="Mensagem", command=self.mensagem, width=w)




objJanela = Tk()
MinhaJanela(objJanela)
objJanela.geometry('600x300')
objJanela.title('Janela Treino')
objJanela.mainloop()

