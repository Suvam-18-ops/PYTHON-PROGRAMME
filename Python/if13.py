Salary=int(input("Enter the Salary"))

if (Salary>=5000):
	da=0.3*Salary
	hr=0.2*Salary
	total_salary=Salary+da+hr
    
else:
	da=0.1*Salary
	hr=0.05*Salary
total_salary=Salary+da+hr
print("DA:",da)
print("HR:",hr)
print("Total Salary:",total_salary)   -