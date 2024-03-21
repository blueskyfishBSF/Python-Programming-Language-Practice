import numpy
N=int(input("your N"))
n=float(input("your n"))
h=8/N
a=-4
while a<=4:
    b=a-a**2
    if b<0:
       b=b
    else:
       b=-b
       if b<n:
        print(a)
    a+=h