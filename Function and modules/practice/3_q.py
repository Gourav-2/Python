'''
Write a lambda function that adds two numbers and test it.'''


# a= lambda a,b:a+b
# print(a(10,15))


# *************

'''Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get
their squares.
'''



l=[1,2,3,4]

a=lambda x:x**2
print(list(map(a,l)))