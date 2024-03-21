from math import pi
k=0
N1=int(input('N1?'))
pi_A=0
while N1<=100:
    B=1/(((4*k)+1)*((4*k)+3))
    N1+=1
    k+=1
    pi_A+=B
print(8*pi_A)

k=1
N2=int(input('N2?'))
pi_A=0
while N2<=100:
    B=1/(k**2)
    N2+=1
    k+=1
    pi_A+=B
print((6*pi_A)**(1/2))


pi_c=pi
print('pi={}'.format(pi_c))




