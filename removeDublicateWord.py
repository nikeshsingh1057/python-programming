
#remove dublicate word form string
a=input()
b=a.split()
lis=[]
for i in b:
    if i not in lis:
        lis.append(i)
lis.sort()
c=" ".join(lis)
print(c)
