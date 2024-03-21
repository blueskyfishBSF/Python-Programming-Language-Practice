import Fibonacci
def converging_ratio(x):
    c=Fibonacci.make_Fibonacci(x+1)
    d=Fibonacci.make_Fibonacci(x)
    return (c/d)

o=int(input('your x?'))
print(converging_ratio(o))


