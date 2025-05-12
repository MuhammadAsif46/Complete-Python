
print(10 * 2)
try:
    print(10 / 0)
except ZeroDivisionError :
    print("Error: Kindly do not divide by ZERO.")
print(10 + 2)
print(10 - 2)


try:
    with open("test.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file does not exist.")



try:
    with open("../18_read-&-write-with-files/read_user_info", "r") as file:
        content = file.readlines()
except FileNotFoundError:
    print("Error: The file does not exist.")
else:
    for line in content:
        print(f'Welcomr, {line.strip()}') 

      
try:
    with open("../16_read-&-write-with-files/read_use_info", "r") as file:
        content = file.readlines()
except Exception as e:
    print(e, type(e))
else:
    for line in content:
        print(f'Welcomr, {line.strip()}') 
finally:
    print("This block will always execute, regardless of exceptions.")
