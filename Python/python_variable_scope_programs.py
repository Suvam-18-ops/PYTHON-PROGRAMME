local  variable    vs global variable
_________________________________________

local  variable :
A variable defined  inside function that is known as local variable .
That is visible within that function.
not access other function.

def show():
	a=10 #local variable
	print("local ",a)
def disp():
	#print(a) error
	print("hi")
show()
disp()
#print(a)
o/p:
local 10
hi










global  variable:
A variable defined outside function that is known as global.
that can acees  all function


a=10 #global variable
def show():
	print("global ",a)
def disp():
	print(a)
	print("hi")
show()
disp()
print(a)

o/p:
global 10
10
hi
10



def show():
	print("global ",a)
def disp():
	print(a)
	print("hi")
a=10 #global varible
show()
disp()
print(a)

o/p:
global 10
10
hi
10



a=10 #global
def show():
	a=30 #local
	print("local ",a)
def disp():
	print(a)
	print("hi")
show()
disp()
print(a)

o/p:
local  30
10
hi
10


a=10
def show():
	global a
	a=30
	print(a) #global a display
def disp():
	print(a)
	print("hi")
show()
disp()
print(a)


o/p:
30
30
hi
30




a=10
def show():
	a=30
	print(a) #local 30
	print(locals()['a'])#local 30
	print(globals()['a']) #global 10
	globals()['a']=40	
show()
print(a)

o/p:
30
30
10
40




amount=10000
def deposit(amt):
	global amount
	amount=amount+amt 
	print(amt,"deposit")
def withdraw(amt):
	global amount 
	amount=amount-amt 
	print(amt,"withdraw")
print("balance=",amount)
deposit(3000)
withdraw(6000)
print("balance=",amount)


o/p:
balance= 10000
3000 deposit
6000 withdraw
balance= 7000