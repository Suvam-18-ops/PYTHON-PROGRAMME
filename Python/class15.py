oops
____________________
#wap store one student name rollno and mark display it
name="muna"
r=1
mark=90.50
print("my name=",name)
print("my rollno=",r)
print("my mark=",mark)

o/p:
my name=muna
my rollno=1
my mark=90.50


#wap store two student name rollno and mark display it

name="muna"
r=1
mark=90.50
print("my name=",name)
print("my rollno=",r)
print("my mark=",mark)
name="kuna"
r=2
mark=80.50
print("my name=",name)
print("my rollno=",r)
print("my mark=",mark)


o/p:
my name=muna
my rollno=1
my mark=90.50
my name=kuna
my rollno=2
my mark=80.50


name="muna"
r=1
mark=90.50
name="kuna"
r=2
mark=80.50
print("my name=",name)
print("my rollno=",r)
print("my mark=",mark)

o/p:
my name=kuna
my rollno=2
my mark=80.50

here first  student data loss

if we store 2 student data  requried 2 name 2 rollno and 2 mark


name="muna"
r=1
mark=90.50
name1="kuna"
r1=2
mark1=80.50
print("my name=",name)
print("my rollno=",r)
print("my mark=",mark)
print("my name=",name1)
print("my rollno=",r1)
print("my mark=",mark1)


o/p:
my name=muna
my rollno=1
my mark=90.50
my name=kuna
my rollno=2
my mark=80.50


if we store 100 student data  requried 100 name 100 rollno and 100 mark
correct 
this type program is not good  solve these program using oops.

class
object
constructor
destructor
inheritance
polymorphism
abstrcation


how to define class
__________________

class classname:
	related data and method
	....
	.....
	constructor
	destructor
	method

how to create object
_______________
classname(args)   # object creation    nameless object

objectrefernce=classname(args)



How to acess object data and method
____________________________________
objectrefernce.data
objectrefernce.method(args)



example
_______________
class Student:
	pass
s=Student()


o/p:
{}


class Student:
    pass
s=Student()
s.name="muna"
s.rollno=1
print(s.__dict__)

o/p:
{'name': 'muna', 'rollno': 1}



class Student:
    pass
s=Student()
s.name="muna"
s.rollno=1
print(s.__dict__)
s1=Student()
s1.name="kuna"
print(s1.__dict__)

o/p:
{'name': 'muna', 'rollno': 1}
{'name': 'kuna'}



class Student:
    name="#"   #class variable   common for all object
    rollno=0   # class variable 
s=Student()
print(s.__dict__)  # { }
print(Student.__dict__)


o/p:
{}
{'__module__': '__main__', 'name': '#', 'rollno': 0, '__dict__': <attribute '__dict__' of 'Student' objects>, '__weakref__': <attribute '__weakref__' of 'Student' objects>, '__doc__': None}


class Student:
    name="#"   #class variable   common for all object
    rollno=0   # class variable 
    def __init__(self):   # constructor   but in java and c++ constructor same as classname
        self.name="muna" # instance variable  object data 
        self.rollno=1
s=Student() # object create  got where constrcutor 
print(s.__dict__)  # { }
print(Student.__dict__)


o/p:
{'name': 'muna', 'rollno': 1}
{'__module__': '__main__', 'name': '#', 'rollno': 0, '__init__': <function Student.__init__ at 0x000001E155CAD300>, '__dict__': <attribute '__dict__' of 'Student' objects>, '__weakref__': <attribute '__weakref__' of 'Student' objects>, '__doc__': None}


class Student:
    clg="iter"
    def __init__(self):   # constructor   but in java and c++ constructor same as classname
        self.name="muna" # instance variable  object data 
        self.rollno=1
s=Student() # object create  got where constrcutor 

print(s.__dict__)  # { }
print(Student.__dict__)
print("my name=",s.name)
print("my rollno=",s.rollno)
print("clg name=",s.clg)
print("clg name better way =",Student.clg)
#print("my name=",Student.name)  error name is part of object 


o/p:
{'name': 'muna', 'rollno': 1}
{'__module__': '__main__', 'clg': 'iter', '__init__': <function Student.__init__ at 0x000001B9ADB0D120>, '__dict__': <attribute '__dict__' of 'Student' objects>, '__weakref__': <attribute '__weakref__' of 'Student' objects>, '__doc__': None}
my name= muna
my rollno= 1
clg name= iter
clg name better way = iter





class Student:
    clg="iter"  #class variable common for all object
    def __init__(self):   # constructor   but in java and c++ constructor same as classname
        self.name="muna" # instance variable  object data 
        self.rollno=1
