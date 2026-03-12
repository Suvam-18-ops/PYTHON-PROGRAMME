List:

list is predefiend   datastrcutre.

insertion  order is preserved.

duplicate element allow.
similar and dismaliar elements
list is mutable.


syntax:
How to create list

L=[]
print(type(L))
o/p:
<class list>


L=[]
L.append(10)
L.append(20)
L.append(30)
print(L)
o/p:
[10,20,30]


if we known data then list initlization in single line.

L=[10,20,30]
print(L)

o/p:
[10,20,30]

L=[10,20.45,"hi"]
print(L)
o/p:
[10,20.45,'hi']


L=list()
print(type(L))
o/p:
<class 'list'>


L=list(range(5))
print(type(L))
print(L)
o/p:
<class 'list'>
[0,1,2,3,4]


L=list("hello")
print(type(L))
print(L)
o/p:
list
['h','e','l','l','o']


s="ram is a good boy"
L=s.split()
print(L)
o/p:
['ram', 'is', 'a', 'good', 'boy']




indexing and slicing

_______________________
L=[10,20,30,40,50]
print(L[2],L[-3])
print(L[1:4:1])
print(L[-4:-1:1])

o/p:
30 30
20 30 40
20 30 40
                                  index   L[index]
                                   0    1    2   3    4      
                                    10  20   30   40  50
                                    -5   -4   -3   -2  -1

 L[start:stop:step]


display all element in list:
_____________________________
way 1:using sequence concept

L=[10,20,30,40,50]
for i in L:
  print(i)
o/p:
here i is element
10
20
30
40
50




way 2:using index concept
range(start,stop,step)
range(start,stop)
range(stop)

here start=0   stop-1     step=1

L=[10,20,30,40,50]
for i in range(0,len(L),1):
  print(L[i])

o/p:
here i is index
10
20
30
40
50


Display all element in backward by using index
___________________________
L=[10,20,30,40,50]

for i in range(len(L)-1,-1,-1):
  print(L[i])

o/p;
50
40
30
20
10


Display all element in backward by using sequnence
L=[10,20,30,40,50]
L1=L[::-1]
for i in L1:
  print(i)

o/p;
50
40
30
20
10

inbulit function
_________
L=[5,9,23,2,0]
print(len(L))
print(max(L))
print(min(L))
print(sum(L))
print(any(L)) #  one nonzero true
print(all(L)) # all nonzero true

o/p:
5
23
0
39
True
False




list operator

L=[5,9,7,2,10]
L[2]=8
del L[1]
print(L)


o/p:
C:\Users\HP\Desktop>py 1.py
[5, 8, 2, 10]




L=[5,9,7,2,10]
L[1:4:]=[15]
print(L)

o/p:
[5, 15, 10]




insert
_
L=[5,9,7,8,10]
L[2:2:]=[10,11,13]
print(L)

o/p:
C:\Users\HP\Desktop>py 1.py
[5, 9, 10, 11, 13, 7, 8, 10]


update
__
L=[5,9,7,8,10]
L[2:3:]=[10,11,13]
print(L)
o/p:
[5, 9, 10, 11, 13, 8, 10]


delete
___
L=[5,9,7,8,10]
del L[2:4]
print(L)

o/p:
[5, 9, 10]




L=[5,9,7,8,10]
print(7 in L)
print(6 in L)
print(6 not in L)


o/p:
C:\Users\HP\Desktop>py 1.py
True
False
True



L1=[5,9,7]
L2=[5,9,7]
print(L1==L2)
print(L1 is L2)


o/p:
True   (==value)
False  (is addrees)


L1=[5,9,7]
L2=[5,8,7]
print(L1==L2)
print(L1 >L2)
print(L1>=L2)


o/p:
False
True
True


L=[2,3,5]
print(L*3)

o/p:
[2,3,5,2,3,5,2,3,5]


L=[2,3,5]
L1=[8,9]
print(L+L1)
o/p:
[2, 3, 5, 8, 9]
list predefied fuction
____________________
append(): insert element last
L=[5,8,12,3,9]
L.append(40)
print(L)

o/p:
[5, 8, 12, 3, 9, 40]




L=[5,8,12,3,9]
L.insert(0,40)
L.insert(6,45)
L.insert(3,35)
L.insert(20,55)
print(L)
print(L[8])
L.insert(-10,34)
print(L[0])
print(L)

o/p:
C:\Users\HP\Desktop>py 1.py
[40, 5, 8, 35, 12, 3, 9, 45, 55]
55
34
[34, 40, 5, 8, 35, 12, 3, 9, 45, 55]

extend:
_______
L=[5,8,7]
L1=[12,34]
L.extend(L1)
print(L)
print(L1)


o/p:
[5, 8, 7, 12, 34]
[12, 34]


L=[5,8,7]
L.extend("hi")
print(L)

o/p:
[5, 8, 7, 'h', 'i']




remove(element):  remove the element

L=[5,8,7,8,12]
L.remove(8)
print(L)
o/p:
[5, 7, 8, 12]




L=[5,8,7,8,12]
L.remove(23)
print(L)
o/p:
Traceback (most recent call last):
  File "C:\Users\HP\Desktop\1.py", line 2, in <module>
    L.remove(23)
ValueError: list.remove(x): x not in list


L=[5,8,7,8,12]
print(L.pop())
print(L.pop())
print(L.pop())
print(L.pop())
print(L.pop())
#print(L.pop()) indexerror
print(L)

o/p:
12
8
7
8
5
[]


L=[5,8,7,8,12]
L.clear()
print(L)

o/p:
[]

L=[5,8,7,8,12]
del L


L=[5,8,7,8,12]
L.reverse()
print(L)

o/p:
[12, 8, 7, 8, 5]



L=[5,9,7,4,12]
L.sort()
print(L)
o/p:
[4, 5, 7, 9, 12]

L=[5,9,7,4,12]
L.sort(reverse=True)
print(L)
o/p:
[12, 9, 7, 5, 4]





L=["muna","kuna","rabi","dadu"]
L.sort()
print(L)
o/p:
['dadu', 'kuna', 'muna', 'rabi']


L=[5,8,7,8,12,8]
print(L.count(8))

o/p:
3


L=[5,8,7,12,8]
print(L.index(8))

o/P
1

L=[5,8,7,6,12,8]
print(L.index(8,3))
o/p:
5


L=[5,8,7]
L[1]=25
print(L)

o/p:
[5,25,7]


assgin list refernce
__________________
L=[5,8,7]
L1=L
L[0]=10
print(L)
print(L1)

o/p:
[10, 8, 7]
[10, 8, 7]



L=[5,8,7]
L1=L.copy()
L[0]=10
print(L)
print(L1)


o/P
[10, 8, 7]
[5, 8, 7]