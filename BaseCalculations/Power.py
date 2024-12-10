from BaseCalculations.Opertaor import Operator


class Power(Operator):
    def calculate(self, num1, num2):
        if num1 == 0 and num2 == 0:
            raise ValueError("0 cannot be to the power of 0")
        return num1 ** num2
