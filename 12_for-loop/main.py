# for loop in python

for no in 1,2,3,4,5:
    print(no)



# for loop with numbers in a list
numbers = [1,2,3,4,6,7,8,9,10]
for i in numbers:
    print(i) 

# for loop with numbers in a list
alphabets = ['hello','world','python','is','fun']
for i in alphabets:
    print(i) 


# for loop with different data types
values = ['ab',1,'cd',4,True,'gh',8,False,'xyz']
for val in values:
    print(val)  


# Other examples of for loop : key, value pairs in a dictionary
age_info = {
    'John': 25,
    'Alice': 30,
    'Bob': 22,
    'Charlie': 28
}

for name, age in age_info.items():
    print(f"{name} is {age} years old.")

for name in age_info.keys():
    print(name)

for age in age_info.values():
    print(age)

# for loop with range function
for i in range(1, 11):
    print(i)