Salary=int(input("Enter the Salary"))
da=0
hr=0


da=0.3*Salary if Salary>5000 else 0.1*Salary
hr=0.2*Salary if Salary>5000 else 0.05*Salary
total_salary=Salary+da+hr
print("DA:",da)
print("HR:",hr)
print("Total Salary:",total_salary)   