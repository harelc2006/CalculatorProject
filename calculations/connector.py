from decimal import Decimal

from MinusManage.Convert import *
from MinusManage.Trimmer import allMinusTrimmer
from calculations.calculation import calculation
from calculations.toPostfix import infixToPostfix


def calculate(exp):
    """"
    gets: expression after validation
    returns: calculates the expression using functions
    """
    exp = exp.replace(" ", "").replace("\t", "")
    exp = conversion(exp)
    exp = allMinusTrimmer(exp)
    exp = signMinusCare(exp)
    pfix = infixToPostfix(exp)
    answer = calculation(pfix)
    if answer.is_integer():
        result = int(answer)
    return f"{Decimal(answer):.1e}" if answer > 4e+20 or (4e-10 > answer > -4e-10)else answer
