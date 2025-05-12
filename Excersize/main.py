# first_num = int(input("Enter first number: "))
# second_num = int(input("Enter second number: "))
# operator = input("Select the operation: ")
# result = 0
# while True:
#     if operator == "+":
#         result = first_num + second_num
#         print(f"Result of {first_num} + {second_num} is {result}")
#         choice = input(f'Continue the operation with {result}? (y/n): ')
#         if choice.lower() != 'y':
#             print('Exiting the program.')
#             break
#         else:
#             next_num = int(input("Enter the next number: "))
#             operator1 = input("Select the operation: ")
#             if operator1 == "+":
#                 result1 = result + next_num
#                 print(f"Result of {result} + {next_num} is {result1}")
#             # elif operator1 == "-":
#             #     result1 = next_num - result
#             #     print(f"Result of {result} - {next_num} is {result}")
#             # elif operator1 == "*":
#             #     result1 = next_num * result
#             #     print(f"Result of {result} * {next_num} is {result}")
#             # elif operator1 == "/": 
#             #     result1 = next_num / result
#             #     print(f"Result of {result} / {next_num} is {result}")
#     elif operator == "-":
#         result = first_num - second_num
#         print(f"Result of {first_num} - {second_num} is {result}")
#     elif operator == "*":
#         result = first_num * second_num
#         print(f"Result of {first_num} * {second_num} is {result}")
#     elif operator == "/":
#         result = first_num / second_num
#         print(f"Result of {first_num} / {second_num} is {result}")


# Initial Inputs
first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))
operator = input("Select the operation (+, -, *, /): ")

# Perform first calculation
def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    else:
        return "Invalid operator"

result = calculate(first_num, second_num, operator)

print(f"Result of {first_num} {operator} {second_num} is {result}")

# Continue operations on result
while True:
    choice = input(f'Continue the operation with {result}? (y/n): ')
    if choice.lower() != 'y':
        print("Exiting the program.")
        break
    next_num = float(input("Enter the next number: "))
    next_operator = input("Select the operation (+, -, *, /): ")
    result = calculate(result, next_num, next_operator)
    print(f"Result of {result} {operator} {next_num} is {result}")
