# 🐍 Python Full Course – Notes

This repository contains organized notes covering all major Python programming topics.  
Perfect for beginners and intermediate learners.

---

## 📚 Table of Contents

## Python Installation and Setup

To start coding in Python, you need to install Python on your computer.

🔹 Download the latest version of Python from the official website:  
👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)

🔹 Installers are available for Windows, macOS, and Linux.

🔹 While installing on Windows, make sure to check the option **"Add Python to PATH"** during the setup process.

🔹 After installation, verify it by running the following command in the terminal or command prompt:

```bash
python --version
```

---

## Running Python on Linux

Most Linux distributions (like Ubuntu, Fedora, Debian) come with Python pre-installed.

🔹 To check if Python is already installed, open the terminal and run:

```bash
python3 --version
```

🔹 If Python is not installed, you can install it using the package manager:

- For Debian/Ubuntu based systems:

```bash
sudo apt update
sudo apt install python3
```

- For Fedora:

```bash
sudo dnf install python3
```

🔹 After installation, verify by running:

```bash
python3 --version
```

✅ Now you can run Python programs using:

```bash
python3 filename.py
```

---

## Your First Python Program

Let's write and run your very first Python programs! 🎉

In Python, the `print()` function is used to display output on the screen.

Here are some basic examples:

```python
print(200)            # Prints the number 200
print("Hello World")  # Prints the text Hello World
print(10 * 5)         # Prints the result of 10 multiplied by 5 (i.e., 50)
print(10 % 3)         # Prints the remainder when 10 is divided by 3 (i.e., 1)
```

### How to run:

1. Open your code editor or terminal.
2. Save the code in a file named first.py.
3. Run the program:

- For Windows:

```bash
python first.py
```

- For Linux/macOS:

```bash
python3 first.py
```

---

## Comments in Python

- Single-line comment example:

```bash
# Printing a number
print(200)

#  Printing a text message
print("Hello World")

# Printing the sum of two numbers
print(10 + 5)

# Printing the product of two numbers
print(10 * 3)

```

- Multi-line comment example:

```bash
'''
This is a multi-line comment.
You can use triple single quotes ('''or''') or triple double quotes (""" or """)
to write comments that span multiple lines.
'''
```

---

## Variables

🔹 How to create a variable in Python:

```python
name = "Asif"
age = 22
price = 499.99
is_active = True
```

🔹 Roles of Variables:

- Store information (like numbers, text, etc.)
- Make code readable and organized
- Allow reuse of values without repeating
- Help in doing calculations and data processing easily

✅ In Python, you don't need to declare the type of a variable — Python automatically figures it out based on the assigned value.

---

## Data Types

Data types represent the kind of data a variable holds.
Each value in Python has a specific type.

🔹 Common Data Types in Python:

- **int** — Integer numbers (e.g., 10, -5, 200)
- **float** — Decimal numbers (e.g., 10.5, 3.14)
- **str** — Strings/Text (e.g., "Hello", "Python")
- **bool** — Boolean (True or False)
- **list** — Ordered collection (e.g., [1, 2, 3])
- **tuple** — Immutable ordered collection (e.g., (1, 2, 3))
- **dict** — Key-Value pairs (e.g., {"name": "Asif", "age": 22})
- **set** — Unordered unique elements (e.g., {1, 2, 3})

🔹 Examples:

```bash
# Integer
x = 10

# Float
y = 20.5

# String
name = "Asif"

# Boolean
is_active = True

# List
fruits = ["apple", "banana", "mango"]

# Dictionary
student = {"name": "Asif", "age": 22}
```

✅ Python automatically sets the type when you assign a value.

### How to Check the Type of a Variable

In Python, you can use the type() function to check what type of data a variable holds.

🔹 Example:

```bash
x = 10
print(type(x))   # Output: <class 'int'>

y = "Hello"
print(type(y))   # Output: <class 'str'>
```

✅ type() function helps you understand what kind of value a variable is storing.

---

## Arithmetic Operations

In Python, arithmetic operations are used to perform basic mathematical calculations like addition, subtraction, multiplication, and division.

