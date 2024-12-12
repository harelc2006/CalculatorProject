from BaseCalculations.Opertaor import Operator


class Multiply(Operator):
    @staticmethod
    def calculate(num1, num2):
        return num1 * num2

    @staticmethod
    def getPriority():
        return 2
