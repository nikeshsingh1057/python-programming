
#input in dictionary
a={}
size=int(input())
for i in range(0,size):
    key=input()
    value=input()
    #a.update({key:value})
    a[key]=value    #both are working
print(a)