s=Student() # object create  got where constrcutor 
print("my name=",s.name)
print("my rollno=",s.rollno)
print("clg name=",s.clg)
s1=Student()
print("my name=",s1.name)
print("my rollno=",s1.rollno)
print("clg name=",s1.clg)



o/p:
my name= muna
my rollno= 1
clg name= iter
my name= muna
my rollno= 1
clg name= iter

here all data same  
change all data difffernt input from keyboard 


class Student:
    clg="iter"  #class variable common for all object
    def __init__(self): # constructor but in java and c++ constructor same as classname
        print("enter name and roll number ")
        self.name=input() # instance variable  object data 
        self.rollno=int(input())
s=Student() # object create  got where constrcutor 
s1=Student()
print("clg name=",Student.clg)
print("my name=",s.name)
print("my rollno=",s.rollno)
print("my name=",s1.name)
print("my rollno=",s1.rollno)

o/p:
enter name and roll number
muna
1
enter name and roll number
kuna
2
clg name= iter
my name= muna
my rollno= 1
my name= kuna

class Student:
    clg="iter"  #class variable common for all object
    def __init__(self):   # constructor   but in java and c++ constructor same as classname
        print("enter name and roll number ")
        self.name=input() # instance variable  object data 
        self.rollno=int(input())
    def show(self):
        print("my name=",self.name)
        print("my rollno=",self.rollno)

s=Student() # object create  got where constrcutor 
s1=Student()
print("clg name=",Student.clg)
s.show()
s1.show()

o/p:
a das
1
enter name and roll number
b das
2
clg name= iter
my name= a das
my rollno= 1
my name= b das
my rollno= 2


class Student:
    def __init__(self):   # constructor   but in java and c++ constructor same as classname
        print("enter name and roll number ")
        self.name=input() # instance variable  object data 
        self.rollno=int(input())
    def show(self):
        print("my name=",self.name)
        print("my rollno=",self.rollno)
s=Student() # object create  got where constrcutor 
s1=Student()
s.show()
s1.show()






usig parameter constructor
______________________________

class Student:
    def __init__(self,n,r):   #parameter constructor   but in java and c++ constructor same as classname
        self.name=n # instance variable or  object data 
        self.rollno=r
    def show(self):
        print("my name=",self.name)
        print("my rollno=",self.rollno)
s=Student("muna",1) # object create  go to  constrcutor 
s1=Student("kuna",2)
s.show()
s1.show()


o/p:
my name= muna
my rollno= 1
my name= kuna
my rollno= 2



class Student:
    def __init__(self,n,r):   #parameter constructor   but in java and c++ constructor same as classname
        self.name=n # instance variable or  object data 
        self.rollno=r
    def show(self):
        print("my name=",self.name)
        print("my rollno=",self.rollno)
print("enter student name and rollno")
n=input()
r=int(input())
s=Student(n,r)
s.show()























class Student:
	def __init__(self,n,r,m):
		self.name=n
		self.roll=r
		self.mark=m
	def show(self):
		print("my name=",self.name)
		print("my rollno=",self.roll)
		print("my mark=",self.mark)
s=Student("muna",1,90.50)
s1=Student("kuna",2,80.50)
s.show()
s1.show()

o/p:
enter student name and rollno
a das
3
my name= a das
my rollno= 3







class Student:
    def __init__(self,n,r):   #parameter constructor   but in java and c++ constructor same as classname
        self.name=n # instance variable or  object data 
        self.rollno=r
    def show(s):  #self postion write any name
        print("my name=",s.name)
        print("my rollno=",s.rollno)
print("enter student name and rollno")
n=input()
r=int(input())
s=Student(n,r)
s.show()





o/p:
enter student name and rollno
a das
3
my name= a das
my rollno= 3





class Rectangle:
    def __init__(self,L,B):  
        self.L=L
        self.B=B
    def show(self):  
        print("length=",self.L)
        print("breadth=",self.B)
    def area(self):
        return self.L*self.B 
    def peri(self):
        print("perimeter=",2*(self.L+self.B))
print("enter rectangle length and breadth ")
Len=float(input())
Bre=float(input())
r=Rectangle(Len,Bre)
r.show()
print("area of rectangle=",r.area())
r.peri()



o/p:
C:\Users\LENOVO\OneDrive\Desktop\python9pm>py 1.py
enter rectangle length and breadth
5
7
length= 5.0
breadth= 7.0
area of rectangle= 35.0
perimeter= 24.0