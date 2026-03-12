string
______________
it is collection of char digit special symbole .

example
____________
'a'
"a"
'''a'''
"""a"""
"""hi125"""


s='hi'
print(type(s))
print(s)


o/p:
<class str>
hi

s="hi"
print(type(s))
print(s)


o/p:
<class str>
hi


s='"hi"'
print(s)


o/p:
"hi"


s=" 'hi' "
print(s)


o/p:
'hi'



s="ram das"
print(s)
o/p:
ram das



s='''ram
  das'''
print(s)

o/p:
ram
das



s="""ram
  das"""
print(s)
o/p:
ram
 das



 s="""r'''a'''m
  das"""
print(s)

o/p:
r'''a'''m
  das


name="ram"
print("my name=",name)

o/p:
my name=ram






print("enter a name ")
name=input()
print("my name=",name)



indexing
____________
s="welcome"
print(s[3],s[-4])
#print(s[7])    error  string index out of range
#print(s[-8])    error




explain
____________
0     1     2      3    4     5    6
w     e      l     c    o     m    e
-7     -6    -5    -4   -3   -2   -1



slicing
________________
substring
[start:stop:step]
[start:stop]
[start:]
[:stop:]     by default  start 0     stop  =stop-1     step increase 1
[::]      by default  start 0     stop  =stop-1     step increase 1   











explain
____________
0     1     2      3    4     5    6
w     e      l     c    o     m    e
-7     -6    -5    -4   -3   -2   -1



s="welcome"
print(s[2:5:1])  #lco
print(s[-5:-2:1]) #lco




s="welcome"
print(s[::])  #  welcome
print(s[:])   # welcome
print(s[2:])  #lcome
print(s[2:4]) #lc
print(s[::1]) #welcome
print(s[:10:1]) #welcome
print(s[::2]) #wloe
print(s[:6:2])#wlo



s=["welcome"]
print(s[2:2])    #[]
print(s[5:3])    #[]


0     1     2      3    4     5    6
w     e      l     c    o     m    e
-7     -6    -5    -4   -3   -2   -1

s="welcome"
print(s[::-1])  #emoclew
print(s[6:3:-1]) #emo
print(s[-1:-4:-1]) #emo
print(s[-3:])  #ome
print(s[-3:-1])  #om
print(s[-3:-1:1]) #om
print(s[-3::-1])  #oclew
print(s[-3:-8:-1])  #oclew
print(s[-3:-100:-1])  #oclew
print(s[:-1]) # welcom
print(s[-7::])  #welcome
print(s[-7::-1])  #w



#wap display string individual letter by using sequence
s="welcome"
for i in s:
	print(i)

o/p:
w
e
l
c
o
m
e

#wap count no of char
s="welcome"
print(len(s))

o/p:
7

#wap display string individual letter by using range
s="welcome"
for i in range(0,len(s),1):
	print(s[i])

o/p:
w
e
l
c
o
m
e


#wap display string individual letter by using range
s="welcome"
for i in range(-len(s),0,1):
	print(s[i])

o/p:
w
e
l
c
o
m
e


#wap dispaly string revorder using sequence
s="welcome"
s=s[::-1]
for i in s:
	print(i)
o/p:
e
m
o
c
l
e
w


#wap dispaly string revorder using range
s="welcome"
for i in range(len(s)-1,-1,-1):
	print(s[i])

#wap dispaly string revorder using range
s="welcome"
for i in range(-1,-len(s)-1,-1):
	print(s[i])




	Concatenation Operator (+)
Used to combine two or more strings.
ex1:
________
a = "Hello"
b = "World"
print(a + " " + b)   # Output: Hello World


 2. Repetition Operator (*)

Used to repeat a string multiple times.

text = "Hi "
print(text * 3)      # Output: Hi Hi Hi 

3. Membership Operators (in, not in)

s = "Python Programming"
print("Python" in s)       # True
print("Java" not in s)     # True




4.Comparison Operators (==, !=, <, >, <=, >=)
Used to compare strings based on lexicographical order (dictionary order).

print("apple" == "apple")    # True
print("apple" < "banana")    # True
print("cat" != "dog")        # True

 5. String Slicing ([])
Not an operator, but used like one to access characters or substrings.
s = "Python"
print(s[0])     # P
print(s[1:4])   # yth




6. Escape Characters (\)
Used to insert special characters in strings


print("He said, \"Hello!\"")  # Output: He said, "Hello!"
print("Line1\nLine2")         # New line



a = "Code"
b = "Fun"
print(a + b)        # CodeFun
print(a * 2)        # CodeCode
print("C" in a)     # True
print(a == b)       # False
#print(a+3)   #error


s = "Hello"
s += " World"   # Same as s = s + " World"
print(s)        # Output: Hello World




s = "Hi "
s *= 3          # Same as s = s * 3
print(s)        # Output: Hi Hi Hi 


 2. String Formatting Operators (%)


name = "Alice"
age = 25
ht=5.6
print("Name: %s, Age: %d"  height:%f % (name, age,ht))



