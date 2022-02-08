a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
i=0
count=0
sum=0
c=[]
while i<len(a):
    if a[i]>0:
        count=count+1
        # c.append(count)
    else:
        sum=sum+a[i]
    i=i+1
c.append(count)
c.append(sum)
print(c)