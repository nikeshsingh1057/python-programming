#count total no of line

'''f=open("mayank.txt","r")
a=f.readlines()
print(len(a)) '''

#count frequency of each word in file

f=open("mayank.txt","r")
a=f.read().split()
b=[]
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    print(i,":",a.count(i)) 

