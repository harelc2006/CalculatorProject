from BaseCalculations.Opertaor import Operator


class UnaryMinus(Operator):
    """
    this class represents - - unary minus operator
    """
    @staticmethod
    def calculate(num1, num2=None):
        """"negate number"""
        return -1 * num1

    @staticmethod
    def getPriority():
        return 2.5

    @staticmethod
    def getOperatorLoc():
        return 0
