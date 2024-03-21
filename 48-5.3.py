import sympy as sym
import math
import numpy as np
import matplotlib.pyplot as plt
from math import pi
x=sym.symbols("x")
A=sym.limit(sym.sin(x),x,0)
F=sym.lambdify([x],A)
print("{}".format(A))

T=np.linspace(-(pi),pi,100)
K=np.sin(T)
plt.plot(T,K,'b')
plt.show()

