a=int(input("enter a number between 1 to 10:"))

match a :
    case 1:
        print("num is one ")
    case 5:
        print("num is four")
    case 10 :
        print("num os 10")
    case _:
        print("invalid")