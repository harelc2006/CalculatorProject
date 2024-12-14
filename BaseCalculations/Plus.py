from BaseCalculations.Opertaor import Operator


class Plus(Operator):
    @staticmethod
    def calculate(num1, num2):
        return num1 + num2

    @staticmethod
    def getPriority():
        return 1

    @staticmethod
    def getOperatorLoc():
        return 1
