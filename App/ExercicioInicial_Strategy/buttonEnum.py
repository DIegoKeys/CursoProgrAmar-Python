from Buttons import (
    mensagem,desvCond,desvCondEncad,matchCase,impTxtWhile,impTxtFor,impTxtForeach,
    impBDConectado,impBDDesconectado, consultarBD)
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
    btnConsultarBD = auto()


    @staticmethod
    def do_task(button, objVisual=None):

        actions = {
            ButtonEnum.btnMensagem: lambda: mensagem.Mensagem.acaoDeEvento(),
            ButtonEnum.btnDesvCond: lambda: desvCond.DesvCond.acaoDeEvento(),
            ButtonEnum.btnDesvCondEncad: lambda: desvCondEncad.DesvCondEncad.acaoDeEvento(),
            ButtonEnum.btnMatchCase: lambda: matchCase.MatchCase.acaoDeEvento(),
            ButtonEnum.btnImpTxtWhile: lambda: impTxtWhile.ImpTxtWhile.acaoDeEvento(objVisual),
            ButtonEnum.btnImpTxtFor: lambda: impTxtFor.ImpTxtFor.acaoDeEvento(objVisual),
            ButtonEnum.btnImpTxtForeach: lambda: impTxtForeach.ImpTxtForeach.acaoDeEvento(objVisual),
            ButtonEnum.btnImpBDConectado: lambda: impBDConectado.ImpBDConectado.acaoDeEvento(objVisual),
            ButtonEnum.btnImpBDDesconectado: lambda: impBDDesconectado.ImpBDDesconectado.acaoDeEvento(objVisual),
            ButtonEnum.btnConsultarBD: lambda: consultarBD.ConsultarBD.acaoDeEvento(objVisual),
        }
        action = actions.get(button)
        if action:
            action()
