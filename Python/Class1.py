literal/constant/data
_____________________
integer literal    any whole number  5,-7,23
float/real number   any decimal value  3.7 -4.5
string              'a' "a" '''a''' """a"""
bool                 True False
complex               2+3j  4-5j

5
5.0
'5'
"5"
5+0j

print(): it is predefined function.
it is used to display output on monitor or console

print()

print(end="\n",sep="")

every print function inside end="\n" sep=" "


print("hi")
print("bye")

o/p:
hi
bye


print("hi",end="\n")
print("bye")

o/p:
hi
bye

print("hi",end="#")
print("bye")
o/p:
hi#bye


print("muna")
print(1)
print(90.50)
o/p:
muna
1
90.50


print("muna",1,90.50)
o/p:
muna 1 90.50


print("muna",1,90.50,sep=" ")
o/p:
muna 1 90.50

print("muna",1,90.50,sep="#")
o/p:
muna#1#90.5


print("muna",1,90.50,sep="\n")
o/p:
muna
1
90.5

print("A","B","C")
print("D","E")
o/p:
A B C
D E


esacpe sequence
____________________
\n
\t
\b
\r
\\
\"

print("AB\nCD")
o/p:
AB
CD

print("AB\tCD")
o/p:
AB  CD


print("india\bo")
print("india\b\b\bo")
print("hello\b\b\b\b\bindia")
print("hello\rindia"

o/p:
indio
inoia
india
india



print("\\")
o/p:
\

print("\\\\")
o/p:
\\


print("\\n")
o/p
\n




print("\\n\\\\n\n\\n")

o/p:
\n\\n
\n



#wap display any integer realno and string value
print(35,5.7,"hi")

identifier:
it is userdefined word.
This word is used to name of variable,classname functionname,...
rule:
(a)it consist of
a to z
A to Z
0 to 9
_
(b)not start with digit

(c)space not allow

(d)case senistive

(e)predefined not allow  (35 keyword  if else )

identify the identifier
______________________

aBd3   v
a#3    iv
a5     v
5a     iv
a b     iv
a_b     v
_ab     v
if      iv
IF       v(not recommand )



import keyword
print(len(keyword.kwlist))
print(keyword.kwlist)



"""
C:\Users\HP\Desktop\pythonprogramdec>py test7.py
35
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

C:\Users\HP\Desktop\pythonprogramdec>

"""
variable:
it is memory location  name where store and retrive data.
variable name must valid identifier.

datatype:
it tells the compiler your variale store which type data.

other datatype
_______________
list
tuple
set
dict


.....

How to create variable and initlization variable
_____________________________________________________
in c ,c++ ,java

datatype variablename;
variablename=constant
in python
__________

variablename=constant
a=10
c=12.34
d="hi"


type():it is a predefined function.
it is used check your variable constant express which type.

a=10
c=12.34
d="hi"
print(type(a))
print(type(c))
print(type(d))
print(type(5))

o/p:
<class 'int'>
<class 'float'>
<class 'str'>
<class 'int'>

all primitive(inbulid datatype) are immutable
________________________________________________

id(): it is predefined function . it is used display the refernce of variable,constant,function,..

a=10
print(id(a),a)
a=20
print(id(a),a)
b=10
print(id(b),b)

"""
140732899976264 10
140732899976584 20
140732899976264 10

"""

single line initlization more variable
______________________________________

a,b,c=10,12.34,"hi"
print(a,b,c)

o/p:
10  12.34  hi


a=10,12.34,"hi"
print(type(a))
print(a)


o/p:
<class 'tuple'>
(10, 12.34, 'hi')





grammer
______________
a=20
print("a")
print(a)
print("a+3")
print(a+3)


o/p:
a
20
a+3
23




a=10
print("a")
print(a)
print("a+3")
print(a+3)


o/p:
a
10
a+3
13

#initlize two integer number add and mult display the all the value
a=10
b=20
print("first no=",a)
print("second no=",b)
print("add=",a+b)
print("mult=",a*b)

o/p:
"""
first  no=10
second no=20
add=30
mult=200
"""

#initlize rectangle length  breadth display length breadth area and perimetr

L=5
B=7
print("length=",L)
print("breadth=",B)
print("area=",L*B)
print("perimetr=",2*(L+B))

or

L=5
B=7
print("length=",L)
print("breadth=",B)
ar=L*B
print("area=",ar)
pr=2*(L+B)
print("perimetr=",pr)


nm="muna";
r=1
m=90.50
print("my name is ",nm,"his rollno ",r," mark=",m)


"""
my name is muna ,his rollno 1  mark=90.50

"""





typecasting
______________
a="10"
b=a
print(type(a),type(b))
print(b*3)


o/p:
<class 'str'> <class 'str'>
101010


string convert to integer
_____________________________

a="10"
b=int(a)
print(type(a),type(b))
print(b*3)

o/p:
<class 'str'> <class 'int'>
30



a="10.45"
b=int(a)
print(b)

o/p:
error
e"C:\Users\HP\Desktop\pythonprogramdec\test13.py", line 2, in <module>
    b=int(a)
      ^^^^^^
ValueError: invalid literal for int() with base 10: '10.



a="10.45"
b=float(a)
print(b)
print(type(b))

o/p:
10.45
<class 'float'>

a=12.34
b=int(a)
print(a,b)

o/p:
12.34 12

int convert to string
______________________

a=10
b=str(a)
print(type(a),type(b))
print(a*3)
print(b*3)


a="10"
b="20"
c=a+b
print(c)


o/p:
1020



a=int("10")
b=int("20")
c=a+b
print(c)

o/p:
30


a="10"
b="20"
c=int(a+b)
print(c+3)

o/p:
1023




a=30
b=40
s=a+b
print("sum=",s)


o/p:
sum=70

Here data is modify every time save and compile
solve this program take input from keyboad

input()
____________
it is a predefined function take input from keyboad in program runtime.
by default it takes string type.

#wap take string from keyboad and display it
print("enter a string ")
nm=input()
print("vaule=",nm)

C:\Users\HP\Desktop\pythonprogramdec>py test13.py
enter a string
muna das
vaule= muna das

C:\Users\HP\Desktop\pythonprogramdec>py test13.py
enter a string
kuna das
vaule= kuna das


input() : it take one argument that must be string type.

#wap take string from keyboad and display it
nm=input("enter a string ")
print("vaule=",nm)

o/p:

C:\Users\HP\Desktop\pythonprogramdec>py test13.py
enter a string muna
vaule= muna
C:\Users\HP\Desktop\pythonprogramdec>py test13.py
enter a string kuna
vaule= kuna



#wap take string from keyboad and display it
nm=input("enter a string\n")
print("vaule=",nm)



#wap take two integer from keyboad and add it
print("enter integer number ")
no1=input()
  print("enter another integer number ")
no2=input()
s=no1+no2
print("sum=",s)

o/p:
C:\Users\HP\Desktop\pythonprogramdec>py test13.py
enter integer number
10
enter another integer number
20
sum= 1020



#wap take two integer from keyboad and add it
print("enter integer number ")
no1=int(input())
print("enter another integer number ")
no2=int(input())
s=no1+no2
print("sum=",s)


"""
C:\Users\HP\Desktop\pythonprogramdec>py test13.py
enter integer number
10
enter another integer number
20
sum= 30

"""


print("enter rectangle length and breadth")
L=int(input())
B=int(input())
print("length=",L)
print("breadth=",B)
ar=L*B
print("area=",ar)
pr=2*(L+B)
print("perimetr=",pr)


o/p:
enter rectangle length and breadth
7
8
length= 7
breadth= 8
area= 56
perimetr= 30





#wap take student name rollno mark keyboad  and dispaly it
print("enter name rollno and mark ")
nm=input()
r=int(input())
m=float(input())
print("name=",nm)
print("rollno=",r)
print("mark=",m)

"""
C:\Users\HP\Desktop\pythonprogramdec>py test13.py
enter name rollno and mark
m das
1
90.50
name= m das
rollno= 1
mark= 90.5
"""



print(pow(2,3))
import math
print(pow(2,3))
print(math.pi)
print(math.pow(2,3))



wap take a student 4 mark from keyboad dispaly all mark
totalmark and avaerage mark

wap take square side formkeyboad dsipaly side area and perimeter

wap take circle radius from keyboad display radius arae and perimetr


convert to f  to c

conver c to f

wap find the simple interset

wap take eme sarly from keyboad  da=30% hra=20% then
display basic sal da hra and total sal







operator
_________

operator is a symbole that operate the operand.
operand may be varibale constant and expression

unary operator :
it operates one operand .
-5

binary operator :
it operates two operand:
a+b
5*6

ternary operator :
it operates three operand.
in python no ternary operator

?   :

precdence:
it is a table.
it decide which operator evaluate first.

associtive:

more than operator same precdence 
same operator more than in expression
it may be evalute 

left to right 
right to left

*  /  %  //  2  L to R
+ -         3

arithmethic operator
_________________

**  power           10**3    1000      precdence  2     right to left
/   exactly division  10/3     3.33333   precedence 3     Left to right
//  floor  division  10//3    3            "                 "
%    module            10%3    1          "                   "
*     mult              10*3   30         "                  "
+     binary plus       10+3   13         precedence 4       "

-     binary  plus      10-3     7           "               "

unary + -    precdence    2      


precdence
_____________
10+3*2**3


10+3*8
10+24
34


Left to right
_________

10//3*5%2
3*5%2
15%2
1


10*3//4*2
30//4*2
7*2
14



right to left
____________

2**3      
8


2**3**2    
2**9
512




10+5//2
12


10+5/2
12.5






display first digit
_____________________

1258//1000      1
476//100        4
34//10            3
56//10              5

display last digit
_____________________

1258%10     8
476%10       6
34%10       4
56%10       6



last digit delete

_____________________
1258//10      125
476//10       47
34//10        3
56//10         5


a=3
b=10
c=2
a=a+4
b=b//c
c=a+b
print(a,b,c)


o/p:

7 5 12


a=3
b=10
c=2
a=a+4
b=b//c
a+b
print(a,b,c)
o/p:
7 5 2


a=3
print(a+2)
print(a)

o/p:
5
3

a=3
a=a+2
print(a)

o/p:
5


a=3
print(a=a+2)
print(a)

o/p:
error

valid in java c,c++
5
5

unary + - operator
________________

a=5
b=-a
print(a,b)
o/p:
5 -5


add two no without using + operator
________________________________
a=5
b=7
c=a- -b
print("sum=",c)


o/p:
12


increment(++) and decrement(--) operator not avaliable in python.


a=5
++a
print(a)

o/p:
5

in java  c, c++
o/p:
6


a=5
a=a+1
print(a)
o/p:
6


a=5
a+=1
print(a)
o/p:
6



relation operator
_____________
<    lessthan
>    greaterthan
<=   lessthanequal
>=
==   is equal
!=

after compare result true or false

3<5    True
3>5     False
3<=3    True
2<=3    True
4<=3     False
3>=3     True
4>=3  True
4>5    False
3==3     True
3==4     False
3!=4       True

10<20<30    True                    in java error

10<50<30    False

2<3==3>2    True   


print(2<3==3>2)
print(2<3==5>2)

True
False


logical or short circut operator
_________________________________
combine two realtion operator
or   
and 
not

    or 
op1     op2      result
True    True      True
True    False     True
False    True     True
False    False     False

print(True or False)  #True

if first operand is true  second operand not checking.
if first operand  is false  second operand must checking
any nonzero value    true 

3 or 5    3  print(3 or 5)
0 or  5   5
3 or 0    3
0 or 0    0

a=3 
b=5
print(a>2 or b>9) 
print(a<2 or b>9) 
print(a>2 or b<9) 
print(a<2 or b<9) 
o/p:
True
False
True
True


and
op1     op2      result
True    True      True
True    False     False
False    True     False
False    False     False

print(True and False)  #False

if first operand is true  second operand must checking.
if first operand  is false  second operand not checking
any nonzero value    True 

3 and 5    5
0 and  5   0
3 and 0    0
0 and 0    0

a=3 
b=5
print(a>2 and b>9) 
print(a<2 and b>9) 
print(a>2 and b<9) 

o/p:
False
False
True





not 
____


operand   resulet

True       False
False       True


not True    False
not False   True

print(not True)
print(not False)
print( not 5)
print(not not 5)

o/p:

False
True
False
True


identity operator
____________________
is      compare reference
is not

==    compare value

a=10
b=10
c=20
print(a is b)
print(a is c)
print(a is not c)
print(a==b)

o/p:
True
False
True
True

a=[10]
b=[10]
c=[20]
print(a is b)
print(a is c)
print(a is not c)
print(a==b)


o/p:
False
False
True
True


membership operator (in ,not in)

print("n" in "india")  #True
print("ndi" in "india")  #True
print("x" in "india")  #False
print("x" not in "india")  #True
print(10  in [5,7,10,12,34])  #True
print(30  in [5,7,10,12,34])  #False
print(30  not in [5,7,10,12,34])  #True








assginment  operator

  vname =vname/constant/expression
  a=10
  b=20
  10=a  invalid
  10=20  invalid
  a+b=30  invalid

swapping two no using 3rd variable

a=10
b=20
temp=b
b=a
a=temp
print(a,b)

o/p:
20 10


swapping two no without using  3rd variable
a=10
b=20
a=a+b
b=a-b
a=a-b
print(a,b)
or
a=10
b=20
a=a*b
b=a//b
a=a//b
print(a,b)
or
a=10
b=20
a=a^b
b=a^b
a=a^b
print(a,b)



a=10
b=20
a,b=b,a   #(only python)
print(a,b)



compund assginment operator
____________________________

+=
-=
*=
/=
%=
//=
**=
&=
|=
^=
<<=
>>=

a+=3    a=a+3
b*=3   b=b*3

10+=2    error   10=10+2

a+=b*=c+=2   error  (in python)     valid c c++ java

#wap take student name rollno and mark display it
print("enter student name rollno and mark ")
nm=input()
r=int(input())
m=float(input())
print("name=",nm)
print("rollno=",r)
print("mark=",m)
o/p:
enter student name rollno and mark
muna das
1
90.50
name=muna das
rollno=1
mark=90.50

#wap take rectangle length and breadth from keyboard displAY LENGTH 
#breadth  area and perimeter.
print("enter rectagle length ")
L=float(input())
print("enter rectagle breadth ")
B=float(input())
ar=L*B
pr=2*(L+B)
print("length=",L)
print("breadth=",B)
print("area=",ar)
print("perimeter=",pr)

o/p:
enter rectangle length
3.5
enter rectangle breadth
4.5
length=3.5
breadth=4.5
area=
perimeetr=


#simple interset
#sal da ta