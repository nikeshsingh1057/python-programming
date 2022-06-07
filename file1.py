#use for loop to read line in file.
f=open("mayank.txt","r")
'''for line in f:
    if line[0]=='A'or line[0]=='a':  #if 1st line is "A" or "a" than it will work
        print(line,end='')'''
for line in (f.readlines()[0:]):
    if line[0]=='A'or line[0]=='a': 
        print(line,end=" ")
