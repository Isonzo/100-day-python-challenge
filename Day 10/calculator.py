from calculator_art import logo

def add(n1, n2):
    """Adds n1 and n2."""
    return n1 + n2

def subtract(n1, n2):
    """Subtracts n1 and n2."""
    return n1 - n2

def multiply(n1, n2):
    """Multiplies n1 and n2."""
    return n1 * n2

def divide(n1, n2):
    """Divides n1 and n2."""
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    }

def calculator():
    print(logo)
    flag = True
    num1 = float(input("Enter the first number\n"))

    for symbol in operations:
        print(symbol)

    while flag:
        operation_symbol = input("Pick an operation: ")

        num2 = float(input("Enter the next number\n"))

        result = operations[operation_symbol](num1, num2)

        print (f"{num1} {operation_symbol} {num2} = {result}")

        if input(f"type 'y' to continue calculating with {result} or 'n' to start a new calculation\n").lower() == "y":
            num1 = result
        else:
            flag = False
            calculator()

calculator()