| Operator | Description         | Example  | Output |
| :------- | :------------------ | :------- | :----- |
| `+`      | Addition            | `5 + 3`  | `8`    |
| `-`      | Subtraction         | `5 - 3`  | `2`    |
| `*`      | Multiplication      | `5 * 3`  | `15`   |
| `/`      | Division            | `5 / 2`  | `2.5`  |
| `//`     | Floor Division      | `5 // 2` | `2`    |
| `%`      | Modulus (Remainder) | `5 % 2`  | `1`    |
| `**`     | Exponent (Power)    | `2 ** 3` | `8`    |

#### Examples:

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

---

## String Operations

In Python, strings are sequences of characters. You can perform many operations on strings like joining, slicing, repeating, and finding length.

| Operation     | Example                                    | Output         |
| :------------ | :----------------------------------------- | :------------- |
| Concatenation | `"Hello " + "World"`                       | `Hello World`  |
| Repetition    | `"Hi " * 3`                                | `Hi Hi Hi `    |
| Length        | `len("Python")`                            | `6`            |
| Slicing       | `"Python"[0:3]`                            | `Pyt`          |
| Lowercase     | `"HELLO".lower()`                          | `hello`        |
| Uppercase     | `"hello".upper()`                          | `HELLO`        |
| Replace       | `"hello world".replace("world", "Python")` | `hello Python` |
| Find          | `"hello".find("e")`                        | `1`            |

#### Examples:

```python
str1 = "Hello"
str2 = "World"

# Concatenation
print(str1 + " " + str2)    # Hello World

# Repetition
print(str1 * 3)             # HelloHelloHello

# Length
print(len(str2))            # 5

# Slicing
print(str1[0:3])            # Hel

# Lowercase and Uppercase
print(str2.lower())         # world
print(str1.upper())         # HELLO

# Replace
sentence = "I love Java"
print(sentence.replace("Java", "Python"))  # I love Python

# Find
print(str1.find('e'))       # 1
```

---

## Lists

In Python, a list is a collection which is ordered and changeable (mutable). Lists allow duplicate elements.

1. Lists are defined using square brackets `[]`.
2. Elements can be of different data types.
3. Lists are mutable (we can change, add, or remove items).
4. Lists allow duplicate values.
5. Common operations include indexing, slicing, adding, removing, and looping.

| Operation   | Example                | Output                   |
| :---------- | :--------------------- | :----------------------- |
| Create List | `my_list = [1, 2, 3]`  | `[1, 2, 3]`              |
| Indexing    | `my_list[0]`           | `1`                      |
| Slicing     | `my_list[0:2]`         | `[1, 2]`                 |
| Append      | `my_list.append(4)`    | `[1, 2, 3, 4]`           |
| Insert      | `my_list.insert(1, 5)` | `[1, 5, 2, 3, 4]`        |
| Remove      | `my_list.remove(2)`    | `[1, 5, 3, 4]`           |
| Pop         | `my_list.pop()`        | Removes last element `4` |
| Length      | `len(my_list)`         | `3` (after pop)          |

#### Examples:

```python
# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])  # apple

# Slicing
print(fruits[0:2])  # ['apple', 'banana']

# Adding elements
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']

# Inserting elements
fruits.insert(1, "mango")
print(fruits)  # ['apple', 'mango', 'banana', 'cherry', 'orange']

# Removing elements
fruits.remove("banana")
print(fruits)  # ['apple', 'mango', 'cherry', 'orange']

# Popping the last element
last_fruit = fruits.pop()
print(last_fruit)  # orange
print(fruits)      # ['apple', 'mango', 'cherry']

# Length of list
print(len(fruits))  # 3
```

✅ Lists are super flexible for storing multiple values in a single variable.

---

## Tuples

In Python, a tuple is a collection which is ordered and **immutable** (cannot be changed after creation). Tuples allow duplicate elements.

1. Tuples are defined using parentheses `()`.
2. Elements can be of different data types.
3. Tuples are immutable (no add, remove, or change after creation).
4. Tuples allow duplicate values.
5. Useful when you want data to stay constant.

