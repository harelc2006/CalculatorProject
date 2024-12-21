from BaseCalculations.Average import Average
from BaseCalculations.BinaryMinus import BinaryMinus
from BaseCalculations.Collapse import Collapse
from BaseCalculations.Divide import Divide
from BaseCalculations.Factorial import Factorial
from BaseCalculations.Maximum import Maximum
from BaseCalculations.Minimum import Minimum
from BaseCalculations.Modulo import Modulo
from BaseCalculations.Multiply import Multiply
from BaseCalculations.Plus import Plus
from BaseCalculations.Power import Power
from BaseCalculations.Tilde import Tilde
from BaseCalculations.UnaryMinus import UnaryMinus

""""
a file for getting symbols instead of writing them each time and in case of adding operators 
"""


def getOperators():
    """"returns: the operators"""
    return ['+', '-', '*', '/', '^', '%', '$', '&', '@', '~', '!', '#']


def getSingleMeaningOperators():
    """"returns: single meaning operators"""
    return ['+', '*', '/', '^', '%', '$', '&', '@', '~', '!', '#']


def getAllOperators():
    """"returns: the operators after first conversions"""
    return ['+', '*', '/', '^', '%', '$', '&', '@', '~', '!', '#', 'B', 'U', 'S']


def getOperatorsAfterConversion():
    """"returns: the operators after second conversions"""
    return ['+', '*', '/', '^', '%', '$', '&', '@', '~', '!', '#', 'B', 'U']


def getMinusTypes():
    """"returns: minus types"""
    return ['B', 'U', 'S']


def getDigits():
    """"returns: list of the numbers"""
    return list("0123456789")


def getParentheses():
    """"
    returns: the Parentheses
    """
    return ['(', ')']


def getBinaryOperators():
    """"
    returns: the binary operators
    """
    bins = []
    for op in getOperatorsAfterConversion():
        if getClass(op).getOperatorLoc() == 1:
            bins.append(op)
    return bins


def getRightOperators():
    """"
    returns: the right operators
    """
    rights = []
    for op in getOperatorsAfterConversion():
        if getClass(op).getOperatorLoc() == 2:
            rights.append(op)
    return rights


def getLeftOperators():
    """"
    returns: the left operators
    """
    lefts = []
    for op in getOperatorsAfterConversion():
        if getClass(op).getOperatorLoc() == 0:
            lefts.append(op)
    return lefts + ['S']


def getClass(sym):
    """"
    gets: symbol
    returns: the class of the symbol
    """
    dictionary = {
        '+': Plus,
        'B': BinaryMinus,
        'U': UnaryMinus,
        '*': Multiply,
        '/': Divide,
        '^': Power,
        '%': Modulo,
        '$': Maximum,
        '&': Minimum,
        '@': Average,
        '~': Tilde,
        '!': Factorial,
        '#': Collapse,
    }
    return dictionary[sym]


def getLoc(op):
    """"
    gets: operator
    returns: the location of it
    """
    return getClass(op).getOperatorLoc()
