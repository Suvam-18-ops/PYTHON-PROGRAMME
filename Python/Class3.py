Using match-case (Python 3.10 and above)
________________________________________________________
# Only works in Python 3.10 or newer
choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Case 1: Add")
    case 2:
        print("Case 2: Subtract")
    case 3:
        print("Case 3: Multiply")
    case _:
        print("Invalid choice")


#wap take two no from keyboard enter your choice 1.add 2.sub 3.mult 
print("enter two number ")
no1=int(input())
no2=int(input())
print("enter your choice\n1.add\n2.sub\n3.mult ")
ch=int(input())
match ch:
	case 1:print("sum=",no1+no2)
	case 2:print("sub=",no1-no2)
	case 3:print("mult=",no1*no2)
	case _:print("invalid choice ")




print("Enter a number:")
num = int(input())

print("1. Check Even")
print("2. Check Odd")
choice = int(input("Enter your choice: "))

match choice:
    case 1:
        if num % 2 == 0:
            print("Even number")
        else:
            print("Not Even")
    case 2:
        if num % 2 != 0:
            print("Odd number")
        else:
            print("Not Odd")
    case _:
        print("Invalid choice")



print("Enter two numbers:")
a = int(input())
b = int(input())

print("1. Find Maximum")
print("2. Find Minimum")
choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Maximum =", max(a, b))
    case 2:
        print("Minimum =", min(a, b))
    case _:
        print("Invalid choice")




ch = input("Enter a character: ").lower()

print("1. Check Vowel")
print("2. Check Consonant")
choice = int(input("Enter your choice: "))

match choice:
    case 1:
        if ch in 'aeiou':
            print("Vowel")
        else:
            print("Not a vowel")
    case 2:
        if ch.isalpha() and ch not in 'aeiou':
            print("Consonant")
        else:
            print("Not a consonant")
    case _:
        print("Invalid choice")






print("Enter two numbers:")
a = int(input())
b = int(input())

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Addition =", a + b)
    case 2:
        print("Subtraction =", a - b)
    case 3:
        print("Multiplication =", a * b)
    case 4:
        if b != 0:
            print("Division =", a / b)
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid choice")








marks = int(input("Enter your marks (0-100): "))

print("1. Check Grade")
choice = int(input("Enter your choice: "))

match choice:
    case 1:
        match marks:
            case _ if marks >= 90: print("Grade: A")
            case _ if marks >= 75: print("Grade: B")
            case _ if marks >= 60: print("Grade: C")
            case _ if marks >= 40: print("Grade: D")
            case _ if marks >= 0: print("Grade: F")
            case _: print("Invalid marks")
    case _:
        print("Invalid choice")



looping
_________________
some statement repeated continously then you choose loop.


print("hi")
print("hi")
print("hi")
print("hi")
print("hi")



print("A")
print("B")
print("C")
print("A")
print("B")
print("C")
print("A")
print("B")
print("C")



i=1
print(i)
i=i+1
print(i)
i=i+1
print(i)
i=i+1
print(i)
i=i+1
print(i)
i=i+1


using looping we write that repeated stmt only once inside the loop body part


There are 2 types
(1)while
(2)for in

every loop there are 3 section
(1)start value /initlizationn
(2)stop value /condtion
(3)step value /update /inc/dec

while loop syntax
____________________

initlization
while condtion:
	repeated stmt write once
	inc/dec


#wap display hi msg 5 times

i=1
while i<6:
	print("hi")
	i=i+1  #i+=1


#wap display A B C 3 times

i=1
while i<4:
	print("A")
	print("B")
	print("C")
	i=i+1
#wap display 1 to 5
i=1
while i<6:       #i<=5    #i!=6
	print(i)
	i=i+1

#wap display 10 to 20
i=10
while i<21:   #i<=20   #i!=21
	print(i)
	i=i+1

#wap display 5 to 1
i=5
while i>0:    # i>=1     #i!=0 
	print(i)
	i=i-1
#wap display 20 to 10
i=20
while i>9:   #i!=9  #i>=10
	print(i)
	i=i-1


print("A")
i=1
while i<5:
	print("B")
	i=i+1
	print("C")
print("D")
print(i)
o/p:
A
B
C
B
C
B
C
B
C
D
5

continue:
it is keyword.
it is used to continue the loop .
every language every loop last statement continue.

print("A")
i=1
while i<5:
	print("B")
	i=i+1
	print("C")
	continue #by default
print("D")
print(i)
o/p:
A
B
C
B
C
B
C
B
C
D
5




print("A")
i=1
while i<5:
	print("B")
	i=i+1
	continue
	print("C")
print("D")
print(i)

i=1,2,3,4,5
o/p:
A
B
B
B
B
D
5




print("A")
i=1
while i<5:
	print("B")
	i=i+1
	if i>=3:
		continue
	print("C")
print("D")
print(i)

i=1,2,3,4,5
o/p:
A
B
C
B
B
B
D
5





break:
it is keyword.
it is used stop the loop .

print("A")
i=1
while i<5:
	print("B")
	i=i+1
	print("C")
	break
print("D")
print(i)
o/p:
A
B
C
D
2



print("A")
i=1
while i<5:
	print("B")
	i=i+1
	break
	print("C")
print("D")
print(i)

i=1,2
o/p:
A
B
D
2




print("A")
i=1
while i<5:
	print("B")
	i=i+1
	if i>=3:
		break
	print("C")
print("D")
print(i)

i=1,2,3
o/p:
A
B
C
B
D
