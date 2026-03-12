a = int(input("Enter the number: "))

if a < 0:
    a = -a

if a // 10 == 0:
    print("Single Digit")
else:
    print("More than one digit")