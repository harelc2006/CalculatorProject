def minusTrimmer(exp):
    """"
    gets: expression after the minus categorization
    returns: trims sign minuses and unary minuses to only leaves either 2 or 1 depends on the number of sign
    minuses/unary minuses
    """
    result = []
    i = 0
    while i < len(exp):
        if exp[i] == 'U':
            minus_count = 0
            while i < len(exp) and exp[i] == 'U':
                minus_count += 1
                i += 1
            if minus_count % 2 == 1:
                result.append('U')
            else:
                result.append('UU')

        if i < len(exp) and exp[i] == 'S':
            minus_count = 0
            while i < len(exp) and exp[i] == 'S':
                minus_count += 1
                i += 1
            if minus_count % 2 == 1:
                result.append('S')
            else:
                result.append('SS')
        elif i < len(exp):
            result.append(exp[i])
            i += 1

    return ''.join(result)


def allMinusTrimmer(exp):
    """"
    gets: expression after the sign minus care
    returns: trims sign minuses and unary minuses to only leaves either 0 or 1 depends on the number of sign
    minuses/unary minuses
    """
    result = []
    i = 0
    while i < len(exp):
        if exp[i] == 'U':
            minus_count = 0
            while i < len(exp) and exp[i] == 'U':
                minus_count += 1
                i += 1
            if minus_count % 2 == 1:
                result.append('U')

        if i < len(exp) and exp[i] == 'S':
            minus_count = 0
            while i < len(exp) and exp[i] == 'S':
                minus_count += 1
                i += 1
            if minus_count % 2 == 1:
                result.append('S')
        elif i < len(exp):
            result.append(exp[i])
            i += 1

    return ''.join(result)
