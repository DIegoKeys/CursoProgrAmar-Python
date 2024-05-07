from abc import ABC, abstractmethod

class ButtonAction(ABC):

    @staticmethod
    @abstractmethod
    def acaoDeEvento(objVisual=None):
        pass