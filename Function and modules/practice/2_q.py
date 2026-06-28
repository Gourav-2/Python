'''Write a function full_name(first, last) that takes first name and last name
as parameters and returns a single string in the format "First Last" '''

# def full_name(first,last):
#     return first +" "+last

# print(full_name("gourav","chouhan"))


'''Write a function calculate_area(length, width=10) that returns the area of
a rectangle. Test it by calling the function with:
Both length and width
Only length (use default width)'''


def calculate_area(length,width=10):
    return length*width

print(calculate_area(10,15))
print(calculate_area(10))