import random
from numpy import zeros
A=zeros(6)
for i in range(6):
    A[i]=random.uniform(0,10)
print(A)

n=len(A)
for i in range(n-1):
        for j in range(i+1,n):
            if A[i]>A[j]:
                A[i],A[j]=A[j],A[i]
print(A)




