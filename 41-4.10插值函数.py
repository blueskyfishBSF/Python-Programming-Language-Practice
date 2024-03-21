t=float(input("your_t?"))
i=int(t)
y=i
print(i)
#(0,4.4)(1,2.0)(2,11.0)(3,21.5)(4,7.5)
def interpolate(t1,y1,t2,y2,t3):
    k=(y2-y1)/(t1-t2)
    b=y1-k*t1
    y3=k*t3+b
    return y3

def find(t4):
    if 0<=t4<=1:
        k=(4.4-2.0)/(0-1)
        b=4.4-k*0
        y3=k*t4+b
        return y3
    elif 1<=t4<=2:
        k=(11.0-2.0)/(2-1)
        b=11.0-k*2
        y3=k*t4+b
        return y3
    elif 2<t4<=3:
        k=(21.5-11.0)/(3-2)
        b=11.0-k*2
        y3=k*t4+b
        return y3
    elif 3<t4<=4:
        k=(11.0-7.5)/(4-3)
        b=11.0-k*2
        y3=k*t4+b
        return y3
    elif t4<0:
        return "error,please remake!"

print(find(2.5))
print(find(3.1))
