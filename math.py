import math
def quad(a,b,c):
    if a==0:
        print("invalid")
        return -0
    d=b*b-4*a*c
    if d>0:
        print("root are real and distint")
        print((-b+math.sqrt(d))/(2*a))
        print((-b-math.sqrt(d))/(2*a))
    elif d==0:
        print("root are distint")
        print(-b/(2*a))
    elif d<0:
        print("root are imagionary")
        print(-b/(2*a),"+ i",math.sqrt(abs(d))/(2*a))
        print(-b/(2*a),"- i",math.sqrt(abs(d))/(2*a))
print(quad(2.3,4,5.6))



