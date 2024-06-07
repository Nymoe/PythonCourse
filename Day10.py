#Functions with outputs

def my_function(something):
    print(something)

def my_function2(something):
    """This is a docstring"""
    return something

#Calculator

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# num1 = int(input("What is the first number?: \n"))
# num2 = int(input("What is the second number?: \n"))
# print()
# for operation in operations:
#     print(f"{operation}")
# symbol = input("Which operation would you like to do?: ")
#
# answer = operations[symbol](num1, num2)
#
# print(f"{num1} {symbol} {num2} = {answer}")
#
# symbol = input("Choose another operation")
# num1 = answer
# num2 = int(input("What number would you like? \n"))
# answer = operations[symbol](num1, num2)
# print(f"{num1} {symbol} {num2} = {answer}")
def calculator():
    num1 = int(input("What is the first number?: \n"))
    for operation in operations:
        print(f"{operation}")
    symbol = input("Which operation would you like to do?: ")
    num2 = int(input("Choose the next number: \n"))
    answer = operations[symbol](num1, num2)
    print(f"{answer} {symbol} {num2} = {answer}")
    ask = input("Would you like to add another operation: Y or N\n")
    if ask.lower() == 'y':
        calculate = True
    else:
        calculate = False
    while calculate:
        for operation in operations:
            print(f"{operation}")
        symbol = input("Which operation would you like to do?: ")
        num1 = answer
        num2 = int(input("Choose the next number: \n"))
        answer = operations[symbol](num1, num2)
        print(f"{num1} {symbol} {num2} = {answer}")
        ask = input("Would you like to add another operation: Y or N\n")
        if ask.lower() == 'y':
            calculate = True
        else:
            calculate = False

calculator()