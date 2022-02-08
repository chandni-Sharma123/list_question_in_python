a=[34.67, 12, -94.89, 'Python', 0, 'C#']
i=0
c=[]
v=[]
while i<len(a):
    if type(a[i])==int:
        c.append(a[i])
    if type(a[i])==float:
        v.append(a[i])
  
    i=i+1
print(c,"int")
print(v,"float")



# a=[1,2,3,4,5]
# i=0
# while i<len(a):
#     j=(a[i])
#     i=i+1
#     print(j)