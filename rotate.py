
# rotate string right by user input

a='hello'
b=len(a)
c=int(input())
st=" "
for i in range(b-c,b):
    st=st+a[i]
for i in range(0,b-c):
    st=st+a[i]
print(st)
    
