
from BaseCalculations.Opertaor import Operator


class Factorial(Operator):
    """"this represents the ! - factorial operator"""
    @staticmethod
    def calculate(num1, num2=None):
        """"returns the factorial of the number"""
        if num1 < 0:
            raise ValueError("Cannot factorial negative numbers")
        if not num1.is_integer():
            raise ValueError("Cannot factorial non integers  numbers")
        result = 1
        if num1 > 170:
            raise ArithmeticError("Too long to calculate")
        for i in range(2, int(num1) + 1):
            result *= i
        return result

    @staticmethod
    def getPriority():
        return 6

    @staticmethod
    def getOperatorLoc():
        return 2
