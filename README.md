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

- [Arithmetic Operations](#arithmetic-operations)
- [String Operations](#string-operations)
- [Lists](#lists)
- [Tuples](#tuples)
- [Dictionaries](#dictionaries)
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
