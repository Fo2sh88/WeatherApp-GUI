# Calculator - Command Line Version
# Basic Operations: Add, Subtract, Multiply, Divide

print("Welcome to the Calculator CLI!")
print('operations: add, subtract, multiply, divide')

num1 = float(input("Enter first number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
num2 = float(input("Enter second number: "))

if operation == 'add':
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {result}")
elif operation == 'subtract':
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: {result}")
elif operation == 'multiply':
    result = num1 * num2
    print(f"The result of {num1} * {num2} is: {result}")
elif operation == 'divide':
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please choose from add, subtract, multiply, divide.")

print("Thank you for using the Calculator CLI!")