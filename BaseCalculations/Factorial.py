from BaseCalculations.Opertaor import Operator


class Factorial(Operator):
    @staticmethod
    def calculate(num1, num2=None):
        if num1 < 0:
            raise ValueError("Cannot factorial negative numbers")
        if not isinstance(num1, int):
            raise ValueError("Cannot factorial non integers  numbers")
        result = 1
        for i in range(2, num1):
            result *= i
        return result

    @staticmethod
    def getPriority():
        return 6
