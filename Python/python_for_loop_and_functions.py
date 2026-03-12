print("A")
print("B")
print("C")
print("A")
print("B")
print("C")
print("A")
print("B")
print("C")

some statement repeated continously then choose loop concept 

benifits of loop
_________________
write that repeated stmt only once inside the loop body.


for i in range(3):
	print("A")
	print("B")
	print("C")


print("A")
print("B")
print("C")
print("D")
print("A")
print("B")
print("C")
print("E")
print("A")
print("B")
print("C")
print("F")

some statement repeated after sometime then choose function concept 

How to define function
________________________


def  functionname(formal parameter,...):
	function body logic
	return


How to function call
________________________

functionname(actual parameter)


def show():
	print("A")
	print("B")
	print("C")
show()
print("D")
show()
print("E")
show()
print("F")



we can write function program 4 way
_____________________________________
(1)no return value no argument
(2)no returnvalue with argument
(3)return value with no argument
(4)return value with argument




#add two number  without function

print("enter a number ")
no1=int(input())
print("enter another number ")
no2=int(input())
s=no1+no2
print("sum=",s)


(1)no return value no argument   add two number 

def add():
	print("enter a number ")
	no1=int(input())
	print("enter another number ")
	no2=int(input())
	s=no1+no2
	print("sum=",s)
	return
add()



(2)no return value with argument   add two number 

def add(no1,no2):
	s=no1+no2
	print("sum=",s)
	return
print("enter a number ")
no1=int(input())
print("enter another number ")
no2=int(input())
add(no1,no2)



(3)return value with no argument   add two number 

def add():
	print("enter a number ")
	no1=int(input())
	print("enter another number ")
	no2=int(input())
	s=no1+no2
	return s
res=add()
print("sum=",res)


(4)return value with argument   add two number 

def add(no1,no2):
	s=no1+no2
	return s
print("enter a number ")
no1=int(input())
print("enter another number ")
no2=int(input())
res=add(no1,no2)
print("sum=",res)




https://chatgpt.com/share/68b85a56-2804-8008-91ba-cd55a0e43b80