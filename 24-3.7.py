import random
N=int(input('your N?'))
M=0
for i in range(N):
    A=random.randint(1,6)
    print('random int {}={}'.format(i,A))
    if A==6:
     M+=1
print('M={}'.format(M))
print('M/N={}'.format(M/N))




