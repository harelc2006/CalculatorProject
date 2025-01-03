from BaseCalculations.Opertaor import Operator


class Modulo(Operator):
    """"this represents the % - modulo operator"""
    @staticmethod
    def calculate(num1, num2):
        return num1 % num2

    @staticmethod
    def getPriority():
        return 4

    @staticmethod
    def getOperatorLoc():
        return 1
