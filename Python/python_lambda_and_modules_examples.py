call by value or call by refernce
___________________________________
call by value (value send)  int,float complex string tuple
def update(a):
	print(a)
	a=20

a=10
update(a)
print(a)

o/p:
10
10

call by address(reference send) list set dict
def update(L):
	print(L)
	L.append(40)
L=[10,20,30]
update(L)
print(L)
[10, 20, 30]
[10,20,30,40]
 

function alias
_________________
def show():
	print("show function")
s=show
d=s
show()
s()
d()




lambda function
_____________________

without lambda  find the square
__________________________
def  sq(x):
	y=x*x
	return y
res=sq(5)  #res variable
print(res)


lambda function 
__________________

lambda parameter: expression


res=lambda x:x*x   #res function
print(res(5))




without lambda function
_________________________

def add(x,y):
	return x+y 
res=add(10,20)
print(res)


using lambda
_________________

res=lambda x,y:x+y
print(res(2,3))


module 
___________
it is a python file.
it is collection of function,variable and class



There are 2 types of module.
(1)predefiend module
	sys,random,......
(2)userdefined module
	name must be valid identifier

How to access module in other file
___________________________________
(1)import modulename
(2)import modulename as dupname
(3)from modulename import membername,...
(4)from modulename import *;
mymod.py
__________________
def show():
	print("show function")
def add(no1,no2):
	return no1+no2
x=20


1.py
_________
import mymod
mymod.show()
print(mymod.add(10,20))
print(mymod.x)

2.py
_________
import mymod as m
m.show()
print(m.add(10,20))
print(m.x)


3.py
________
from mymod import show,add,x
show()
print(add(10,20))
print(x)


4.py
_________
from mymod import *
show()
print(add(10,20))
print(x)



show function
30
20

predefined module math use
_________________________
import math
print(math.pi)
print(math.pow(2,3))
print(math.sqrt(16))

3.141592653589793
8.0
4.0


import math as m
print(m.pi)
print(m.pow(2,3))
print(m.sqrt(16))


from math import pi,pow,sqrt
print(pi)
print(pow(2,3))
print(sqrt(16))


from math import *
print(pi)
print(pow(2,3))
print(sqrt(16))



import random as r
print(r.random())
print(round(12.3456,2))
print(round(r.random(),3))

C:\Users\HP\Desktop\pythonpro>py 2.py
0.07210318327459808
12.35
0.787

C:\Users\HP\Desktop\pythonpro>py 2.py
0.22951788312383603
12.35
0.002


import random as r
print(r.uniform(10,20))

C:\Users\HP\Desktop\pythonpro>py 2.py
18.98421799815529
C:\Users\HP\Desktop\pythonpro>py 2.py
19.141364192175452

import random as r
print(r.randrange(10,20))  #any whole number  10 to 20


import random as r
print(r.choice("welcome"))
print(r.choice([4,6,12,45,7]))

C:\Users\HP\Desktop\pythonpro>py 2.py
l
4

C:\Users\HP\Desktop\pythonpro>py 2.py
m
4

C:\Users\HP\Desktop\pythonpro>py 2.py
m
6

import random as r
print(r.sample("welcome",3))
print(r.sample([4,6,12,45,7],4))
C:\Users\HP\Desktop\pythonpro>py 2.py
['w', 'c', 'e']
[4, 45, 6, 7]

C:\Users\HP\Desktop\pythonpro>py 2.py
['c', 'e', 'm']
[12, 6, 45, 7]