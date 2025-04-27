# Dictionary in Python:
# A dictionary is a collection of key-value pairs, where each key is unique and maps to a value.
# Dictionaries are mutable, meaning they can be changed after creation.
# Dictionaries are defined using curly braces {} or the dict() constructor.
# Keys must be immutable types (e.g., strings, numbers, tuples), while values can be of any type.
# Dictionaries are unordered collections, meaning the order of items is not guaranteed.

cars = {
    "Toyota": "Corolla",
    "Honda": "Civic",
    "Ford": "Mustang",
    "Chevrolet": "Camaro",
    "Nissan": "Altima"
}
print("Cars dictionary:", cars)  # Print the dictionary of cars
print("Toyota model:", cars["Toyota"])  # Access the value associated with the key "Toyota"

marks = {
    "Urdu": 90,
    "English": 85,
    "Math": 95,
}
print("Marks dictionary:", marks)  # Print the dictionary of marks
print("Math marks:", marks["Math"])  # Access the value associated with the key "Math"
print("Urdu marks:", marks.get("Urdu"))  # Access the value associated with the key "Urdu" using get() method

marks["Science"] = 88  # Add a new key-value pair to the dictionary
print("Updated marks dictionary:", marks)  # Print the updated dictionary of marks


del marks["English"]  # Remove the key-value pair with the key "English"
print("Marks dictionary after deletion:", marks)  # Print the dictionary after deletion

length = len(marks)  # Get the number of key-value pairs in the dictionary
print("Number of subjects:", length)  # Print the number of subjects in the dictionary