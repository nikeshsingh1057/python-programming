#adding n nuber of file in python file.
f=open("creat new file.txt","w")
for i in range(0,2):
    a=input()
    f.write(a)
    f.write('\n')  # to change line every time
f=open("creat new file.txt","a")
f.write("apple\n")
f.write("mango")