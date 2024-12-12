from BaseCalculations.Opertaor import Operator


class Minimum(Operator):
    @staticmethod
    def calculate(num1, num2):
        return num1 if num1 < num2 else num2

    @staticmethod
    def getPriority():
        return 5
