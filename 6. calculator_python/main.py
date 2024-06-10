# Define basic mathematical operations
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Dictionary to map operation symbols to their corresponding functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,   
    "/": divide
}

def calculator():
    # Get the first number from the user
    num_1 = float(input("What is your first number? "))
    # Display available operations
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        # Get the operation symbol from the user
        operation_symbol = input("Pick an operation from the line above: ")
        # Get the second number from the user
        num_2 = float(input("What is your second number? "))
        # Retrieve the function corresponding to the chosen operation
        calculation_function = operations[operation_symbol]
        # Perform the calculation
        answer = calculation_function(num_1, num_2)

        # Display the result of the calculation
        print(f"{num_1} {operation_symbol} {num_2} = {answer}")

        # Check if the user wants to continue with the current answer or start a new calculation
        if input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation: ") == "y":
            num_1 = answer
        else:
            should_continue = False
            print("Have a good day, bye!")

# Start the calculator
calculator()
