import employees

# Object Creation
emp1 = employees.ExmployeesData("John", "jhon@gmail.com", "Sales", 30000)
emp2 = employees.ExmployeesData("Doe", "doe@gmail.com", "HR", 40000)

print(emp1.name)
print(emp2.department)

# emp1.emp_info()
# emp2.emp_info()

emp1.change_salary(35000)
emp1.emp_info()

print(emp1.COMPANY)
print(employees.ExmployeesData.COMPANY)