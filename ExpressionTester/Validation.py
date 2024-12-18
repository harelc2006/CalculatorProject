from Symbols import *
from Trim.Trimmer import allMinusTrimmer
from Trim.Trimmer import minusTrimmer


def emptyExpression(exp):
    errorMessage = ""
    if len(exp) > 0:
        if len(exp) == exp.count(' ') + exp.count('\t') + exp.count('\n') + exp.count('\r'):
            errorMessage += "white space expression"
    else:
        errorMessage += "empty expression"
    return errorMessage


def validSymbols(exp):
    symbols = getOperators() + getDigits() + getParentheses()
    errorMessage = ""
    for char in exp:
        if char not in symbols:
            errorMessage += "unknown symbol " + char + "\n"
    return errorMessage


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
            trimmed = allMinusTrimmer(exp)
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


def bugExplanation(loc, booleans, exp, i):
    if loc == 1:
        if booleans[0]:
            lst = [exp[i + 1] if i + 1 < len(exp) else "empty", "right"]
        else:
            lst = [exp[i - 1] if i - 1 >= 0 else "empty", "left"]
        return lst[0] + " cannot be on the " + lst[1] + " of a binary operator"
    if loc == 0:
        if booleans[3]:
            lst = [exp[i + 1] if i + 1 < len(exp) else "empty", "right"]
        else:
            lst = [exp[i - 1] if i - 1 >= 0 else "empty", "left"]
        return lst[0] + " cannot be on the " + lst[1] + " of a left operator"
    if loc == 2:
        if booleans[3]:
            lst = [exp[i - 1] if i - 1 >= 0 else "empty", "left"]
        else:
            lst = [exp[i + 1] if i + 1 < len(exp) else "empty", "right"]
        return lst[0] + " cannot be on the " + lst[1] + " of a right operator"


def ValidUseOfOperators(exp):
    errorMessage = ""
    i = 0
    orders = [[0, 1, 0, 1], [1, 1, 0, 0], [1, 0, 1, 0]]
    lefts = (getLeftOperators() + getDigits() + list(getParentheses()[0]))
    rights = (getRightOperators() + getDigits() + list(getParentheses()[1]))
    while i < len(exp):
        if exp[i] in getOperators():
            b1 = i - 1 >= 0 and exp[i - 1] in rights
            b2 = i + 1 < len(exp) and exp[i + 1] in lefts
            b3 = i + 1 == len(exp) or exp[i + 1] in getBinaryOperators() + getRightOperators() + list(
                getParentheses()[1])
            b4 = i - 1 == -1 or exp[i - 1] in getBinaryOperators() + getLeftOperators() + list(getParentheses()[0])
            booleans = [b1, b2, b3, b4]
            if exp[i] != '-':
                loc = getClass(exp[i]).getOperatorLoc()
                if not ((loc == 0 and b2 and b4) or (loc == 1 and b1 and b2) or (loc == 2 and b1 and b3)):
                    errorMessage += bugExplanation(loc, booleans, exp, i) + "\n"
            else:
                if not ((b2 and b4) or (b1 and b2)):
                    if not (b1 or b2 or b4):
                        errorMessage += "minus has to be used a either a left or a binary operator\n"
                    else:
                        if not b2:
                            errorMessage += (exp[i + 1] if i + 1 < len(exp) else "empty") + " cannot be on the right of" \
                                                                                            " a minus\n"
                        if not (b4 or b1):
                            errorMessage += "you have to use a minus as binary or an unary operator\n"

        i += 1
    return errorMessage


def checkParentheses(exp):
    errorMessage = ""
    i = 0
    count = 0
    while i < len(exp):
        ch = exp[i]
        if ch == '(':
            count += 1
        if ch == ')':
            count -= 1
            if count < 0:
                errorMessage += ") with no open for it in position: " + i + "\n"
        i += 1
    if count != 0:
        errorMessage += "number of ( doesnt match the number of )"
    return errorMessage


def floatValidation(exp):
    i = 0
    errorMessage = ""
    number = ""
    while i < len(exp):
        if exp[i] == '.' or exp[i].isdigit():
            number += exp[i]
        else:
            if number.count('.') > 0:
                errorMessage += validateFloatNumber(number)
            number = ""
        i += 1
    if number.count('.') > 0:
        errorMessage += validateFloatNumber(number)
    return errorMessage


def validateFloatNumber(number):
    if number.count('.') > 1:
        return number + " is not valid - cannot have more than 1 dot in a number\n"
    index = number.index('.')
    if index > 0 and index + 1 < len(number) and number[index - 1].isdigit() and number[index + 1].isdigit():
        return ""
    else:
        return number + " is not valid - you have to have a number before and after the .\n"


def validateExpression(exp):
    em = ""
    em += emptyExpression(exp)
    if em != "":
        raise SyntaxError(em)
    exp = minusTrimmer(exp)
    em += validSymbols(exp)
    em += validSymbols(exp)
    em += validSequence(exp)
    em += ValidTildeUse(exp)
    em += ValidUseOfOperators(exp)
    em += checkParentheses(exp)
    em += floatValidation(exp)
    if em != "":
        raise SyntaxError(em)
    print("valid expression")
