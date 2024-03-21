try:
    a=float(input("your a?"))
    b=float(input("your b?"))
    A=a/b
    print("a/b=",A)
except ZeroDivisionError:
    print('your b is zero!')
except KeyboardInterrupt:
    print("ok,I know you want to stop!")
except:
    print('you should give a number!')


