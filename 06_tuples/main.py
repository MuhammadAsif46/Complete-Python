# Tuples in Python
# Same as lists but immutable (cannot be changed)
# Tuples are defined using parentheses () instead of square brackets []
# Tuples can contain different data types, including numbers, strings, and other tuples

days=("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday")  # Tuple of days of the week
print("Days of the week:", days)  # Print the tuple of days

print(days.count("Monday"))  # Count the occurrences of "Monday" in the tuple
print(days.index("Wednesday"))  # Get the index of "Wednesday" in the tuple
