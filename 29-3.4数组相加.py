import numpy as np
N = 5
h = np.zeros(N) # heights of family members (in meter)
h[0] = 1.60; h[1] = 1.85; h[2] = 1.75; h[3] = 1.80; h[4] = 0.50
sum = 0
i=0
while i<5:
    sum = sum + h[i]
    i+=1
average = sum/N
print('Average height: {:g} meter'.format(average))




