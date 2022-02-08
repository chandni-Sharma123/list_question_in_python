# list = [6,2,1,2,3]
# c=[]
# i=0

# while i<len(list):
#     if list[i] not in c:
#         c.append(list[i])
#     i=i+1
# k=0 
# Multiple=1
# while k<len(c):
#     Multiple=Multiple*c[k]
#     k=k+1
# print(Multiple)


list = [6,2,1,2,3]
c=[]
i=0

while i<len(list):
    if list[i] not in c:
        c.append(list[i])
    i=i+1
k=0 
Multiple=1
while k<len(c):
    Multiple=Multiple*c[k]
    k=k+1
print(Multiple)
