from Symbols import *


def calc(operator, n1, n2=None):
    op = getClass(operator)
    if op.getOperatorLoc() != 1:
        ans = op.calculate(n1)
    else:
        ans = op.calculate(n1, n2)
    return ans


def calculation(pfix):
    print(pfix)
    answer = []
    i = 0
    for token in pfix:
        if token not in getOperatorsAfterConversion():
            answer.append(token)
        else:
            if getLoc(token) == 1:
                n2 = float(answer.pop())
                n1 = float(answer.pop())
                answer.append(calc(token, n1, n2))
            else:
                n1 = float(answer.pop())
                answer.append(calc(token, n1))
    return answer
