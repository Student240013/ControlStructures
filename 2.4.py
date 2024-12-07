number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ").strip()

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    if number2 != 0:
        result = number1 / number2
    else:
        result = "undefined (division by zero)"
else:
    result = "invalid operator"

print(f'{number1} {operator} {number2} = {result}')