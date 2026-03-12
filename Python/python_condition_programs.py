terNary operator 
_____________________

truepart if condtion else falsepart


#wap take a number from keyboard check no is +ve or -ve
print("enter a number ")
no=int(input())
print("+ve") if no>=0 else print("-ve")



#wap take a number from keyboard check no is even or odd
print("enter a number ")
no=int(input())
print("even number") if no%2==0 else print("odd number")



#wap take salary from  keyboad if salary>=5000 da=30% hra=20%  if salary <5000 
#da=20% hra=10% then display basic salary da hra and totalsal

print("enter basic sal ")
sal=float(input())
da=sal*0.3 if sal>=5000 else sal*0.2
hra=sal*0.2 if sal>=5000 else sal*0.1
totalsal=sal+da+hra
print("basic sal=",sal)
print("da=",da)
print("hra=",hra)
print("total sal=",totalsal)





nested if else statement
____________________________
syn1:

if   c1:
	if c2:
		c2 true block
	else:
		c2 false block


#wap take number from keyboard check no is +ve or -ve  zero no output
print("enter a number ")
no=int(input())
if no!=0:
	if no>0:
		print("+ve")
	else:
		print("-ve")



syn2:

if   c1:
	if c2:
		c2 true block
	else:
		c2 false block
else:
	c1 false block

#wap take number from keyboard check no is +ve  -ve  zero 
print("enter a number ")
no=int(input())
if no!=0:
	if no>0:
		print("+ve")
	else:
		print("-ve")
else:
	print("ZERO")



syn3:
if   c1:
	c1 true block
else:
	if c2:
		c2 true block
	else:
		c2 false block
#wap take number from keyboard check no is +ve  -ve  zero 
print("enter a number ")
no=int(input())
if no==0:
	print("zero")
else:
	if no>0:
		print("+ve")
	else:
		print("-ve")


syn4:
if   c1:
	if c2:
		c2 true block
	else:
		c2 false block
else:
	if c3:
		c3 true block
	else:
		c3 false block

#wap take 3 number from keyboard display bigest number
print("enter three nos")
no1=int(input())
no2=int(input())
no3=int(input())
if no1>=no2:
	if no1>=no3:
		print("first number is biger ",no1)
	else:
		print("third number is biger ",no3)
else:
	if no2>=no3:
		print("second no is biger ",no2)
	else:
		print("third no is biger ",no3)


elif statement
_________________
syn3:
if   c1:
	 c1 true block
elif c2:
	c2 true block
else:
	 false block
where the condtion is true other condtion not checking

#wap take number from keyboard check no is +ve  -ve  zero 
print("enter a number ")
no=int(input())
if no>0:
	print("+ve")
elif  no<0:
	print("-ve")
else:
	print("zero")

#wap take no from keyboard check no is sd dd  td and od using elif
print("enter a number ")
no=int(input())
if no<0:
	no=-no
#check
if no<10:
	print("sd")
elif no<100:
	print("dd")
elif no<1000:
	print("td")
else:
	print("od")
#wap take no from keyboard no is divisble by 5 and 7 only 5 only 7 not divisble 5 and 7
print("enter a number ")
no=int(input())
if no%5==0 and no%7==0:
	print("d by 5 and 7")
elif no%5==0:
	print("only 5")
elif no%7==0:
	print("only 7")
else:
	print("not div by 5 and 7")

#wap take two no from keyboard enter your choice 1.add 2.sub 3.mult 
print("enter two number ")
no1=int(input())
no2=int(input())
print("enter your choice\n1.add\n2.sub\n3.mult ")
ch=int(input())
if ch==1:
	print("sum=",no1+no2)
elif ch==2:
	print("sub=",no1-no2)
elif ch==3:
	print("mult=",no1*no2)
else:
	print("invalid choice ")

3 Program: Area of Square, Rectangle, and Circle
import math
print("Choose a shape to calculate area:")
print("1. Square")
print("2. Rectangle")
print("3. Circle")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    side = float(input("Enter the side of the square: "))
    area = side * side
    print("Area of Square =", area)

elif choice == 2:
    length = float(input  ("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    area = length * breadth
    print("Area of Rectangle =", area)
elif choice == 3:
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius * radius
    print("Area of Circle =", area)

else:
    print("Invalid choice")



print("Enter two numbers:")
no1 = int(input("First number: "))
no2 = int(input("Second number: "))
print("\nEnter an operator (+, -, *, //):")
op = input("Operator: ")

if op == "+":
    print("Result =", no1 + no2)
elif op == "-":
    print("Result =", no1 - no2)
elif op == "*":
    print("Result =", no1 * no2)
elif op == "//":
    if no2 != 0:
        print("Result =", no1 // no2)
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid operator")



✅ Program: Electricity Bill Calculation
Assume the following rates:

Units Consumed	Rate per Unit
0 - 100	₹1.5
101 - 200	₹2.5
201 - 300	₹4.0
Above 300	₹6.0


# Electricity Bill Calculator

units = int(input("Enter total electricity units consumed: "))
bill = 0

if units <= 100: 
    bill = units * 1.5
elif units <= 200:
    bill = (100 * 1.5) + (units - 100) * 2.5
elif units <= 300:
    bill = (100 * 1.5) + (100 * 2.5) + (units - 200) * 4.0
else:
    bill = (100 * 1.5) + (100 * 2.5) + (100 * 4.0) + (units - 300) * 6.0

print("Total Bill = ₹", round(bill, 2))