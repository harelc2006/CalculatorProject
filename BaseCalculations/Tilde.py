from BaseCalculations.Opertaor import Operator


class Tilde(Operator):
    def calculate(self, num1, num2=None):
        return -1 * num1
