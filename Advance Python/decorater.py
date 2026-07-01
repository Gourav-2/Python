def decorater(func):
    def wrapper():
        print("start")
        func()
        return wrapper()


@decorater
def hello():
    print("hello")


hello()
