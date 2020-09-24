n=int(input('Enter Size: '))
for i in range(1,n+1):
	k=flag=0
	for j in range(1,2*n):
		if(k>=n):
			flag=1
		if(flag==0):
			k+=1
		else:
			k-=1
#		print ('[',i,j,']',' ',end='')
		if(j+i>n+1 and j<n+i-1):
			print ('   ',end='')
		else:
			print (k,' ',end='')
	print ('\n')
