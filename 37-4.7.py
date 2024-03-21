def range(x):
    n=0
    k=x
    while x>=1:
        n=x+n
        x-=1
    m=n/k
    return m

x=int(input("your x"))
print(range(x))
