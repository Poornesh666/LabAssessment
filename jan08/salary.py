salary = int(input("Enter your basic salary: "))
hra = 0.2*salary
da = 0.1*salary
tax = 0.05*salary
netSalary = hra+da+tax
print(f"Net Salary:{netSalary}")