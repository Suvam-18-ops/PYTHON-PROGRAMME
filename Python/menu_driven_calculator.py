a=int(input("Enter first number"))
b=int(input("Enter Second number"))
res=0
choice=int(input("Enter 1 for addition ,Enter 2 for substraction, Enter 3 for Multiplication,Enter 4 for division "))
if(choice==1):
	res=a+b
elif(choice==2):
   res=a-b
elif(choice==3):
   res=a*b
elif(choice==4):
   res=a//b 
else:
    print("Invalid choice")     

print(res)       	
