from abc import ABC, abstractmethod


class Operator(ABC):

    @staticmethod
    @abstractmethod
    def getPriority():
        pass

    @staticmethod
    @abstractmethod
    def calculate(num1, num2):
        pass

    @staticmethod
    @abstractmethod
    def getOperatorLoc():
        pass
