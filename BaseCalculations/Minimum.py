from BaseCalculations.Opertaor import Operator


class Minimum(Operator):
    def calculate(self, num1, num2):
        return num1 if num1 < num2 else num2
