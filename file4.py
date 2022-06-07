f=open("multiply.txt","w")
t=int(input("enter number to print table:"))
for i in range(1,11):
    table=t*i     # write always take string input so we need to typexast it into string.
    f.write(str(table))
    f.write("\n")

f.close()
