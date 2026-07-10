# function with a single parameter

def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator(a, b, operation):
    if operation == "add":
        return add(a, b)
    elif operation == "subtract":
        return subtract(a, b)
    elif operation == "multiply":
        return multiply(a, b)
    elif operation == "divide":
        return divide(a, b)
    else:
        return "Error: Invalid operation"
  
print("lets do some calculation")
a=int(input("enter your value a"))
b=int(input("enter your value b"))
operation = input("which operation you want to perform ?")
print(calculator(a,b,operation))

 