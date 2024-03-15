import os

a = float(input('Enter a number :'))
b = float(input('Enter another number :'))


if type(a) or type(b) != float:
    raise ValueError('Invalid input')
else:
    pass

op = input('Operation :')

if op == 'Addition' or 'Sum':
    print(a + b)

elif op == 'Subtraction' or 'Subtract':
    print(a - b)

elif op == 'Multiplication' or 'Multiply':
    print(a * b)

elif op == 'Divide' or 'Division':
    print(a/b)

else:
    raise ValueError('Invalid input')