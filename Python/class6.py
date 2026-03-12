Types of parameter
_______

(1)requried parameter
(2)default parameter
(3)keyword parameter
(4)variable length parameter


requried parameter
______
def show(a,b,c,d):
	print(a,b,c,d)

show(10,12.34,"hi",5)
#show(1,5,7) error

o/p:
10 12.34 hi 5



default parameter
______

def  show(a=0,b=0,c=10,d=0):
	print(a,b,c,d)
show(5,"hi")
show(1,5,7,12.34)
show()

o/p:
5 hi 10 0
1 5 7 12.34
0 0 10 0



keyword parameter
______

def  show(a=0,b=3,c=10,d=0):
	print(a,b,c,d)
show(1,5,7,12.34)
show(d=25,c=12,a=5,b=1)
show(c=30)
o/p:
1 5  7  12.34
5 1  12  25
0 3 30 0



variable length parameter
_________
1. *args (Variable-Length Positional Arguments)
The *args syntax allows a function to accept any number of positional arguments. Inside the function, args is treated as a tuple.

def show(*a):
	print(a)
show(10,12.34)
show("hi",1,5.3)

o/p:
(10, 12.34)
('hi', 1, 5.3)


def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

# Calling with a varying number of arguments
print(multiply(2, 3))          # Output: 6
print(multiply(2, 3, 4))       # Output: 24
print(multiply(1, 2, 3, 4, 5)) # Output: 120







def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling with varying keyword arguments
print_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York
print_info(brand="Toyota", model="Corolla", year=2020)
# Output:
# brand: Toyota
# model: Corolla
# year: 2020



def show(*a,b):
	print(a)
show(10,12.34)
show("hi",1,5.3)

o/p:
Traceback (most recent call last):
  File "C:\Users\HP\Desktop\demo.py", line 3, in <module>
    show(10,12.34)
TypeError: show() missing 1 required keyword-only argument: 'b'



def show(b,*a):
	print(a)
show(10,12.34,"hi")
show("bye",1,5.3)
o/p:
(12.34, 'hi')
(1, 5.3)



Combining *args and **kwargs
You can use both *args and **kwargs in the same function. However, *args must come before **kwargs in the function definition.

Example:
def display(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# Calling with both positional and keyword arguments
display(1, 2, 3, name="Alice", age=30)
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 30}






______________________________________________
✅ (1) Required Parameter (Positional Parameter)
📘 Theory:
These are mandatory parameters in a function. You must pass values in the correct order. If any required parameter is missing, Python will raise an error.

def add(a, b):
    print("Sum =", a + b)

add(10, 20)     # Correct
# add(10)       # ❌ Error: Missing required argument 'b'
✅ Key Point:
Order matters.

Cannot be skipped.

✅ (2) Default Parameter
📘 Theory:
You can assign a default value to a parameter. If no value is passed, the default is used. If you pass a value, it overrides the default.

def greet(name, msg="Good Morning"):
    print("Hello", name, "-", msg)

greet("Alice")                  # Uses default message
greet("Bob", "Good Evening")   # Overrides default
✅ Key Point:
Must be at the end of the parameter list.

Used to make parameters optional.

✅ (3) Keyword Parameter
📘 Theory:
You pass the argument by name, not by position. This makes your code more readable and the order of arguments doesn't matter.


def student(name, age, grade):
    print(f"Name: {name}, Age: {age}, Grade: {grade}")

student(age=18, grade="A", name="Rita")  # Order doesn't matter
✅ Key Point:
Improves code clarity.

Useful when there are many parameters.

✅ (4) Variable Length Parameter
Python supports two types of variable-length parameters:

🔹 (a) *args → for variable positional arguments
📘 Theory:
Allows passing any number of positional arguments. It stores them as a tuple.


def total_marks(*marks):
    print("Marks:", marks)
    print("Total:", sum(marks))

total_marks(85, 90)
total_marks(70, 80, 90, 95)
🔹 (b) **kwargs → for variable keyword arguments
📘 Theory:
Allows passing any number of keyword arguments. It stores them as a dictionary.


def profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

profile(name="John", age=22, city="Delhi")
🎯 Summary Table:
Type                 Syntax  Use Case                               Stored As
Required Parameter  a, b        Must be passed in order                 Direct values
Default Parameter   a=10       Optional; use default if not passed       Direct values
Keyword Parameter   name="John" Pass by name for readability          Direct values
Variable-length (*args) *args   Pass many positional values            Tuple
Variable-length (**kwargs)  **kwargs    Pass many keyword values    Dictionary