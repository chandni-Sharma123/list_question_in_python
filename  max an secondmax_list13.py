# a=[2,1,3,43,5,66,7]
# i=0
# max=0
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     i=i+1
# print(max)




a=[12,3,4,8,6,7,9,10]
i=0
max=0
sec=0
while i<len(a):
    if a[i]>max:
        max=a[i]
    i=i+1
j=0
while j<len(a):
    if max>a[j] and a[j] >sec:
        sec=a[j]
    j=j+1
print(max)
print(sec)
