def operation(operation_name):
    def addition(*args):
        total = 0
        for i in args:
           total += i
        return total
    def multiplication(*args):
        product = 1
        for i in args:
            product *= i
        return product
    def subtraction(*args):
        if len(args) < 2:
           raise ValueError('At least two numbers are required for subtraction.')
        resullt = args[0]
        for i in args[1:]:
            resullt -= i
        return resullt
    def division (*args):
        if len(args) < 2:
            raise ValueError('At least two numbers are required for division')
        resullt = args[0]
        for i in args[1:]:
            if i == 0:
                raise ZeroDivisionError('Divison by zero is not allowed.')
            resullt /= i
        return resullt
    def exponentiation(base,exponent):
        return base ** exponent
    operations = {
        'addition': addition,
        'multiplication': multiplication,
        'subtraction': subtraction,
        'division': division,
        'exponentiation': exponentiation
    }
    if operation_name in operations:
        return operations[operation_name]
    else:
        raise ValueError('Unknown operation')
    def get_user_input():
        print('Available operations: addition, multiplication, subtraction, division, exponentiation')
        choice = input('Enter the operation you want to perform: ')
        func = operation(choice)
        if choice == 'exponentiation':
            base = float(input('Enter the base: '))
            exponent = float(input('Enter the exponent: '))
            result = func(base, exponent)
        else:
            numbers = list(map(float, input('Enter numbers separated by spaces: ').split()))
            result = func(*numbers) 
#The `*` operator passes elements of a list or tuple as separate arguments. This is particularly useful when a function requires a specific number of arguments
        print('Result: ',result)
    get_user_input()