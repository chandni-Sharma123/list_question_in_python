l=[12,67,98,413]
i=0
sum=0
while i<len(l):
    k=l[i]%10
    k1=l[i]//10
    k2=l[i]/10
    sum=k+k1
    print(sum,end=" ")
    i+=1

