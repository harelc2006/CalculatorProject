from BaseCalculations.Opertaor import Operator


class Plus(Operator):
    """"this represents the + - plus operator"""
    @staticmethod
    def calculate(num1, num2):
        """"returns num1 + num2"""
        return num1 + num2

    @staticmethod
    def getPriority():
        return 1

    @staticmethod
    def getOperatorLoc():
        return 1
