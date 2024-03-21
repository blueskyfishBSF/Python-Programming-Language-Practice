def x(A):
    mul=1
    while A>=1:
        mul*=A
        A=A-1
    return mul

C=0
for B in range (1,11,1):
    C+=x(B)

print(C)