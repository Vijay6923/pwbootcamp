annual_salary=int(input("Enter the annual salary: "))
tax_rate=int(input("Enter tax rate: "))
Post_tax_annual_salary=float(annual_salary*(1-(tax_rate/100)))
monthly_salary=float(Post_tax_annual_salary/12)
print("monthly salary: ",monthly_salary)