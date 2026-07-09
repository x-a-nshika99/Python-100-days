# define function

from unittest.mock import call


def greet(name):
    return f"Hello, {name}!" 

# call the function
result = greet("Alice")
print(result)