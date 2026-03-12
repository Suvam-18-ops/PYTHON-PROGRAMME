c=input("Enter a Character")
s=ord(c)
if (s>=65 and s<=90):
	print(chr(s+32))
if (s<65 and s>90):
	print(chr(s))
