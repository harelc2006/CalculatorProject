from BaseCalculations.Opertaor import Operator


class Average(Operator):
    @staticmethod
    def calculate(num1, num2):
        return (num1+num2) / 2

    @staticmethod
    def getPriority():
        return 5

    @staticmethod
    def getOperatorLoc():
        return 1
