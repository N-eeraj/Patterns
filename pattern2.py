n=int(input('Enter number: '))
for i in range(1,n+1):
	k=n-i
	j=flag=1
	while(j<2*i):
		if(n<=k):
			flag=0
		if(flag==1):
			k+=1
		else:
			k-=1
		print (k,' ',end='')
		j+=1
	print ('\n')
i-=1
while(i>0):
	j=flag=1
	while(j<2*i):
		if(n<=k):
			flag=0
		if(flag==1):
			k+=1
		else:
			k-=1
		print (k,' ',end='')
		j+=1
	print ('\n')
	i-=1
