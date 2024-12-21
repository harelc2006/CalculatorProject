from BaseCalculations.Opertaor import Operator


class Multiply(Operator):
    """"this represents the * - multiply operator"""
    @staticmethod
    def calculate(num1, num2):
        """"return num1 * num2"""
        return num1 * num2

    @staticmethod
    def getPriority():
        return 2

    @staticmethod
    def getOperatorLoc():
        return 1
