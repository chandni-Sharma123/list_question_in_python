# list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
# c=[]
# i=0
# while i<len(list):
#     if list[i] not in c:
#         c.append(list[i])
#     i=i+1  
# print(c)  


# list=[4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
# c=[]
# i=0
# while i<len(list):
#     if list[i] not in c:
#         c.append(list[i])
#     i=i+1
# print(c)


# list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
# c=[]
# d=[]
# i=0
# while i<len(list):
#     if list[i]==4:
#         c.append(list[i])
#     elif list[i]==3:
#         d.append(list[i])
#     i+=1
# s=c+d
# print(s)




   
    



list = [3,4,3,5,8,5,4,7]
i=0
c=[]
while i < len(list):
    j=i+1
    while j<len(list):
        if list[i]==list[j]:
            # print(list[i][j])
            c.append(list[i])
        j=j+1
    i+=1
print(c)




  


















