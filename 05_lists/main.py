# Lists:
# - A list is a collection of items in a particular order.
# - Lists are mutable, meaning they can be changed after creation.

users = ["Alice", "Bob", "Charlie"]

print("Users:", users)  # Print the list of users
print("First user:", users[0])  # Access the first user
print("Last user:", users[-1])  # Access the last user

users.append("David")  # Add a new user to the end of the list
users.insert(1, "Eve")  # Insert a new user at index 1
users.remove("Bob")  # Remove a user from the list
del users[3]  # Delete a user at index 3
len(users)  # Get the number of users in the list

# Sorting of list items:
users.sort()  # Sort the list in ascending order
print("Sorted users:", users)  # Print the sorted list of users
users.reverse()  # Reverse the order of the list
print("Reversed users:", users)  # Print the reversed list of users
users.sort(reverse=True)  # Sort the list in descending order
print("Sorted users in descending order:", users)  # Print the sorted list of users in descending order

users.pop()  # Remove the last user from the list
print("Users after pop:", users)  # Print the list of users after pop
users.pop(1)  # Remove the user at index 1 from the list


print(users[0:2]) # Print the first two users in the list
print(users[1:])  # Print the users from index 1 to the end of the list
print(users[:2])  # Print the first two users in the list
print(users[::2])  # Print every second user in the list
print(users[::-1])  # Print the list in reverse order
print(users[1:3])  # Print the users from index 1 to 2 (exclusive of index 3)
print(users[-2:])  # Print the last two users in the list


# Numbers list:
marks = [90, 85, 78, 92, 88]  # List of marks
print("Marks:", marks)  # Print the list of marks

# getting the maximum and minimum marks
print("Maximum marks:", max(marks))  # Get the maximum marks
print("Minimum marks:", min(marks))  # Get the minimum marks
print("Sum of marks:", sum(marks))  # Get the sum of all marks
print("Average marks:", sum(marks) / len(marks))  # Get the average marks