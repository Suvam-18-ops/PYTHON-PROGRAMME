module :
it is a python file.
inside module we write function variable class .
There are 2 types of modules
(1)predefined module
   sys
   random
   .
   .
   .


(2)userdefined module
that name must be valid identifier



How to use module
______________________
we can use module 4 way
(1)import modulename
(2)import moulename as dupname
(3)from modulename import member,member
(4)from modulename import *


mymodule.py
______________
def show():
	print("show function")
def add(no1,no2):
	return no1+no2
a=10


first.py
___________
import mymodule
mymodule.show()
print("sum=",mymodule.add(10,20))
print(mymodule.a)

second.py
____________
import mymodule as m
m.show()
print("sum=",m.add(10,20))
print(m.a)

third.py
_______
from mymodule import show,add,a
show()
print("sum=",add(10,20))
print(a)


four.py
_______
from mymodule import *
show()
print("sum=",add(10,20))
print(a)




import math 
print(math.pow(2,3))
print(math.sqrt(16))
print(math.pi)


import math as m
print(m.pow(2,3))
print(m.sqrt(16))
print(m.pi)


from math import pow,sqrt,pi
print(pow(2,3))
print(sqrt(16))
print(pi)



from math import *
print(pow(2,3))
print(sqrt(16))
print(pi)


import math
print(dir(math))



import mymodule
help(mymodule)


import math
help(math.sqrt)



help(str) 



help(len)          # Help on built-in len() function
help(list.append)  # Help on method of list

help()   Interactive help console
help(module)   Show module functions & docs
help(function/class/object)   Show docstring of the specific item



import random
a=random.random()
print(a)
print(round(a,2))


o/p:
C:\Users\LENOVO\OneDrive\Desktop\python9pm>py m8.py
0.5083985005214688
0.51

C:\Users\LENOVO\OneDrive\Desktop\python9pm>py m8.py
0.5934735585298511
0.59


import random
a=random.uniform(10,20)
print(a)
print(round(a,2))


C:\Users\LENOVO\OneDrive\Desktop\python9pm>py m8.py
13.729859114355794
13.73

C:\Users\LENOVO\OneDrive\Desktop\python9pm>py m8.py
11.59057354135729
11.59


import random
print(random.randrange(10,20))


o/p:
C:\Users\LENOVO\OneDrive\Desktop\python9pm>py m8.py
10

C:\Users\LENOVO\OneDrive\Desktop\python9pm>py m8.py
11

C:\Users\LENOVO\OneDrive\Desktop\python9pm>py m8.py
14



import random
print(random.choice([10,20,30,40,50,60]))
print(random.choice("welcome"))

o/p:
C:\Users\LENOVO\OneDrive\Desktop\python9pm>py m8.py
60
o

C:\Users\LENOVO\OneDrive\Desktop\python9pm>py m8.py
30
e


import random
print(random.sample([10,20,30,40,50,60],3))
print(random.sample("welcome",4))

C:\Users\LENOVO\OneDrive\Desktop\python9pm>py m8.py
[50, 40, 60]
['e', 'c', 'e', 'l']

C:\Users\LENOVO\OneDrive\Desktop\python9pm>py m8.py
[60, 40, 50]
['o', 'e', 'w', 'e']

C:\Users\LENOVO\OneDrive\Desktop\python9pm>py m8.py
[20, 10, 40]
['w', 'e', 'c', 'l']

package/libary
__________
package  is collection of subpackage and realted module.

every package is a floder
every folder is not a package

rule
________
inside folder there must be init.py    file
that file must be balnk file.
inside subfloder also init.py





x->y->init.py
blank file nothing write

x->y->mymath.py
____________________
def add(no1,no2):
	return no1+no2
a=10


inside x->

f.py
___________
import y.mymath
print(y.mymath.add(10,20))
print(y.mymath.a)

s.py
__________
import y.mymath as m
print(m.add(10,20))
print(m.a)

t.py
_________
from y.mymath import add,a
print(add(10,20))
print(a)

f.py
________
from y.mymath import *
print(add(10,20))
print(a)