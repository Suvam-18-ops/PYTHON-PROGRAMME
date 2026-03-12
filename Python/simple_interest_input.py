def SIcal():
	p=float(input("Enter the Principal Value:"))
	t=float(input("Enter the time duration:"))
	r=float(input("Enter the rate of intrest:"))
	i=(p*t*r)/100
	return i
print(SIcal())	