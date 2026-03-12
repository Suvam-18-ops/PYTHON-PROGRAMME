Salary=int(input("Enter the Salary"))
da=0
hr=0
total_salary=0
if(Salary>=5000):
	da=0.3*Salary
	hr=0.2*Salary
	total_salary=Salary+da+hr
print("DA:",da)
print("HR:",hr)
print("Total Salary:",total_salary)
