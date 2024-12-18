def allMinusTrimmer(exp):
    exp = exp.replace(" ", "")
    result = []
    prime = False
    i = 0
    while i < len(exp):
        if exp[i] == '-':
            minus_count = 0
            while i < len(exp) and exp[i] == '-':
                minus_count += 1
                i += 1
            if minus_count % 2 == 1:
                result.append('-')
            else:
                result.append('')
        else:
            result.append(exp[i])
            i += 1
    return ''.join(result)


def minusTrimmer(exp):
    exp = exp.replace(" ", "")
    result = []
    i = 0
    while i < len(exp):
        if exp[i] == '-':
            minus_count = 0
            while i < len(exp) and exp[i] == '-':
                minus_count += 1
                i += 1
            if minus_count % 2 == 1:
                result.append('-')
            else:
                result.append('--')
        else:
            result.append(exp[i])
            i += 1
    return ''.join(result)
