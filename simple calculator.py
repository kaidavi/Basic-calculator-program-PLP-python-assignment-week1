# Simple Calculator Program

def calculator():
    # Ask for user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ").strip()

    # Perform the operation
    if operation == "+":
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}")
    elif operation == "/":
        if num2 != 0:  # Avoid division by zero
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please choose one of +, -, *, or /.")

# Run the calculator
calculator()
