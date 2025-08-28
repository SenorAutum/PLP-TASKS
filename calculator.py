# --- Basic Calculator Program ---

# 1. Get user input
# We ask the user for the first number and store it.
# The input() function reads text, so we use float() to convert it to a number that can have decimals.
try:
    num1 = float(input("Enter the first number: "))

    # We ask for the second number and do the same conversion.
    num2 = float(input("Enter the second number: "))

    # We ask for the operation the user wants to perform.
    operation = input("Enter the operation (+, -, *, /): ")

    # 2. Perform the operation based on user's input
    result = 0
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        # We add a check to prevent division by zero, which would cause an error.
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            exit() # Exit the program if there's an error
        else:
            result = num1 / num2
    else:
        # If the user enters an invalid operator, we print an error message.
        print("Invalid operation. Please use +, -, *, or /.")
        exit() # Exit the program

    # 3. Print the result in the required format
    # The f-string (f"...") allows us to easily embed variables directly into our string.
    print(f"{num1} {operation} {num2} = {result}")

except ValueError:
    # This 'except' block catches errors if the user enters text instead of a number.
    print("Invalid input. Please enter valid numbers.")

