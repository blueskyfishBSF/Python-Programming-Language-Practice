import numpy
t = numpy.linspace(0, 1, 1001)
y = 5*t - 0.5*9.81*t**2
z=y[0]
for i in t:
    if y[i]>z:
        z=y[i]
        if y[i]<z:
            break
        print(z)
