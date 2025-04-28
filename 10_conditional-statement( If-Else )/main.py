# codional statement:

if True:
    print("This is true")
else:
    print("This is false")


age = int(input("Enter your age: "))

# Check if the user is eligible to vote
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# Check if the number is even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")



users = ["Alice", "Bob", "Charlie"]
if "Alice" in users:
    print("User Exists.")
else:
    print("User does not exist.")


# If-Elif-Else Statement:
# Check if the number is positive, negative, or zero
number = int(input("Enter a number: "))
if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print("The number is zero.")



# Nested if-else statement
country = input("Enter your country: ")
if country == "Pakistan":
    print("You are from Pakistan.")
    city = input("Enter your city: ")
    if city == "Karachi":
        print("You are from Karachi city.")
    else:
        print("You are not from Karachi city.")
else:
    print("You are not from Pakistan.")