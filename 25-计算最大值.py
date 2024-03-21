import numpy
t = numpy.linspace(0, 1, 1001)
B=0
for i in range(len(t)):
  t[i] = 5*t[i] - 0.5*9.81*t[i]**2
  largest = t[0]
for i in range(len(t)):
   if t[i]>largest:
       largest = t[i]
       B+=1
print(largest)
print(B)




