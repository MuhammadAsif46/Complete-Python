# print the CSV file
# Print only Salary Column
# Find Min and Max Salary
# Find data of employees with 
    # emp_id 105
    # Max salary
# Find total & average salary of all employees
# Print full name of employee id 103

import pandas as pd

# Read the CSV file
data = pd.read_csv('emp_data.csv')
print(data)

# Print only Salary Column
print(data.salary)

# Find Min and Max Salary
print("Min Salary -> ",data.salary.min())
print("Max Salary -> ", data.salary.max())
print("Sum Salary -> ",data.salary.sum())


# Find data of employees with emp_id 105
print(data[data.emp_id == 105])

# Find data of employees with Max salary
print(data[data.salary == data.salary.max()])

# Find total & average salary of all employees
print("Total Salary -> ",data.salary.sum())
print("Average Salary -> ",data.salary.mean())

# Print full name of employee id 103
emp_id_103 = data[data.emp_id == 103]
print("Full name -> ",emp_id_103.fname.values[0], emp_id_103.lname.values[0])


print(data.salary.to_list())
for i in data.salary:
    print(f'Salary here - {i} ')


print(data.to_dict())