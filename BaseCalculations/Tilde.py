from BaseCalculations.Opertaor import Operator


class Tilde(Operator):
    @staticmethod
    def calculate(num1, num2=None):
        return -1 * num1

    @staticmethod
    def getPriority():
        return 6

    @staticmethod
    def getOperatorLoc():
        return 0