# Output: Name: Alice, Age: 25


%s → string
%d → integer
%f → float



 3. String Interpolation (f-Strings) 👉 (Python 3.6+)
name = "Bob"
age = 30
print(f"My name is {name} and I'm {age} years old.")


4. Logical Operators with Strings
Used to check truth values.

print("" and "Hello")     # Output: ""
print("Hi" and "Hello")   # Output: Hello
print(3 and 5)    #5
print(3>0 and 5>0)  #TRue
print("" or "World")      # Output: World


 5. Identity Operators (is, is not)
Check if two string variables point to the same object in memory.


a = "hello"
b = "hello"
print(a is b)   # True (due to string interning in Python)


6. Ternary Operator with Strings

x = 5
result = "Even" if x % 2 == 0 else "Odd"
print(result)   # Output: Odd


operator in string
____________________
s='ram'
print(s*3)
#print(s+3) error
s1="das"
print(s+s1)
print('a' in s1)
print('x' in s1)
s2="abc"
s3="Abc"
print(s2==s3)
print(s2>=s3)
print(s2<=s3)
print(s2!=s3)

ramramram
ramdas
True
False
False
True
False
True



#wap count no char in string
#len():inbulit function count no of char
s="welcome"
print(len(s))
print(len("ok"))
o/p:
7
2

#wap count no char in string  without len() function

s="welcome"
c=0
for i in s:
    c=c+1
print("no of char=",c)





some predefined member function  in string
________________

s="ram is a Good boy"
s=s.title()
print(s)

o/P:
Ram Is A Good Boy


s="ram is a Good boy"
s=s.capitalize()
print(s)


o/p:
Ram is a good boy

s="ram is a Good boy"
s=s.upper()
print(s)
o/p:
RAM IS A GOOD BOY

s="rAM is a Good boy"
s=s.lower()
print(s)
o/p:
C:\Users\HP\Desktop\javascript>py 3.py
ram is a good boy

or
s="rAM is a Good boy"
s=s.casefold()
print(s)
o/p:
ram is a good boy


text = "Straße"

print(text.lower())    # Output: "straße"
print(text.casefold()) # Output: "s



s="rAM is a Good boy"
print(s.swapcase())
print(s)
o/p:
C:\Users\HP\Desktop\javascript>py 3.py
Ram IS A gOOD BOY
rAM is a Good boy





lstrip():   remove space left side 
s=" hi"
print(len(s))
s=s.lstrip()
print(len(s))

o/p:
C:\Users\HP\Desktop\javascript>py 3.py
3
2







rstrip(): remove space right side
s="hi "
print(len(s))
s=s.rstrip()
print(len(s))

o/p:
C:\Users\HP\Desktop\javascript>py 3.py
3
2






strip(): remove space both side
s=" hi "
print(len(s))
s=s.strip()
print(len(s))

o/p:
C:\Users\HP\Desktop\javascript>py 3.py
4
2






s="hi"
print(s)
print(s.center(5))
print(s.center(5,"*"))
print(s.ljust(5,"*"))
print(s.rjust(5,"*"))

o/p:
hi
  hi
hi*
hi***
***hi


s="welcome"
print(s)
print(s.center(5))
print(s.center(5,"*"))
print(s.ljust(5,"*"))
print(s.rjust(5,"*"))
o/p:
welcome
welcome
welcome
welcome
welcome


s="welcome"
print(s)
print(s.center(10))
print(s.center(10,"*"))
print(s.ljust(10,"*"))
print(s.rjust(10,"*"))



o/p:
C:\Users\HP\Desktop\javascript>py 3.py
welcome
 welcome
welcome*
welcome***
***welcome


s="ram is a good boy"
print(s.startswith("r"))
print(s.startswith("ram"))
print(s.startswith("rom"))
print(s.startswith("ram is a good boy"))
o/p:
C:\Users\HP\Desktop\javascript>py 3.py
True
True
False
True





s="ram is a good boy"
print(s.endswith("y"))
print(s.endswith("boy"))
print(s.endswith("box"))
print(s.endswith("ram is a good boy"))

o/p:
True
True
False
True
            
startwith(string,start,stop)


s="ram is a good boy"
print(s.startswith("r",4))
print(s.startswith("is",4))
print(s.endswith("o",4,11))

o/p:
False
True
True



s="ram is a good is boy"
print(s.count("a"))
print(s.count("is"))
print(s.count("x"))

o/p:
C:\Users\HP\Desktop\javascript>py 3.py
2
2
0

s="ram is a good is boy"
print(s.count(" "))
o/p:
5


s="ram is a good is boy"
print(s.index("a"))
print(s.index("m"))
o/p:
C:\Users\HP\Desktop\javascript>py 3.py
1
2



