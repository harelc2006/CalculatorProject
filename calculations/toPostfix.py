from Symbols import *


def isStrongerOperator(op1, op2):
    return True if getClass(op1).getPriority() >= getClass(op2).getPriority() else False


def infixToPostfix(exp):
    i = 0
    postfix = []
    operators = []
    currentNumber = ""

    while i < len(exp):
        while i < len(exp) and (exp[i] == '.' or exp[i] in getDigits()):
            currentNumber += exp[i]
            i += 1
        if currentNumber != "":
            postfix.append(currentNumber)
            currentNumber = ""
        if i == len(exp):
            break
        if exp[i] == '(':
            newexp = ""
            i += 1
            parentheses = 1
            while parentheses != 0:
                if exp[i] == '(':
                    parentheses += 1
                if exp[i] == ')':
                    parentheses -= 1
                if parentheses != 0:
                    newexp += exp[i]
                    i += 1
            postfix += infixToPostfix(newexp)
        if exp[i] in getOperatorsAfterConversion():
            while len(operators) > 0 and isStrongerOperator(operators[-1], exp[i]):
                postfix.append(operators.pop())
            operators.append(exp[i])
        i += 1
    while len(operators) > 0:
        postfix.append(operators.pop())
    return postfix