| Operation         | Example                | Output      |
| :---------------- | :--------------------- | :---------- |
| Create Tuple      | `my_tuple = (1, 2, 3)` | `(1, 2, 3)` |
| Single Item Tuple | `single = (5,)`        | `(5,)`      |
| Indexing          | `my_tuple[1]`          | `2`         |
| Slicing           | `my_tuple[0:2]`        | `(1, 2)`    |
| Length            | `len(my_tuple)`        | `3`         |
| Count Elements    | `my_tuple.count(2)`    | `1`         |
| Find Index        | `my_tuple.index(3)`    | `2`         |

#### Examples:

```python
# Creating a tuple
numbers = (1, 2, 3, 4)

# Accessing elements
print(numbers[0])  # 1

# Slicing
print(numbers[1:3])  # (2, 3)

# Length of tuple
print(len(numbers))  # 4

# Count specific value
print(numbers.count(2))  # 1

# Find index of a value
print(numbers.index(3))  # 2

# Single item tuple (must include comma)
single_item = (5,)
print(single_item)  # (5,)
```

✅ Tuples are perfect when you want fixed, read-only data in Python.

---

## Dictionaries

In Python, a dictionary is a collection of key-value pairs. Dictionaries are **unordered**, **mutable**, and **indexed**.

1. Dictionaries store data in key-value pairs.
2. Keys must be unique and immutable (like strings, numbers).
3. Values can be of any data type.
4. Dictionaries are mutable (can add, change, or remove key-value pairs).
5. Useful for structured data storage (like JSON).

| Operation         | Example                                 | Output                                        |
| :---------------- | :-------------------------------------- | :-------------------------------------------- |
| Create Dictionary | `my_dict = {"name": "Asif", "age": 20}` | `{'name': 'Asif', 'age': 20}`                 |
| Access Value      | `my_dict["name"]`                       | `'Asif'`                                      |
| Add Item          | `my_dict["city"] = "Karachi"`           | Adds `'city': 'Karachi'`                      |
| Update Value      | `my_dict["age"] = 21`                   | Updates `'age': 21`                           |
| Remove Item       | `my_dict.pop("city")`                   | Removes `'city'`                              |
| Keys List         | `my_dict.keys()`                        | `dict_keys(['name', 'age'])`                  |
| Values List       | `my_dict.values()`                      | `dict_values(['Asif', 21])`                   |
| Items (Pairs)     | `my_dict.items()`                       | `dict_items([('name', 'Asif'), ('age', 21)])` |

#### Examples:

```python
# Creating a dictionary
student = {
    "name": "Asif",
    "age": 20,
    "course": "Python"
}

# Accessing values
print(student["name"])  # Asif

# Adding new key-value pair
student["city"] = "Karachi"
print(student)

# Updating value
student["age"] = 21
print(student)

# Removing a key-value pair
student.pop("course")
print(student)

# Getting all keys
print(student.keys())

# Getting all values
print(student.values())

# Getting all key-value pairs
print(student.items())
```

✅ Dictionaries are perfect for representing structured, real-world data.

---

## Sets

In Python, a set is an **unordered**, **unindexed**, and **mutable** collection of **unique elements**.

1. Sets automatically remove duplicate values.
2. Sets are mutable, but elements must be immutable.
3. Sets do not support indexing or slicing.
4. Sets are useful for membership tests, removing duplicates, and mathematical operations (union, intersection).

| Operation            | Example                   | Output                           |
| :------------------- | :------------------------ | :------------------------------- |
| Create Set           | `my_set = {1, 2, 3}`      | `{1, 2, 3}`                      |
| Add Element          | `my_set.add(4)`           | Adds `4` to the set              |
| Remove Element       | `my_set.remove(2)`        | Removes `2`                      |
| Discard Element      | `my_set.discard(5)`       | No error even if `5` not present |
| Union of Sets        | `set1.union(set2)`        | Combine sets                     |
| Intersection of Sets | `set1.intersection(set2)` | Common elements                  |
| Difference of Sets   | `set1.difference(set2)`   | Elements only in set1            |

