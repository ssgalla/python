# users inputs for the numbers and the operators
num1 = float(input('Enter your first number: '))
operator = input(('Enter operator: '))
num2 = float(input('Enter your second number: '))

# if operator is (+ | -  | * | /) then print out number 1 (+ | - | * | /) number 2
if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '/':
    print(num1 / num2)
elif operator == '*':
    print(num1 * num2)
# if the user didn't put an operator
else:
    print('Invalid operator')
