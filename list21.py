# list = [12, 67, 98, 34]
# i=0
# count=0
# while i<len(list):
#     count=count+list[i]
#     i=i+1
#     print(count)



l=[15, 81, 11, 34]

i=0
sum=0
while i<len(l):
    k=l[i]%10
    k1=l[i]//10
    sum=k+k1
    print(sum,end=" ")
    i+=1
