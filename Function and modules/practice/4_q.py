'''
Write a recursive function factorial(n) that returns the factorial of a
number'''


# num=int(input("enter a number :"))

# def fact(n):
#     if(n==0):
#         return 1
#     return n*fact(n-1)

# print(f"Factorial is {fact(num)}")



# ****************************************

'''Write a recursive function sum_of_digits(n) that returns the sum of all digits
of a given number.
# '''
# def sum_of_digit(n):
#     if(n==0):
#         return 0
#     return n+sum_of_digit(n-1)

# print(sum_of_digit(4))


def sum_of_digit(n):
    if n==0:
        return 0
    return n%10+sum_of_digit(n//10)

print(sum_of_digit(123))