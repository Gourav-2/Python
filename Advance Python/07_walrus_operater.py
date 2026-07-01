def print_hello():
    print("hello")
    print("hello")
    print("hello")
    print("hello")
    print("hello")
    return 10

if(a:=print_hello()):#walrus operater function ke return type ko varriable me save kar deta hai 
    print(a)