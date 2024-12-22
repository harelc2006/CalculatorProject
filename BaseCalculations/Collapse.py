from BaseCalculations.Opertaor import Operator


class Collapse(Operator):
    """"this represents the # - collapse operator"""
    @staticmethod
    def calculate(num1, num2=None):
        """"returns all of the digits combined of the number"""
        if num1 < 0:
            raise ValueError("cannot perform # on a negative number")
        number = (str(num1).replace(".", ""))
        result = sum(int(digit) for digit in number)
        if result > 1.5e+308:
            raise ArithmeticError("Too long to calculate")
        return float(result)

    @staticmethod
    def getPriority():
        return 6

    @staticmethod
    def getOperatorLoc():
        return 2
