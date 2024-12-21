from BaseCalculations.Opertaor import Operator


class Divide(Operator):
    """"this represents the / - divide operator"""
    @staticmethod
    def calculate(num1, num2):
        """"returns num1 divided by num2"""
        if num2 == 0:
            raise ZeroDivisionError("you are trying to divide by zero")
        return num1 / num2

    @staticmethod
    def getPriority():
        return 2

    @staticmethod
    def getOperatorLoc():
        return 1
