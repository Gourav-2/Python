'''Write a decorator logger that prints "Function is being called" before
the function runs. Use it to decorate a function say_hello() that prints
"Hello!" .'''


def decorater(funx):
    def wrapper():
        print("Function is being called" )
        funx
        return wrapper()



@decorater
def say_hello():
    print("Hello!")

say_hello()