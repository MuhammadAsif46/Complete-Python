# what are functions?
# Functions are reusable pieces of code that perform a specific task.
# They help to organize code, make it more readable, and reduce redundancy.
# Block of code that only runs when called.
# Functions can take inputs (arguments) and can return outputs (results).

# Creating a function
def greet():
    print("Hello, World!")

# Calling the function
greet()

# Function with parameters
def greet_user(name,age):
    print(f"Hello, and welcome:  {name}!")
    print(f'Age is {age}')

# Calling the function with arguments
greet_user("John", 25)
greet_user("Clerk", 52)

# Function with default parameters
def greet_user(name, age=18):
    print(f"Hello, and welcome:  {name}!")
    print(f'Age is {age}')

# Calling the function with default parameter
greet_user("John")
greet_user("Clerk")

def sum(num1, num2):
    return num1 * num2

sum_result = sum(5, 10)
print(f"The sum is: {sum_result}")


# Dynamic Arguments functions ( * ):
def greet_user(name, *hobbies):
    print(f"Welome: - {name}!")
    print(f"Your hobbies are:")
    for hobby in hobbies:
        print(f"- {hobby}")

greet_user("John", "Reading", "Traveling")


# Dynamic Arguments functions ( */8 ):
def greet_user(name, **userInfo):
    print(f"Welome: - {name}!")
    for key, value in userInfo.items():
        print(f"{key}: {value}")


greet_user("John", age= 25, hobby= "Reading", city = "New York")
greet_user("Clerk", age=52, hobby = "Traveling")
