# print maximum word from file.
with open("mayank.txt","r") as f:
    a=f.read().split()
    l=0
    for i in a:
        if len(i)>l:
            l=len(i)
    b=[]
    for i in a:
        if len(i)==l:
            b.append(i)
    print(b)
    

            
            
    