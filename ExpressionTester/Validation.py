from Symbols import *
from Trim.Trimmer import minusTrimmer


def validateExpression():
    return


def validSymbols(exp):
    symbols = getOperators() + getDigits() + getParentheses()
    errorMessage = ""
    for char in exp:
        if not char in symbols:
            errorMessage += "unknown symbol " + char + "\n"
    return errorMessage


def emptyExpression(exp):
    errorMessage = ""
    if len(exp) > 0:
        if len(exp) == exp.count(' ') + exp.count('\t'):
            errorMessage += "white space expression"
    else:
        errorMessage += "empty expression"
    print(errorMessage)


def validSequence(exp):
    last = exp[0]
    count = 0
    dup = []
    for char in exp[1:]:
        if char == last:
            count += 1
        else:
            if count > 0:
                dup.append(last)
            last = char
            count = 0
    if count > 0:
        dup.append(last)
    errorMessage = ""
    symbols = getDigits() + getParentheses() + ['-']
    for sym in dup:
        if sym not in symbols:
            errorMessage += "cannot put " + sym + " consecutively\n"
    return errorMessage


def ValidTildeUse(exp):
    errorMessage = ""
    if exp.count("~") > 0:
        while exp.count("~") > 0:
            trimmed = minusTrimmer(exp)
            index = trimmed.index("~")
            acceptable = getDigits() + ['(']
            b1 = index + 2 < len(trimmed) and (trimmed[index + 1] == '-' and trimmed[index + 2] in acceptable)
            b2 = index + 1 < len(trimmed) and trimmed[index + 1] in acceptable
            b3 = index + 1 != len(trimmed)
            i = exp.index("~")
            if not (b3 and (b1 or b2)):
                while i < len(exp) and not exp[i] in acceptable:
                    i += 1
                errorMessage += exp[exp.index("~"):i + 1] + " is not valid use of tilde\n"
            exp = exp[i + 1:]
    return errorMessage


def ValidUseOfOperators(exp):
    errorMessage = ""
    i = 0
    orders = [[0, 1, 0, 1], [1, 1, 0, 0], [1, 0, 1, 0]]
    lefts = (getLeftOperators() + getDigits() + list(getParentheses()[0]))
    rights = (getRightOperators() + getDigits() + list(getParentheses()[1]))
    while i < len(exp):
        if exp[i] in getOperators():
            loc = getClass(exp[i]).getOperatorLoc()
            b1 = i - 1 >= 0 and exp[i - 1] in rights
            b2 = i + 1 < len(exp) and exp[i + 1] in lefts
            b3 = i + 1 == len(exp) or exp[i + 1] in getBinaryOperators() + getRightOperators() + list(
                getParentheses()[1])
            b4 = i - 1 == -1 or exp[i - 1] in getBinaryOperators() + getLeftOperators() + list(getParentheses()[0])
            booleans = [b1, b2, b3, b4]
            if exp[i] != '-':
                # print(b1,b2,b3,b4)
                if not ((loc == 0 and b2 and b4) or (loc == 1 and b1 and b2) or (loc == 2 and b1 and b3)):
                    errorMessage += bugExplanation(loc, booleans, exp, i) + "\n"

        i += 1
    return errorMessage


def bugExplanation(loc, booleans, exp, i):
    if loc == 1:
        if booleans[0]:
            lst = [exp[i + 1] if i + 1 < len(exp) else "empty", "right"]
        else:
            lst = [exp[i - 1] if i - 1 >= 0 else "empty", "left"]
        return lst[0] + " cannot be on the " + lst[1] + " of a binary operator"
    if loc == 0:
        if booleans[3]:
            lst = [exp[i + 1], "right"]
        else:
            lst = [exp[i - 1], "left"]
        return lst[0] + " cannot be on the " + lst[1] + " of a left operator"
    if loc == 2:
        if booleans[3]:
            lst = [exp[i - 1], "left"]
        else:
            lst = [exp[i + 1], "right"]
        return lst[0] + " cannot be on the " + lst[1] + " of a right operator"




