
# to capatalize key only in dictionry 
dict1={}
n=int(input())
for i in range(0,n):
    key=input()
    value=input()
    cap=key.upper()         #to capatilize key only
    dict1[cap]=value
print(dict1)
    

