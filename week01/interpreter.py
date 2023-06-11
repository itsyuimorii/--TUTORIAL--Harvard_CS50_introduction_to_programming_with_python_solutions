def main():
    # Get the expression from the user
    expression = input("Expression: ")

    # Split the expression into operands and operator
    x, operator, y = map(str.strip, expression.split())

    try:
        # Convert operands to float
        x = float(x)
        y = float(y)

        # Perform the calculation based on the operator
        result = calculate(x, operator)
        print(result)
    except ValueError:
        print("Invalid input. Please enter a valid expression.")

def calculate(x, operator):
    # Define the operators and their corresponding functions
    operators = {
        "+": add,
        "-": sub,
        "*": mult,
        "/": div
    }

    if operator in operators:
        # Call the appropriate function based on the operator
        return operators[operator](x, y)
    else:
        raise ValueError("Invalid operator.")

def add(x, y):
    # Add two numbers
    return x + y

def sub(x, y):
    # Subtract the second number from the first number
    return x - y

def mult(x, y):
    # Multiply two numbers
    return round(x * y, 2)

def div(x, y):
    if y != 0:
        # Divide the first number by the second number
        return round(x / y, 2)
    else:
        raise ZeroDivisionError("Division by zero is not allowed.")

main()
