import numpy
n=numpy.random.randint(0,10)
print("n=",n)
while n<=21:
    m=int(input("do want a new number?1=yes,2=no"))
    if m==1:
            k=numpy.random.randint(0,10)
            print("k=",k)
            n=n+k
            print("n=",n)
    if m==2:
            print("n=",n)
print("n=",n)


