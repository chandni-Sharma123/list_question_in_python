# a=[1234, 122, 1984, 1372, 100]
a=['aabc', 'abc', 'bb', 'a']
i=0
comapre = str(a[0])
comapre= comapre[0]
while i<len(a):
   element = str(a[i])
   if element[0]!=comapre:
      ans = False
      break
   ans = True
   i=i+1
print(ans)

   