'''
Write a program that keeps asking the user to enter a password until they
enter the correct one'''



password="gourav"

while True:
    user_enter=input("enter a password:")
    if(user_enter==password):
        print("password is correct")
        break 
    else:
        print("incorreact password ")
        print('try again')