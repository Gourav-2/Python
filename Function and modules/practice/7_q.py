'''Write a recursive function fibonacci(n) that prints the first n Fibonacci  numbers.'''
f=[]
for i in range(0,11):
    def fib(i):
        if i==0 or i==1:
          return i
        return fib(i-1)+fib(i-2)
    f.append(fib(i))

print(f)

