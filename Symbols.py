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


def getOperators():
    return ['+', '-', '*', '/', '^', '%', '$', '&', '@', '~', '!', '#']


def getSingleMeaningOperators():
    return ['+', '*', '/', '^', '%', '$', '&', '@', '~', '!', '#']


def getAllOperators():
    return ['+', '*', '/', '^', '%', '$', '&', '@', '~', '!', '#', 'B', 'U', 'S']


def getOperatorsAfterConversion():
    return ['+', '*', '/', '^', '%', '$', '&', '@', '~', '!', '#', 'B', 'U']



def getMinusTypes():
    return ['B', 'U', 'S']


def getDigits():
    return list("0123456789")


def getParentheses():
    return ['(', ')']


def getBinaryOperators():
    bins = []
    for op in getOperatorsAfterConversion():
        if getClass(op).getOperatorLoc() == 1:
            bins.append(op)
    return bins


def getRightOperators():
    rights = []
    for op in getOperatorsAfterConversion():
        if getClass(op).getOperatorLoc() == 2:
            rights.append(op)
    return rights


def getLeftOperators():
    lefts = []
    for op in getOperatorsAfterConversion():
        if getClass(op).getOperatorLoc() == 0:
            lefts.append(op)
    return lefts + ['S']


def getClass(sym):
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
    return getClass(op).getOperatorLoc()
