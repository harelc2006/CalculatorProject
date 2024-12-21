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
    return f"{Decimal(calculation(pfix)):.1e}" if answer > 4e+20 or answer < 4e-10 else answer
