# i=1
# j=1
# while(i<=4):
# 	while(j<=((i*(i+1))/2)):
# 		print(j,end=" ")
# 		j+=1
# 	i+=1
# 	print( )	
 #or
for i in range(1,5,1):
    for j in range(0,i,1):
    	print(((i*(i-1))//2)+j+1,end=" ")
    print()	