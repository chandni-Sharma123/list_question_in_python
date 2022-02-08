# a=[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6]]
# # a=[4.8, 5.8, 6.8, 8.0, 11.0]
# # s=float(a)
# b=[]
# i=0
# while i<len(a):
#     sum=0
#     j=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j = j + 1
#     average=sum/len(a[i])
#     i=i+1
#     b.append(average)
# print(b)





a=[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6]]
# a=[4.8, 5.8, 6.8, 8.0, 11.0]
# s=float(a)
b=[]
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        sum=a[i][j]
        j = j + 1
    # average=sum/len(a[i])
    i=i+1
    b.append(sum)
print(b)