#### Examples:

```python
# Creating a set
fruits = {"apple", "banana", "cherry"}

# Adding an element
fruits.add("orange")
print(fruits)

# Removing an element
fruits.remove("banana")
print(fruits)

# Using discard (no error if element doesn't exist)
fruits.discard("pineapple")

# Set union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))  # {1, 2, 3, 4, 5}

# Set intersection
print(set1.intersection(set2))  # {3}

# Set difference
print(set1.difference(set2))  # {1, 2}
```

✅ Sets are great for working with unique items and set operations.

---

## User Input

In Python, `input()` function is used to take input from the user.  
The input is always received as a **string**. You can typecast it into other data types like `int`, `float`, etc.

| Operation          | Example                                     | Output/Behavior                 |
| :----------------- | :------------------------------------------ | :------------------------------ |
| Take String Input  | `name = input("Enter your name: ")`         | User types input (e.g., "Asif") |
| Take Integer Input | `age = int(input("Enter your age: "))`      | Converts input to integer       |
| Take Float Input   | `price = float(input("Enter the price: "))` | Converts input to float         |
| Display User Input | `print(name)`                               | Prints the user input           |

#### Examples:

```python
# Taking a string input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Taking an integer input
age = int(input("Enter your age: "))
print(f"You are {age} years old.")

# Taking a float input
price = float(input("Enter the product price: "))
print(f"The price is {price} dollars.")

# Simple calculation with user input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"The sum is {num1 + num2}")
```

✅ input() is the way to interact with users in a Python program!

---

## Conditional Statements (If-Else-Elif)

In Python, conditional statements allow you to **make decisions** based on certain conditions.  
The main keywords are `if`, `else`, and `elif`.

| Statement | Purpose                                                 |
| :-------- | :------------------------------------------------------ |
| if        | Executes a block of code if the condition is true       |
| elif      | (Else If) Checks another condition if previous is false |
| else      | Executes a block of code if all conditions are false    |

#### Syntax:

```python
if condition:
    # code block
elif another_condition:
    # another code block
else:
    # code block if all conditions fail

# Basic if-else
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Using elif
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")

# Multiple conditions
temperature = int(input("Enter the temperature: "))
if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("The weather is pleasant.")
else:
    print("It's cold outside!")
```

✅ Conditional statements control the flow of your Python program based on conditions.

---

## Logical Operators (AND, OR)

Logical operators are used to **combine multiple conditions**.  
Python mainly has three logical operators: `and`, `or`, and `not`.

| Operator | Description                                        | Example                      |
| :------- | :------------------------------------------------- | :--------------------------- |
| and      | Returns True if **both** conditions are true       | `(5 > 2) and (3 < 7)` → True |
| or       | Returns True if **at least one** condition is true | `(5 > 8) or (3 < 7)` → True  |

#### Examples:

```python
# Using AND operator
age = int(input("Enter your age: "))
if age >= 18 and age <= 60:
    print("You are eligible to work.")
else:
    print("You are not eligible to work.")

# Using OR operator
day = input("Enter the day: ")
if day == "Saturday" or day == "Sunday":
    print("It's a weekend!")
else:
    print("It's a weekday.")

# Combining multiple conditions
score = int(input("Enter your score: "))
if score > 80 and score < 100:
    print("Excellent!")
elif score > 50 or score == 50:
    print("Good!")
else:
    print("Needs Improvement.")
```

✅ Logical operators make your conditional checks more powerful in Python!

---

### For Loops

In Python, a `for` loop is used to **iterate over sequences** like lists, tuples, strings, etc.

| Use Case           | Description                    |
| :----------------- | :----------------------------- |
| Loop over a list   | Access each item in a list     |
| Loop over a string | Access each character          |
| Use with range()   | Generate numbers in a sequence |

#### Syntax:

