from BaseCalculations.Opertaor import Operator


class BinaryMinus(Operator):
    """"this represents the - - binary minus"""
    @staticmethod
    def calculate(num1, num2):
        """"returns num1 minus num2"""
        return num1 - num2

    @staticmethod
    def getPriority():
        return 1

    @staticmethod
    def getOperatorLoc():
        return 1