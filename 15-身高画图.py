from numpy import zeros
import matplotlib.pyplot as plt
A=zeros(4)
B=zeros(4)
A[0]=1.60
A[1]=1.85
A[2]=1.75
A[3]=1.80
B[0]=0.50
B[1]=0.70
B[2]=1.90
B[3]=1.75
C=[1,2,3,4]
plt.plot(C,A,'r')
plt.plot(C,B,'b')
plt.show()





