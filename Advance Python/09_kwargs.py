# def fun1(**kwargs):
#     print(kwargs)


# fun1(gourav=55,nitin=55,summit=55)


def my_function(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    for key, value in kwargs.items():
        print(f"{key}: {value}")
 
my_function(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York
 
my_function()  # No output (empty dictionary)
my_function(a=1, b=2)
# Output:
# a: 1
# b: 2

