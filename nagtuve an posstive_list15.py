# a=[2, -7, 5, -64, -14]
a=[-12, 14, 95, 3]

i=0
count1=0
count2=0
while i<len(a):
    if a[i]>0:
        count1=count1+1
    else:
        count2=count2+1
    i=i+1
print("pos","=",count1,",","nag","=",count2)
# print(count2,"nag")
