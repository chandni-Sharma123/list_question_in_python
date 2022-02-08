#  a=['0', '1', '2', '3', '4']
# s=['red', 'green', 'black', 'blue', 'white']
# d=['100', '200', '300', '400', '500']

# i=0
# c=[]
# while i<len(a):
#     b=(a[i]+s[i]+d[i])
#     c.append(b)
#     i=i+1
# print(c)


# a=['0red100', '1green200', '2black300', '3blue400', '4white500']
   




a=['a','d','s']
b=[3,2,1]
o=str(b)
i=0
while i<len(a):
    d=a[i]+o[i-1]
    print(d)
    i=i+1
