def make_Fibonacci(x):
    m=0
    c=1
    while m<x:
        c+=c
        m+=1
    return c

if __name__=='__main__':
    x=int(input('your n?'))
    m=0
    c=1
    while m<x:
        c+=c
        m+=1
    print(c)