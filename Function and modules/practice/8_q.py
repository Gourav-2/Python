'''Write a function safe_divide(a, b) that returns the result of a / b , but returns "Cannot divide by zero" if b is 0 .'''


def safe_devide(a,b):
    if b==0:
        print("b is 0 it is possible")
        return
    return a/b
print(safe_devide(4,0))