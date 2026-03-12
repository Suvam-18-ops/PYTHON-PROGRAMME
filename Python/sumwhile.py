a=int(input("Enter  the number"))
soe=0
sod=0
while a>0:
	l=a%10
	if(l%2==0):
		soe+=l
	else:
	    sod+=l
	a=a//10    
print(sod)
print(soe)	    
