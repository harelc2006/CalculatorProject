from BaseCalculations.Opertaor import Operator
import math


class Power(Operator):
    @staticmethod
    def calculate(num1, num2):
        if num1 == 0 and num2 == 0:
            raise ValueError("0 cannot be to the power of 0")
        try:
            return math.pow(num1, num2)
        except OverflowError:
            raise OverflowError("Too long to calculate")
        except ValueError:
            raise ValueError("cannot raise negative numbers to the power of non integers")

    @staticmethod
    def getPriority():
        return 3

    @staticmethod
    def getOperatorLoc():
        return 1
