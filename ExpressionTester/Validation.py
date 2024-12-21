from MinusManage.Convert import conversion
from Symbols import *
from MinusManage.Trimmer import minusTrimmer

""""
in all of this file if there is an error it puts something in errorMessage otherwise it's stays empty
"""


def emptyExpression(exp):
    """"
    gets: expression
    :returns: if its empty empty expression and if its white space expression returns white space expression
    """
    errorMessage = ""
    if len(exp) > 0:
        if len(exp) == exp.count(' ') + exp.count('\t') + exp.count('\n') + exp.count('\r'):
            errorMessage += "white space expression\n"
    else:
        errorMessage += "empty expression\n"
    return errorMessage


def validSymbols(exp):
    """"
    gets: expression
    :returns: if its made from valid symbols
    """
    symbols = getOperators() + getDigits() + getParentheses() + list('.')
    errorMessage = ""
    for char in exp:
        if char not in symbols:
            errorMessage += "unknown symbol " + char + "\n"
    return errorMessage


def validSequence(exp):
    """"
    gets: expression
    :returns: if the only sequence in it is is minus/digits/parentheses
    """
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
        if sym not in symbols and sym in getOperators():
            errorMessage += "cannot put " + sym + " consecutively\n"
    return errorMessage


def ValidTildeUse(exp):
    """"
    gets: expression
    :returns: if tilde use is valid
    """
    errorMessage = ""
    if exp.count("~") > 0:
        acceptable = getDigits() + ['(']
        while exp.count("~") > 0:
            index = exp.index("~")
            b1 = index + 2 < len(exp) and (exp[index + 1] in ['S', 'U'] and exp[index + 2] in acceptable)
            b2 = index + 1 < len(exp) and exp[index + 1] in acceptable
            b3 = index + 1 != len(exp)
            i = index
            if not (b3 and (b1 or b2)):
                while i < len(exp) and not exp[i] in acceptable:
                    i += 1
                errorMessage += exp[exp.index("~"):i + 1] + " is not valid use of tilde\n"
            exp = exp[i + 1:]
    return errorMessage


def bugExplanation(loc, booleans, exp, i):
    """"
    the function is being used as an explanation for ValidUseOfOperators() function
    gets: location,i,expression,booleans list
    :returns: if the only sequence in it is is minus/digits/parentheses
    """
    if loc == 1:
        if booleans[0]:
            lst = [exp[i + 1] if i + 1 < len(exp) else "empty", "right"]
        else:
            lst = [exp[i - 1] if i - 1 >= 0 else "empty", "left"]
        return lst[0] + " cannot be on the " + lst[1] + " of a binary operator\n"
    if loc == 0:
        if booleans[3]:
            lst = [exp[i + 1] if i + 1 < len(exp) else "empty", "right"]
        else:
            lst = [exp[i - 1] if i - 1 >= 0 else "empty", "left"]
        return lst[0] + " cannot be on the " + lst[1] + " of a left operator\n"
    if loc == 2:
        if booleans[3]:
            lst = [exp[i - 1] if i - 1 >= 0 else "empty", "left"]
        else:
            lst = [exp[i + 1] if i + 1 < len(exp) else "empty", "right"]
        return lst[0] + " cannot be on the " + lst[1] + " of a right operator\n"


def ValidUseOfOperators(exp):
    """"
    gets: expression
    :returns: if the operators in it are being use validly
    """
    errorMessage = ""
    i = 0
    lefts = (getLeftOperators() + getDigits() + list(getParentheses()[0]))
    rights = (getRightOperators() + getDigits() + list(getParentheses()[1]))
    while i < len(exp):
        if exp[i] in getAllOperators():
            b1 = i - 1 >= 0 and exp[i - 1] in rights  # checks if the operator has valid token on its left (8!+3 or 8+3)
            b2 = i + 1 < len(exp) and exp[i + 1] in lefts  # checks if the operator has valid token on its right
            # (8+~3) or (8+3)
            b3 = i + 1 == len(exp) or exp[i + 1] in getBinaryOperators() + getRightOperators() + list(
                getParentheses()[1])  # checks if the operator has valid token on its right , this used for right
            # operators (123# + 3)
            b4 = i - 1 == -1 or exp[i - 1] in getBinaryOperators() + getLeftOperators() + list(getParentheses()[0])
            # checks if the operator has valid token on its left , this used for left operators
            booleans = [b1, b2, b3, b4]
            if exp[i] != 'S':
                loc = getClass(exp[i]).getOperatorLoc()
                if not ((loc == 0 and b2 and b4) or (loc == 1 and b1 and b2) or (loc == 2 and b1 and b3)):
                    errorMessage += bugExplanation(loc, booleans, exp, i) + "\n"
            else:
                b = i + 1 < len(exp) and exp[i + 1] in (getDigits() + list(getParentheses()[0]) + list('S'))
                if not (b and b4):
                    if not b:
                        errorMessage += "sign minus have to be before a number or (\n"
                    if not b2:
                        errorMessage += "sign minus can only come after a binary/left operator or a (\n"

        i += 1
    return errorMessage


def checkParentheses(exp):
    """"
    gets: expression
    :returns: if the parentheses in it are being use validly
    """
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
                errorMessage += ") with no open for it in position: " + str(i+1) + "\n"
        i += 1
    if count != 0:
        errorMessage += "number of ( doesnt match the number of )\n"
    if exp.count("()") > 0:
        errorMessage += "cannot open and close parentheses immediately\n"
    return errorMessage


def floatValidation(exp):
    """"
    gets: expression
    :returns: if the floats in it are written validly
    """
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
    """"
    used as a help function for floatValidation()
    gets: number
    :returns: if the number is a float
    """
    if number.count('.') > 1:
        return number + " is not valid - cannot have more than 1 dot in a number\n"
    index = number.index('.')
    if index > 0 and index + 1 < len(number) and number[index - 1].isdigit() and number[index + 1].isdigit():
        return ""
    else:
        return number + " is not valid - you have to have a number before and after the .\n"


def validateExpression(exp):
    """"
    gets: expression
    :returns: does all the tests functions in the right order and raises the errors with the messages received
    """
    em = ""
    em += emptyExpression(exp)
    if em != "":
        raise SyntaxError(em)
    exp = exp.replace(" ", "").replace("\t", "")
    em += validSymbols(exp)
    em += validSequence(exp)
    if em != "":
        raise SyntaxError(em)
    exp = conversion(exp)
    exp = minusTrimmer(exp)
    em += ValidTildeUse(exp)
    em += ValidUseOfOperators(exp)
    em += checkParentheses(exp)
    em += floatValidation(exp)
    if em != "":
        em = em.replace("S ", "sign minus ")
        em = em.replace("B ", "binary minus ")
        em = em.replace("U ", "unary minus ")
        raise SyntaxError(em)
