# Store number variables for the two numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# The sum of the two numbers variable
sum = float(num1) + float(num2)
sum2 = float(num1) - float(num2)
sum3 = float(num1) * float(num2)
sum4 = float(num1) / float(num2)

# What operator to use
choice = input('Enter an operator, + = addition, - = subtraction, * = multiplication and / = division: ')

# Different sums based on the operators
match choice:
    case '+':
        print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

    case '-':
        print('The sum of {0} and {1} is {2}'.format(num1, num2, sum2))

    case '*':
        print('The sum of {0} and {1} is {2}'.format(num1, num2, sum3))

    case '/':
        print('The sum of {0} and {1} is {2}'.format(num1, num2, sum4))
