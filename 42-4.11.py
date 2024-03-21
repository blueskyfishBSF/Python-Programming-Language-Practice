def f(x):
    y=4*x+1
    return y
import random
import numpy
t=numpy.zeros(100)
for i in range(100):
    t[i]=random.uniform(0,10)
for x in range(100):
    b=(f(t[x])-f(2))/(t[x]-2)
    if b==4:
        print(t[x],"yes")
    elif b!=4:
        print(t[x],"no")



