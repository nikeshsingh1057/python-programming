
#use of filter iterator
lis=[45,5,53,34,66,55,47]
def myeven(lis):
    if lis%2==0:
        return True
    return False

li=filter(myeven,lis)
a=list(li)
print(a)
    
