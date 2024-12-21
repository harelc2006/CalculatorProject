from BaseCalculations.Opertaor import Operator


class Collapse(Operator):
    """"this represents the # - collapse operator"""
    @staticmethod
    def calculate(num1, num2=None):
        """"returns all of the digits combined of the number"""
        if num1 < 0:
            raise ValueError("cannot perform # on a negative number")
        number = (str(num1).replace(".", ""))
        return sum(int(digit) for digit in number)

    @staticmethod
    def getPriority():
        return 6

    @staticmethod
    def getOperatorLoc():
        return 2
