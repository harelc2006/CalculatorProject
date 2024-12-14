from BaseCalculations.Opertaor import Operator


class Power(Operator):
    @staticmethod
    def calculate(num1, num2):
        if num1 == 0 and num2 == 0:
            raise ValueError("0 cannot be to the power of 0")
        return num1 ** num2

    @staticmethod
    def getPriority():
        return 3

    @staticmethod
    def getOperatorLoc():
        return 1
