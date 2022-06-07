
# short by key in dictionary
a= {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}
b={}
for i in sorted(a):
    b.update({i:a[i]})
print(b)
