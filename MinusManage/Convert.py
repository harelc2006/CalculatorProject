from Symbols import *


def conversion(exp):
    i = 0
    lexp = list(exp)
    i = 0
    while lexp[i] == '-':
        lexp[i] = 'U'
        i += 1
    while i < len(lexp):
        if lexp[i] == '-':
            if lexp[i - 1] in getRightOperators() + getDigits() + list(getParentheses()[1]):
                lexp[i] = 'B'
            else:
                lexp[i] = 'S'
        i += 1
    return "".join(lexp)


def signMinusCare(exp):
    i = 0
    lexp = list(exp)
    while i < len(exp):
        if lexp[i] == 'S':
            lexp[i] = 'U'
            lexp.insert(i, '(')
            i += 2
            if lexp[i] == '(':
                i += 1
                parentheses = 1
                while parentheses != 0:
                    if lexp[i] == '(':
                        parentheses += 1
                    if lexp[i] == ')':
                        parentheses -= 1
                    i += 1
            else:
                while i < len(lexp) and lexp[i] in (getDigits() + list('.')):
                    i += 1
            lexp.insert(i, ')')
        i += 1
    return "".join(lexp)
