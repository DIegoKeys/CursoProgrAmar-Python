from Buttons import mensagem,desvCond,desvCondEncad,matchCase,impTxtWhile,impTxtFor,impTxtForeach,impBDConectado,impBDDesconectado
from enum import Enum,auto
class ButtonEnum(Enum):
    btnMensagem = auto()
    btnDesvCond = auto()
    btnDesvCondEncad = auto()
    btnMatchCase = auto()
    btnImpTxtWhile = auto()
    btnImpTxtFor = auto()
    btnImpTxtForeach = auto()
    btnImpBDConectado = auto()
    btnImpBDDesconectado = auto()


    @staticmethod
    def do_task(button, listBox=None):
        actions = {
            ButtonEnum.btnMensagem: lambda: mensagem.Mensagem.acaoDeEvento(),
            ButtonEnum.btnDesvCond: lambda: desvCond.DesvCond.acaoDeEvento(),
            ButtonEnum.btnDesvCondEncad: lambda: desvCondEncad.DesvCondEncad.acaoDeEvento(),
            ButtonEnum.btnMatchCase: lambda: matchCase.MatchCase.acaoDeEvento(),
            ButtonEnum.btnImpTxtWhile: lambda: impTxtWhile.ImpTxtWhile.acaoDeEvento(listBox),
            ButtonEnum.btnImpTxtFor: lambda: impTxtFor.ImpTxtFor.acaoDeEvento(listBox),
            ButtonEnum.btnImpTxtForeach: lambda: impTxtForeach.ImpTxtForeach.acaoDeEvento(listBox),
            ButtonEnum.btnImpBDConectado: lambda: impBDConectado.ImpBDConectado.acaoDeEvento(listBox),
            ButtonEnum.btnImpBDDesconectado: lambda: impBDDesconectado.ImpBDDesconectado.acaoDeEvento(listBox),
        }
        action = actions.get(button)
        if action:
            action()
