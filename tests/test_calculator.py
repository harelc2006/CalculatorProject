import pytest
from ExpressionTester.Validation import validateExpression
from calculations.connector import calculate


def evaluate(exp):
    """"evaluates the expression"""
    try:
        if len(exp) > 1500:
            raise MemoryError("expression too long")
        validateExpression(exp)  # Assuming you have a validateExpression function
        exp = exp.strip()
        result = calculate(exp)  # Assuming you have a calculate function
        return result
    except Exception as e:
        # Split exception message to remove redundant newlines and display clean error
        ems = "\n".join(set(str(e).replace("int too large to convert to float", "too long to calculate").split("\n")))
        return ems


def test_syntax_errors():
    print(evaluate("2*^3"))
    print(evaluate("2+()+3"))
    print(evaluate("~-~2"))
    print(evaluate("2**3"))
    print(evaluate("23-"))


def test_gibberish_string():
    print(evaluate("abc&1t5"))


def test_empty_and_whitespace_strings():
    print(evaluate("            "))
    print(evaluate(""))


def test_simple_expressions():
    assert evaluate("2^3") == 2 ** 3
    assert evaluate("2^0") == 2 ** 0
    assert evaluate("1+1") == 1 + 1
    assert evaluate("3-2") == 3 - 2
    assert evaluate("2*3") == 2 * 3
    assert evaluate("4/3") == 4 / 3
    assert evaluate("8%3") == 8 % 3
    assert evaluate("12$5") == 12
    assert evaluate("12&5") == 5
    assert evaluate("13@5") == 9
    assert evaluate("~5") == -1 * 5
    assert evaluate("5!") == 120
    assert evaluate("99##") == 9
    assert evaluate("1--3^2") == 1 - (-3) ** 2
    assert evaluate("-3^2") == -(3 ** 2)


def test_complex_expressions():
    assert evaluate("(5 + 3) ^ 2 - 10 /2") == 59
    assert evaluate("((8 * 5) @ 2) + 7") == 28
    assert evaluate("((6 + 3) ^ 3) @ 4 - 5") == 361.5
    assert evaluate("(10 $ 3)# + (4 + 2)") == 7
    assert evaluate("3! % ((2 + 5) ^ 2)# ^ 3") == 216
    assert evaluate("(9 @ 2) - 4 + 7 ^ 2") == 50.5
    assert evaluate("5 + (2 @ 3) * 3 ^ 2") == 27.5
    assert evaluate("(4 ^ 2) @ (5 - 3) # *3") == 27
    assert evaluate("(3 * (4 + 2)) ^ 2 + 1 @ 5") == 327
    assert evaluate("~(72 # ^ 2) ^ 3 + 5 @ 2") == -531437.5
    assert evaluate("5 * 3 ^ (2 @ 1) + 10 # ^ 4") == 26.98076211353316
    assert evaluate("(6 ^ 2) @ 413# + 3") == 25
    assert evaluate("((5 + 2) @ 3) ^ 2 + 10") == 35
    assert evaluate("4 + (5 @ 2) * 32.56#") == 60
    assert evaluate("((6 * 2) ^ 3) & (8 @ 2)") == 5
