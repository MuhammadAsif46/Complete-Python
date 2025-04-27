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

| Operator | Description        | Example     | Output  |
|:---------|:--------------------|:------------|:--------|
| `+`      | Addition             | `5 + 3`     | `8`     |
| `-`      | Subtraction          | `5 - 3`     | `2`     |
| `*`      | Multiplication       | `5 * 3`     | `15`    |
| `/`      | Division             | `5 / 2`     | `2.5`   |
| `//`     | Floor Division       | `5 // 2`    | `2`     |
| `%`      | Modulus (Remainder)  | `5 % 2`     | `1`     |
| `**`     | Exponent (Power)     | `2 ** 3`    | `8`     |

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

| Operation     | Example                      | Output          |
|:--------------|:------------------------------|:----------------|
| Concatenation | `"Hello " + "World"`           | `Hello World`   |
| Repetition    | `"Hi " * 3`                    | `Hi Hi Hi `     |
| Length        | `len("Python")`                | `6`             |
| Slicing       | `"Python"[0:3]`                | `Pyt`           |
| Lowercase     | `"HELLO".lower()`              | `hello`         |
| Uppercase     | `"hello".upper()`              | `HELLO`         |
| Replace       | `"hello world".replace("world", "Python")` | `hello Python` |
| Find          | `"hello".find("e")`             | `1`             |

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

| Operation        | Example                     | Output                    |
|:-----------------|:-----------------------------|:---------------------------|
| Create List      | `my_list = [1, 2, 3]`         | `[1, 2, 3]`                |
| Indexing         | `my_list[0]`                 | `1`                       |
| Slicing          | `my_list[0:2]`               | `[1, 2]`                  |
| Append           | `my_list.append(4)`          | `[1, 2, 3, 4]`            |
| Insert           | `my_list.insert(1, 5)`       | `[1, 5, 2, 3, 4]`         |
| Remove           | `my_list.remove(2)`          | `[1, 5, 3, 4]`            |
| Pop              | `my_list.pop()`              | Removes last element `4`  |
| Length           | `len(my_list)`               | `3` (after pop)           |

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

| Operation        | Example                      | Output                |
|:-----------------|:------------------------------|:----------------------|
| Create Tuple     | `my_tuple = (1, 2, 3)`         | `(1, 2, 3)`           |
| Single Item Tuple| `single = (5,)`                | `(5,)`                |
| Indexing         | `my_tuple[1]`                 | `2`                   |
| Slicing          | `my_tuple[0:2]`               | `(1, 2)`              |
| Length           | `len(my_tuple)`               | `3`                   |
| Count Elements   | `my_tuple.count(2)`            | `1`                   |
| Find Index       | `my_tuple.index(3)`            | `2`                   |

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

### Dictionaries

In Python, a dictionary is a collection of key-value pairs. Dictionaries are **unordered**, **mutable**, and **indexed**.

1. Dictionaries store data in key-value pairs.
2. Keys must be unique and immutable (like strings, numbers).
3. Values can be of any data type.
4. Dictionaries are mutable (can add, change, or remove key-value pairs).
5. Useful for structured data storage (like JSON).

| Operation          | Example                                  | Output                          |
|:-------------------|:-----------------------------------------|:--------------------------------|
| Create Dictionary  | `my_dict = {"name": "Asif", "age": 20}`   | `{'name': 'Asif', 'age': 20}`   |
| Access Value       | `my_dict["name"]`                        | `'Asif'`                        |
| Add Item           | `my_dict["city"] = "Karachi"`             | Adds `'city': 'Karachi'`        |
| Update Value       | `my_dict["age"] = 21`                    | Updates `'age': 21`             |
| Remove Item        | `my_dict.pop("city")`                    | Removes `'city'`                |
| Keys List          | `my_dict.keys()`                         | `dict_keys(['name', 'age'])`    |
| Values List        | `my_dict.values()`                       | `dict_values(['Asif', 21])`     |
| Items (Pairs)      | `my_dict.items()`                        | `dict_items([('name', 'Asif'), ('age', 21)])` |

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

- [Sets](#sets)
- [User Input](#user-input)
- [Conditional Statements (If-Else)](#conditional-statements-if-else)
- [ELIF Statement](#elif-statement)
- [Nested If-Else](#nested-if-else)
- [Logical Operators (AND, OR)](#logical-operators-and-or)
- [For Loops](#for-loops)
- [Fizz Buzz Project](#fizz-buzz-project)
- [While Loops](#while-loops)
- [Break and Continue Statements](#break-and-continue-statements)
- [Functions](#functions)
- [Using Python Code as a Module](#using-python-code-as-a-module)
- [Assignment / Exercise](#assignment-exercise)
- [Object-Oriented Programming (OOP) in Python](#object-oriented-programming-oop-in-python)
- [File Reading and Writing](#file-reading-and-writing)
- [Exception Handling](#exception-handling)
- [Random and Datetime Modules](#random-and-datetime-modules)
- [Dice Game Project](#dice-game-project)
- [What is PyPI and PIP?](#what-is-pypi-and-pip)
- [CSV Data Analysis using Pandas](#csv-data-analysis-using-pandas)
- [Data Visualization using Matplotlib](#data-visualization-using-matplotlib)
- [Sending Emails using SMTP Library](#sending-emails-using-smtp-library)
- [Weather App using API in Python](#weather-app-using-api-in-python)
- [Running Linux Commands using Python (Subprocess Module)](#running-linux-commands-using-python-subprocess-module)

---

## 🚀 About

These notes are designed to help learners move from basic Python concepts to more advanced programming skills.
Ideal for building projects, automation, and real-world applications.

---

```

```
