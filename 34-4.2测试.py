def f(x):
    return x**2
def g(x):
    return 2*x
for x in [1, 5, 6, 9]:
    if x < 5:
        # case 1
        print(f(x))
    elif x == 5:
        # case 2
        print(2*f(x))
    elif x > 5 and x < 8:
        # case 3
        print(f(x+4) + g(x*2) - g(2))
    else:
        # case 4
        y = x + 2
        print(g(y))




