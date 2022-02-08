a=[8,1,2,4,5,3,6]
max=0
sec=0
thi=0
i=0
while i<len(a): 
    if a[i]>max:
        thi=sec
        sec=max
        max=a[i]
    elif a[i]>sec:
        thi=sec
        sec=a[i]
    elif a[i]>thi:
        thi=a[i]
    i=i+1
print(max)
print(sec)
print(thi)
    