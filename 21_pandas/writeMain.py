# Change the salary of sham to 80000
# Remove the data of leena
# Sort the data with salary (min to max)
# Add a new column 'bonus' with value 10% of salary
# Drop the 'salary' column


import pandas as pd

# Read the CSV file
data = pd.read_csv('emp_data.csv')
print(data)


# Change the salary of sham to 80000
data.loc[data.fname == 'Sham' , 'salary' ] = 95000
print(data)


# Remove the data of leena
# data.drop(6) # 1st way
drop_data = data.index[data.emp_id == 107].to_list()[0]
data1 = data.drop(drop_data)
print(data1)


# Sort the data with salary (min to max)
# data = data.sort_values(by='salary', ascending=False)
data = data.sort_values(by='salary')
print(data)


# Add a new column 'bonus' with value 10% of salary
data['bonus'] = data.salary / 10
print(data)


# Drop the 'salary' column
data = data.drop('bonus', axis=1)
print(data)