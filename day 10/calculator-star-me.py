

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    
}

num1 = int(input("What is the first number?: "))



for symbol in operations:
    print(symbol)

operation_symbol = input("pick an operation from the line above: ")

num2 = int(input("What is the second number?: "))

fun = operations[operation_symbol]

answer = fun(num1,num2) 

print(f"{num1} {operation_symbol} {num2} = {answer}")

###############
operation_symbol = input("pick another operation: ")

num3 = int(input("What is the third number?: "))

fun = operations[operation_symbol]
second_answer = fun(fun(num1,num2),num3)

print(f"{answer} {operation_symbol} {num3} = {second_answer}")