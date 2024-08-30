# Calculate the square of 2 numbers


def square(x):
    return x * x

def cube(x):
    return x * x * x

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def power(x, y):
    return x ** y

def mod(x, y):
    return x % y

def factorial(x):
    if x < 0:
        raise ValueError("Cannot calculate factorial of a negative number!")
    elif x == 0 or x == 1:
        return 1
    else:
        result = 1
        for i in range(2, x + 1):
            result *= i
        return result
