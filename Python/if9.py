ch=input("Enter a Character")
s=ord(ch)
if (s>=65 and s<=90):
    ch=chr(s+32)
if (s>=97 and s<=122):
	ch=chr(s-32)
print(ch)	