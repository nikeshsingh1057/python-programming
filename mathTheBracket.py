
#match the bracket
def check(a):
    one=0
    two=0
    for i in a:
        if i=='(':
            one+=1 
        elif i==')':
            two+=1 
    if one==two and(one and two!=0):
        return 'ok'
    else:
        return 'bad'
strr=input()
print(check(strr))
