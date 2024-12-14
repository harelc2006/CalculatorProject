from BaseCalculations.Opertaor import Operator


class Maximum(Operator):
    @staticmethod
    def calculate(num1, num2):
        return num1 if num1 > num2 else num2

    @staticmethod
    def getPriority():
        return 5

    @staticmethod
    def getOperatorLoc():
        return 1
