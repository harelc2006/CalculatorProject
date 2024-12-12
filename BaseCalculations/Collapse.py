from BaseCalculations.Opertaor import Operator


class Collapse(Operator):
    def calculate(self, num1, num2=None):
        if num1 < 0:
            raise ValueError("cannot perform # on a negative number")
        number = (str(num1).replace(".", ""))
        return sum(int(digit) for digit in number)