```python
for item in sequence:
    # code block

# Looping through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Looping through a string
for letter in "Python":
    print(letter)

# Using range()
for i in range(5):
    print(i)   # Prints 0 to 4

# Using range with start and end
for i in range(2, 7):
    print(i)   # Prints 2, 3, 4, 5, 6
```

✅ for loops are perfect for repeating tasks automatically in Python!

---

## While Loops

A `while` loop in Python is used to **execute a block of code repeatedly** as long as a given condition is `True`.

| Element    | Description                              |
| :--------- | :--------------------------------------- |
| while loop | Repeats code while the condition is true |
| break      | Exits the loop early                     |
| continue   | Skips to the next iteration              |

#### Syntax:

```python
while condition:
    # code block
```

```python
# Basic while loop
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

# Infinite loop with break
while True:
    num = int(input("Enter a number (0 to exit): "))
    if num == 0:
        break
    print("You entered:", num)

# Using continue
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)

```

✅ while loops are ideal when you don't know how many times you need to run the loop.

---

## Break and Continue Statements

In Python loops, `break` and `continue` are used to control the flow of the loop.

| Statement | Description                                       |
| :-------- | :------------------------------------------------ |
| break     | Immediately exits the loop                        |
| continue  | Skips the current iteration and moves to the next |

---

### break Example:

```python
# Exit the loop when number is 3
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# Output: 1, 2
```

### Continue Example:

```python
# Skip printing number 3
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Output: 1, 2, 4, 5
```

✅ Use break to stop early, and continue to skip logic inside a loop.

---

## Functions

Functions in Python are **blocks of reusable code** used to perform a specific task.

| Concept        | Description                           |
| :------------- | :------------------------------------ |
| def            | Keyword to define a function          |
| parameters     | Input values to the function          |
| return         | Sends back a result from the function |
| default values | Assign default values to parameters   |

---

#### Basic Function Example:

```python
def greet():
    print("Hello, Python!")

greet()
```

Function with Parameters:

```python
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Asif")

```

Function with Return Value:

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

Function with Default Parameter:

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()          # Output: Hello, Guest!
greet("Asif")    # Output: Hello, Asif!
```

✅ Functions help in writing modular, reusable, and clean code.

---

## Using Python Code as a Module

In Python, any `.py` file can act as a **module** and can be imported into other Python scripts to reuse code.

| Concept     | Description                                |
| :---------- | :----------------------------------------- |
| module      | A Python file containing functions/classes |
| import      | Keyword to load a module                   |
| from-import | Import specific parts of a module          |

---

#### Example:

**math_utils.py**

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

main.py

```python
import math_utils

print(math_utils.add(10, 5))        # Output: 15
print(math_utils.subtract(10, 5))   # Output: 5

```

Using from ... import ...

```python
from math_utils import add

print(add(3, 2))  # Output: 5

```

✅ Organizing your code into modules helps in reusability and clean architecture.

---

## Object-Oriented Programming (OOP) in Python

OOP is a programming paradigm based on **objects and classes** that helps in organizing code and reusability.

| Concept  | Description                                     |
| :------- | :---------------------------------------------- |
| class    | Blueprint for creating objects                  |
| object   | Instance of a class                             |
| **init** | Constructor method, runs when object is created |
| self     | Refers to the current instance of the class     |
| method   | Function defined inside a class                 |

---

### Basic OOP Example:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
```

### Creating object

```python
p1 = Person("Asif", 23)
p1.greet()
```

### Output

```python
Hello, my name is Asif and I am 23 years old.
```

✅ OOP makes your code modular, scalable, and easier to maintain.

---

## File Reading and Writing

In Python, you can use the built-in `open()` function to **read from** and **write to** files.

| Mode | Description         |
| :--- | :------------------ |
| 'r'  | Read (default mode) |
| 'w'  | Write (overwrite)   |
| 'a'  | Append              |
| 'x'  | Create new file     |
| 'rb' | Read binary         |
| 'wb' | Write binary        |

---

#### Writing to a File

```python
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.")
```

#### Reading from a File

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

```

#### Appending to a File

```python
with open("example.txt", "a") as file:
    file.write("\nThis line is added later.")
