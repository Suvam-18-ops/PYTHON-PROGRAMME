k=1
b=0
for i in range(1,5,1):
	for j in range(1,i+1,1):
		if(i%2!=0):
			print(k,end=" ")	
			
		else:
		    print(b,end=" ")
		    b=b-1
		k=k+1  
	b=k+i 	   
	print( )	