def sum(a,b):
    return a+b
print(sum(5,2))


def sum1(*args):
    print(args)
    total=0
    for i in args:
        total+=i
    print(total)

sum1(1,2,2,2,2)