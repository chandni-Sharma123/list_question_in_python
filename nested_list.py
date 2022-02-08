a=[1,2,[33,2,11,5,[6,7,8],[1,2,3,4],9],22,[2,4,5]]
i=0
l=[]
while i<len(a):
	if type(a[i])==type([]):
		j=0
		while j<len(a[i]):
			if type(a[i][j])==type([]):
				k=0
				while k<len(a[i][j]):
					l.append(a[i][j][k])
					k+=1
			else:
				l.append(a[i][j])
			j+=1
	else:
		l.append(a[i])
	i+=1
print(l)