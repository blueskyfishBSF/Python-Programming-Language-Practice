import sympy as sym
import math
x=sym.symbols("x")
f=sym.atan(x)/(x**2+1)
number1=sym.diff(f,x)
number2=sym.lambdify([x],number1)

print(number1)
print(number2(math.pi/6))


