print("\nWelcome to our simple calculator!")
print("This calculator can perform addition, subtraction, multiplication, and division.")
print("It works by taking two numbers and an operator as input.\n")
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    # Check for division by zero
    if num2 == 0:
        print("Division by zero is not allowed!")
        exit()
    result = num1 / num2
else:
    print("Invalid operator")
    exit()

# Output the result
print("Result: ", result)
print("Thank you for using our calculator!\n")