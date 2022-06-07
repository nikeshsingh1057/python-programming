
# delete dublicat value form dictionary
dict1={8:90,7:90,23:90}
dict2={}
temp=[]
for i in dict1:
    if dict1.get(i) not in temp:
        temp.append(dict1.get(i))
        dict2.update({i:dict1[i]})
print(dict2)
