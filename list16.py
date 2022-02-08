a=[5, 6, [], 3, [], [], 9]
i=0
c=[]
while i<len(a):
    if type(a[i])==int:
        c.append(a[i])
    i=i+1
print(c)