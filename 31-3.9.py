import numpy as np
import matplotlib.pyplot as plt
v0 = 5 # Initial velocity
g = 9.81 # Acceleration of gravity
t = np.linspace(0, 1, 1000) # 1000 points in time interval
y =[2,3,8,5]# Generate all heights
# At this point, the array y with all the heights is ready,
# and we need to find the largest value within y.
largest_height = y[0] # Starting value for search
for i in range(1, len(y), 1):
    if y[i] > largest_height:
        largest_height = y[i]
        print(y[i])
print('The largest height achieved was {:g} m'.format(largest_height))




