'''Write a function multiply(a, b) that has a proper docstring explaining what
it does. Then use help(multiply) to display the docstring.'''

def multiply(a,b):
    '''this funtion is multiply two digit 
    a is int
    b is also int '''
    return a*b


def help(n):
    print(n.__doc__)
print(multiply(10,15))
help(multiply)
