n=int(input('Enter Size: '))
for i in range(1,n+1):
	k=i
	for j in range(1,n+1):
		print (k,' ',end='')
		k+=1
		if(k>n):
			k-=n
	print ('\n')
