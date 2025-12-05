# divide_numbers.py

try:
    # Take user input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform division
    result = num1 / num2
    print(f"Result: {result}")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid numeric values.")
