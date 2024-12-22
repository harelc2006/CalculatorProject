from Symbols import *


def calc(operator, n1, n2=None):
    """"
    gets: operator and two/one number depends on the operator
    returns: the the answer to the basic calculation
    """
    op = getClass(operator)
    if op.getOperatorLoc() != 1:
        ans = op.calculate(n1)
    else:
        ans = op.calculate(n1, n2)
    if ans > 1.5e+308:
        raise ArithmeticError("Too long to calculate")
    return float(ans)


def calculation(pfix):
    """"
    gets: a postfix equation
    returns: calculates the postfix equation
    """
    answer = []
    i = 0
    for token in pfix:
        if token not in getOperatorsAfterConversion():
            token = token.replace('S', '-')
            answer.append(token)
        else:
            if getLoc(token) == 1:
                n2 = float(answer.pop())
                n1 = float(answer.pop())
                answer.append(calc(token, n1, n2))
            else:
                n1 = float(answer.pop())
                answer.append(calc(token, n1))
    return answer[0]


