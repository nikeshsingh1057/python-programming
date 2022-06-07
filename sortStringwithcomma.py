
#sort string with hyphn seperated
a="green-ted-yeadf-bac-abc"
b=a.split("-")
b.sort()
b=" ".join(b)     #to conver list into string
c=""
for i in b:
    if i==" ":
        c=c+"-" 
    else:
        c=c+i 
print(c)
    
