
# push all zero last in the list
lis=[4,6,2,0,0,0,5,6,0,0,9,8,2]
a=[]
count=0
for i in lis:
    if i!=0:
        a.append(i)
    else:
        count=count+1
for i in range(0,count):
    a.append(0)
print(a)
