'''
  
Using format() , create a sentence:
"My name is John and I am 25 years old."
by passing "John" and 25 as variables. '''


text="My name is {} and I am {} years old."

a="john"
b="33"
print(text.format(a,b))


# ***************************************Do the same using f-strings***********************/



text=f"My name is {a} and I am {b} years old."
print(text)
