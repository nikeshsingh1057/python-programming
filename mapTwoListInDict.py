
# map two list in dictionary
lis1 =  ['mango', 'pear', 'apple','papaya'] # treat as key
lis2 = [90, 78, 110, 60]              # treat as value
dic={}
for i in range(0,len(lis1)):
    key=lis1[i]
    val=lis2[i]
    dic.update({key:val})           # if we add {val} than value me bhee ye print hoga.
print(dic)

