class EmployeesData:

    COMPANY = 'ABC.Tech'
    # Constructor to initialize
    def __init__(self, name, email, department, salary):
        self.name = name
        self.email = email
        self.department = department
        self.salary = salary

    def emp_info(self):
        print(f'Name: {self.name}')
        print(f'Email: {self.email}')
        print(f'Department: {self.department}')
        print(f'Salary: {self.salary}')

    def change_salary(self, new_salary):
        self.salary = new_salary
        print(f'New Salary: {new_salary}')

# # Object Creation
# emp1 = EmployeesData("John", "jhon@gmail.com", "Sales", 30000)
# emp2 = EmployeesData("Doe", "doe@gmail.com", "HR", 40000)

# print(emp1.name)
# print(emp2.department)

# # emp1.emp_info()
# # emp2.emp_info()

# emp1.change_salary(35000)
# emp1.emp_info()

# print(emp1.COMPANY)
# print(EmployeesData.COMPANY)