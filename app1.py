# Type hinting in python

# Without type hinting
def add1(num1, num2):
    return num1 + num2

# With type hinting
def add2(num1: int, num2: int) -> int:
    return num1 + num2

print(add1('hello', 'world')) # This won't give a warning.
print(add2('hello', 'world')) # This will give a warning because of type hinting.