```

✅ Always use with open(...) — it automatically closes the file after use.

---

## Exception Handling

Exception handling in Python allows you to deal with **errors** gracefully without crashing the program.

| Keyword | Description                     |
| :------ | :------------------------------ |
| try     | Code block to test for errors   |
| except  | Code block to handle the error  |
| else    | Executes if no exception occurs |
| finally | Always executes (error or not)  |

---

#### Basic Example

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
else:
    print("Division successful!")
finally:
    print("Execution completed.")
```

✅ Exception handling helps you build robust and user-friendly applications.

---

## Random and Datetime Modules

Python provides built-in modules like `random` and `datetime` to work with randomness and date/time.

---

#### ✅ `random` Module

Used to generate random numbers or make random selections.

```python
import random

print(random.randint(1, 10))         # Random integer between 1 and 10
print(random.choice(["red", "blue", "green"]))  # Random choice from list
```

✅ datetime Module

#### Used to work with dates and times.

```python
import datetime

now = datetime.datetime.now()
print("Current Date & Time:", now)

today = datetime.date.today()
print("Today's Date:", today)

# Formatting date
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted Date & Time:", formatted)
```

✅ These modules are useful for games, logging, scheduling, and time-based logic.

---

## Dice Game Project

This mini project simulates a dice roll using Python’s `random` module.

#### 🎲 Code Example

```python
import random

print("🎲 Dice Game 🎲")
input("Press Enter to roll the dice...")

dice = random.randint(1, 6)
print(f"You rolled a {dice}!")
```

🔁 Optional: Play Multiple Times

```python
import random

while True:
    input("Press Enter to roll the dice (or Ctrl+C to exit)...")
    print(f"You rolled: {random.randint(1, 6)}\n")
```

✅ This is a fun way to practice the random module and while loop!

---

## What is PyPI and PIP?

### 📦 PyPI (Python Package Index)

PyPI is the **official third-party software repository** for Python.  
It contains thousands of packages and libraries that you can use in your Python projects.

🔗 Visit: [https://pypi.org](https://pypi.org)

---

## 📥 PIP (Python Installer Package)

PIP is the tool used to **install packages** from PyPI.

---

### ✅ Basic PIP Commands

| Command                           | Description                       |
| :-------------------------------- | :-------------------------------- |
| `pip install package-name`        | Install a package                 |
| `pip uninstall package-name`      | Uninstall a package               |
| `pip list`                        | List all installed packages       |
| `pip show package-name`           | Show info about a package         |
| `pip freeze > requirements.txt`   | Save installed packages to a file |
| `pip install -r requirements.txt` | Install from a `requirements.txt` |

---

#### 🔧 Example

```bash
pip install pandas
```

---

### CSV Data Analysis using Pandas

The `pandas` library in Python is widely used for **data analysis**, especially with CSV files.

---

#### 📥 Installing Pandas

```bash
pip install pandas
```

#### 🧾 Reading CSV File

```python
import pandas as pd

# Load data from a CSV file
data = pd.read_csv('data.csv')

# Display first 5 rows
print(data.head())
```

#### 📊 Common Operations

```python
print(data.shape)         # Rows and columns
print(data.columns)       # Column names
print(data.describe())    # Summary statistics
print(data['column_name'].value_counts())  # Count of unique values
```

#### 🔍 Filtering Data

```python
# Rows where age > 25
filtered = data[data['age'] > 25]
print(filtered)
```
✅ pandas makes it easy to manipulate, filter, and analyze CSV data in just a few lines of code.

---

- [Data Visualization using Matplotlib](#data-visualization-using-matplotlib)
- [Sending Emails using SMTP Library](#sending-emails-using-smtp-library)
- [Weather App using API in Python](#weather-app-using-api-in-python)
- [Running Linux Commands using Python (Subprocess Module)](#running-linux-commands-using-python-subprocess-module)

---

## 🚀 About

These notes are designed to help learners move from basic Python concepts to more advanced programming skills.
Ideal for building projects, automation, and real-world applications.

---
