c=input("Enter a Character")
s=ord(c)
if (s>=65 and s<=90):
	print(chr(s+32))
if (s>=97 and s<=122):
	print(chr(s-32))
if(s<65):
	print(chr(s))