s="ram is a good is boy"
print(s.rindex("a"))
print(s.rindex("m"))
print(s.rindex("x"))
o/p:
C:\Users\HP\Desktop\javascript>py 3.py
7
2
Traceback (most recent call last):
  File "C:\Users\HP\Desktop\javascript\3.py", line 4, in <module>
    print(s.rindex("x"))
          ^^^^^^^^^^^^^
ValueError: substring not found


s="ram is a good is boy"
print(s.find("a"))
print(s.find("m"))
print(s.find("x"))

o/p:

C:\Users\HP\Desktop\javascript>py 3.py
1
2
-1


s="ram is a good is boy"
print(s.rfind("a"))
print(s.rfind("m"))
print(s.rfind("x"))
o/p:
C:\Users\HP\Desktop\javascript>py 3.py
7
2
-1



s="Ab3"
print(s.isalnum())
s1="Ab#3"
print(s1.isalnum())
o/p:
True
False





s="Ab"
print(s.isalpha())
s1="Ab3"
print(s1.isalpha())
o/p:
True
False



s="125"
print(s.isdigit())
s1="125a"
print(s1.isdigit())
o/p:
True
False


s=" "
print(s.isspace())
s1="ram is"
print(s1.isspace())

o/p:
True
False


s="a"
print(s.islower())
s="B"
print(s.islower())

o/p:
True
False



s="a"
print(s.isupper())
s="B"
print(s.isupper())


o/p:
False
True





s="hi"
x=s.encode() #String convert byte
print(type(s),type(x))
print(s,x)
s1=x.decode() #byte convert to string
print(s1)


o/P:
C:\Users\HP\Desktop\javascript>py 3.py
<class 'str'> <class 'bytes'>
hi b'hi'
hi



s="ram is a good boy"
L=s.split()
print(L)

o/p:
C:\Users\HP\Desktop\javascript>py 3.py
['ram', 'is', 'a', 'good', 'boy']


s="ram is a good boy"
L=s.split("i")
print(L)
o/p:
C:\Users\HP\Desktop\javascript>py 3.py
['ram ', 's a good boy']


s="ram is a good boy"
L=s.split()
s1=" ".join(L)
print(s1)
o/p:
ram is a good boy


s="ram is a good boy"
L=s.split()
s1="#".join(L)
print(s1)

o/p:
ram#is#a#good#boy


s="ram is a good boy"
L=s.split("a")
s1="#".join(L)
print(s1)


r#m is # good boy



s="ram is a good boy"
L=s.split("a")
s1="#".join(L)
print(s1)


r#m is # good boy








tit
cap
upper
lowe
case
swap
count
center
ljust
rjust
strim
lstrim
rstrim
replace
index
rindex
find
rfind
statswith
endswith
isalnum
isalpha
isdigit
isspace
islower
isupper
split
join
encode
decode



#wap count no of uppercase in string
s="WelCOme123"
c=0
for i in s:
    if i.isupper():
        c=c+1
print("no of uppercase=",c)

#wap count no of lowercase in string
s="WelCOme123"
c=0
for i in s:
    if i.islower():
        c=c+1
print("no of lowercase=",c)

#wap  count no of digit in string
s="WelCOme123"
c=0
for i in s:
    if i.isdigit():
        c=c+1
print("no of digit=",c)

#wap  count no of vowel 
s="WelCOme123"
vw=0
for i in s:
    if i in "aeiouAEIOU":
        vw=vw+1
print("no of vw=",vw)

#wap    count no of alphabet

s="WelCOme123"
c=0
for i in s:
    if i.isalpha():
        c=c+1
print("no of alp=",c)



#wap   count no of space

s="WelCOme123 boy"
c=0
for i in s:
    if i.isspace():
        c=c+1
print("no of space=",c)

#wap  count no of alp uppercae lowercase no of vowel cons
    no of digit no of space no of sy  no of word .








print("enter a string ")
s=input()
alp,lw,up,vw,co,dg,sp,wd,c,sy=0,0,0,0,0,0,0,0,0,0
for i in s:
    if i.isalpha():
        alp=alp+1
        if i.isupper():
            up=up+1
        else:
            lw=lw+1
        if i in "aeiouAEIOU":
            vw=vw+1
        else:
            co=co+1
    elif i.isdigit():
        dg=dg+1
    elif i.isspace():
        sp=sp+1
    else:
        sy=sy+1
    c=c+1
wd=sp+1

print("total no of char=",c)
print("total no of alp=",alp)
print("total no of vw=",vw)
print("total no of co=",co)
print("total no of upper=",up)
print("total no of lower=",lw)
print("total no of digit=",dg)
print("total no of space=",sp)
print("total no of sy=",sy)
print("total no of word=",wd)




C:\Users\LENOVO\Desktop\pythonprogram>py strt.py
enter a string
ram is a GOOD B1&
total no of char= 17
total no of alp= 11
total no of vw= 5
total no of co= 6
total no of upper= 5
total no of lower= 6
total no of digit= 1
total no of space= 4
total no of sy= 1
total no of word= 5


https://chatgpt.com/share/68c2e866-f2cc-8008-9138-3e244ce6b802