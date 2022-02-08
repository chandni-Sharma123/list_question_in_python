list=[1, 2, 2, 5, 8, 4, 4, 8]
c=[]
i=0
while i<len(list):
    if list[i] not in c:
        c.append(list[i])
    i=i+1  
print(c)  