import matplotlib.pyplot as plt
import numpy
x=[0,1,2,3,4]
y=[0.5,2.0,1.0,1.5,7.5]
a=int(input("your_a?"))
b=int(input("your_b?"))
e=0

E=numpy.zeros(5)
R=numpy.zeros(5)

for i in range(0,5):
    A=(a*x[i]+b-y[i])
    E[i]=e
    e=A+e
    R[i]=e

largest=R[i]
for i in range(0,5):
    if R[i]>largest:
        largest=R[i]
print('largest=',largest)

t=numpy.linspace(0,4,1000)
B=a*t+b

plt.subplot(2,1,1)
plt.plot(x,E[x],'r')
plt.plot(t,B,'b')

plt.show()