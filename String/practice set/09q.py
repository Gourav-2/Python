'''
Take a user input string and check if it is a palindrome (same forwards and
backwards)'''
text=input("enter your string:")
text1=text[-1::-1]
if(text==text1):
    print("string is palendrom")
else:
    print("no")