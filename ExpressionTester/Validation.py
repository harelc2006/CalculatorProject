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
            b3 = index+1 != len(trimmed)
            i = exp.index("~")
            if not (b3 and (b1 or b2)):
                while i < len(exp) and not exp[i] in acceptable:
                    i += 1
                errorMessage += exp[exp.index("~"):i + 1] + " is not valid use of tilde\n"
            exp = exp[i+1:]
    return errorMessage



