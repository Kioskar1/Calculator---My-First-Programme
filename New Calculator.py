a = float(input('Enter a number :'))
b = float(input('Enter another number :'))

if type(a) or type(b) != float:
    raise ValueError('Invalid input')
else:
    pass

op1 = input('Operation :')
op = op1.lower()

match op :
    case 'add' :
        print(a + b)

    case'subtract' :
        print(a - b)

    case'multiply' :
        print(a * b)

    case 'divide' :
        print(a / b)

    case _ :
        raise ValueError('Invalid operation')
