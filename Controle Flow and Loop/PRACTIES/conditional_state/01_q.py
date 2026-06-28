'''

Write a program that asks the user for a number and prints whether it is 
positive, negative, or zero.

'''

num=eval(input("enter a number : "))

if num>0:
    print("number is positve")
elif num<0:
    print("number is negative ")
elif num==0:
    print("zero")
else:
    print("invalid")