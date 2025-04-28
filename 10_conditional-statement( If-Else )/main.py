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
