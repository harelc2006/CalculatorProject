from BaseCalculations.Opertaor import Operator


class UnaryMinus(Operator):
    def calculate(self, num1, num2=None):
        return -1 * num1
