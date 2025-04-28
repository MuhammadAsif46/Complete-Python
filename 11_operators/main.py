# Operators:
# 1. Arithmetic Operators: +, -, *, /, //, %, **
# 2. Comparison Operators: ==, !=, >, <, >=, <=
# 3. Logical Operators: and, or, not
# 4. Assignment Operators: =, +=, -=, *=, /=, //=, %=, **=
# 5. Identity Operators: is, is not
# 6. Membership Operators: in, not in
# 7. Bitwise Operators: &, |, ^, ~, <<, >>
# 8. Ternary Operator: condition_if_true if condition else condition_if_false
# 9. Conditional Operator: (condition) ? (true_value) : (false_value)

# equal == 20
# not equal != 20
# greater than > 20
# less than < 20
# greater than or equal to >= 20
# less than or equal to <= 20


# Logical Operators: and, or, not
country = "Pakistan"
city = "Karachi"
if country == "Pakistan" and city == "Karachi":
    print("You are in Karachi, Pakistan")
else:
    print("You are not in Karachi, Pakistan")

# or operator
country = "Pakistan"
city = "Lahore"
if country == "Pakistan" or city == "Karachi":
    print("You are in Pakistan or Karachi")
else:
    print("You are not in Pakistan or Karachi")

# not operator
country = "Pakistan"
city = "Karachi"
if not (country == "Pakistan" and city == "Karachi"):
    print("You are not in Karachi, Pakistan")
else:
    print("You are in Karachi, Pakistan")