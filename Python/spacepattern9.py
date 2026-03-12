c=0
for i in range(4,0,-1):
	for j in range(1,i+1,1):
		print(j,end="")
	for j in range(1,c+1,1):
	    print(end=" ")
	for j in range(i,0,-1):
		print(j,end="")
	c=c+2
	print()    