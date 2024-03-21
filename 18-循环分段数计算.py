x=0
for i in range (1000,4001,1):
    if int(i)%2==0 and int(i/10)%2==0 and int(i/100)%2==0 and int(i/1000)%2==0:
        x+=1
print(x)




