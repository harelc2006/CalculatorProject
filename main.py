from ExpressionTester.Validation import validateExpression
from calculations.connector import calculate
from colorama import Fore, Style


def start():
    print("=" * 78)  # Printing separator
    print("Welcome to the Equation Evaluator!")
    print("=======================================================")
    print("Instructions:")
    print("+ plus: Adds numbers together. For example: 4 + 4 = 8")
    print("- minus: Subtracts numbers. For example: 4 - 2 = 2")
    print("* times: Multiplies numbers. For example: 4 * 2 = 8")
    print("/ divide: Divides numbers. For example: 8 / 2 = 4")
    print("^ exponentiation: Raises the first number to the power of the second. For example: 2 ^ 3 = 8")
    print("% modulo: Returns the remainder of division. For example: 10 % 3 = 1")
    print("! factorial: Multiplies all whole numbers from the number down to 1. For example: 4! = 4*3*2*1 = 24")
    print("~ tilde: Converts a positive number to negative and vice versa. For example: ~5 = -5")
    print("&: Minimum value. Returns the smallest number. For example: 5 & 12 = 5")
    print("$: Maximum value. Returns the largest number. For example: 4 $ 12 = 12")
    print("@: Average value. Returns the average of two numbers numbers. For example: 4 @ 2 = 3")
    print("#: Custom operation, returns some calculated value based on the context. For example: 123# might return 6 "
          "(context dependent)")
    print(
        "-: Unary minus. Converts a positive number to negative and vice versa. For example: -5 becomes -5, and --5 "
        "becomes 5.")
    print("==============================================================================")
    exp = input("enter your equation: ")
    while exp.strip().upper() != "EXIT":
        evaluate(exp)
        print("==============================================================================")
        exp = input("enter your equation: ")


def evaluate(exp):
    try:
        validateExpression(exp)  # Assuming you have a validateExpression function
        exp = exp.strip()
        result = calculate(exp)  # Assuming you have a calculate function
        if result.is_integer():
            result = int(result)
        print(f"{Fore.GREEN}✔ answer: {Style.RESET_ALL}{result}")
    except Exception as e:
        # Split exception message to remove redundant newlines and display clean error
        ems = "\n".join(set(str(e).replace("int too large to convert to float","too long to calculate").split("\n")))
        print(f"{Fore.RED}✘ error:{Style.RESET_ALL} {ems}")


start()
