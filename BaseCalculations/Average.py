from BaseCalculations.Opertaor import Operator


class Average(Operator):
    """"this represents the @ - average operator"""
    @staticmethod
    def calculate(num1, num2):
        """"returns the average of num1 and num2"""
        return (num1+num2) / 2

    @staticmethod
    def getPriority():
        return 5

    @staticmethod
    def getOperatorLoc():
        return 1
