list=[1,2,4,5,7,9,11]
i=1
while i<=11:
	j=0
	while j<len(list):
		if i not in list:
			list.append(i)
			list.sort()
		j=j+1
		i=i+1
print(list)