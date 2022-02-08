a=[1,2,3,4,5,6,7]
i=0
c=[]
while i<len(a):
    j=0
    while j<len(a):
        k= sum([a[i],a[j]])
        if k %2==0:
            c.append(k)
        j=j+1
    i=i+1
print(c)







# even=[]
# while l<len(c):
#     m=0
#     sum=0
#     while m<len(c[l]):
#         sum=sum+c[l][m]
#         if sum%2==0:
#             even.append(sum)
#         m=m+1
#     l=l+1 
#     print(even) 
    # print(sum)      













a=[1,2,3,4,5,6,7]
i=0
c=[]
while i<len(a):
    j=0
    sum=a[i]
    while j<len(a):
        k=[a[i],a[j]]
        sum=sum+a[j]
        # c.append(k)
        j=j+1
    i=i+1
print(sum)                                                                                                                            




