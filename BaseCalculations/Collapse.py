from BaseCalculations.Opertaor import Operator


class Collapse(Operator):
    def calculate(self, num1, num2=None):
        if num1 < 0:
            raise ValueError("cannot perform # on a negative number")
        number = str(num1).replace(".", "")
        while len(number) > 1:
            numbers = str(sum(int(digit) for digit in numbers))
        return int(number)
