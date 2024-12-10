from BaseCalculations.Opertaor import Operator


class Divide(Operator):
    def calculate(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("you are trying to divide by zero")
        return num1 / num2
