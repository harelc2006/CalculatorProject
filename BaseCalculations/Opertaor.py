from abc import ABC, abstractmethod


class Operator(ABC):
    """
    an abstract method for operator that used as base class for the rest of the operators
    methods:
        getPriority() -> return operators priority
        calculate() -> get two or one numbers depends on the operator and calculates the answer
        getLoc() -> return what is the location of the operator
        all methods are static
    """
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
