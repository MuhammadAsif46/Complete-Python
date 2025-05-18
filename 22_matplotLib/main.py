import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('emp_data.csv')
print(data)


# Plotting the data using Plot
# plt.plot(data.emp_id, data.salary)

# Plotting the data using Bar
# plt.bar(data.emp_id, data.salary)

# Plotting the data using scatter
# plt.scatter(data.emp_id, data.salary)

# plt.title('Employee ID vs Salary')
# plt.xlabel("Employee id")
# plt.ylabel("Employee salary")
# plt.show()


# Plotting the data using Bar

data = pandas.read_csv('user_info.csv')
city_count = data.city.value_counts()
plt.bar(city_count.index, city_count.values)
plt.title('City vs No of users')
plt.xlabel("City")
plt.ylabel("No of users")
plt.show()
