while True:
    try:
        a=int(input("enter 1st num :"))
        b=int(input("enter 2nd num :"))
        print(f"division is {a/b}")
    except Exception as e:
        print("not devide by zero",e)
    finally:                         #this code always run
        print("this is finally  part ")