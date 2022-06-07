def square(a):
    ev=0
    od=0
    l=[]
    for i in a:
        if i%2==0:
            od+=i*i
        else:
            ev+=i*i
    l.append(ev)
    l.append(od)
    return l
a=list(map(int,input().split()))
print(square(a))
  
    
    