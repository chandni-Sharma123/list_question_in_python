a = ["a", "n", "n","t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
b=[]
while i<len(a):
	j=0
	c=[]
	count=0
	while j<len(a):
		if a[i]==a[j]:
			count=count+1
		j=j+1
	c.append(a[i])
	c.append(count)
	if c not in b:
		b.append(c)
	i=i+1
print(b)
