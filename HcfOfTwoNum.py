
# hcf of two number
a=52
b=56
c=1
while(1):
    if(a%b!=0):
        c=a%b
        a=b
        b=c
    else:
        break
print(c)
        

