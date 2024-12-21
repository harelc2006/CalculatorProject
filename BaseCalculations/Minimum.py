from BaseCalculations.Opertaor import Operator


class Minimum(Operator):
    """"this represents the & - minimum operator"""
    @staticmethod
    def calculate(num1, num2):
        """"return the lower number out num1 and num2"""
        return num1 if num1 < num2 else num2

    @staticmethod
    def getPriority():
        return 5

    @staticmethod
    def getOperatorLoc():
        return 1
