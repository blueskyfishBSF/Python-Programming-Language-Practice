import numpy
while 1==1:
    a=numpy.random.randint(1,10)
    b=numpy.random.randint(1,10)
    print(a,"*",b,"=?")
    c=int(input('your_result'))
    if c==a*b:
        print('nb!')
    else:
        print('sb!')