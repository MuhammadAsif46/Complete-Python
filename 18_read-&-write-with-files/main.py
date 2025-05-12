
# Read and write with files

# with open('user_info', 'w') as file:
#     file.write('This is my first created file using python\n')

# Read the file appending the text

# with open('user_info', 'a') as file:
#     file.write('This is my second line in my text file using python\n')

# with open('user_info', 'a') as file:
#     file.write('This is my third line in my text file using python\n')


# Read the file
# with open('read_user_info', 'r') as file:
#     content = file.read()
#     print(content)

# Read the file line by line
with open('read_user_info', 'r') as file:
    content = file.readlines()
    for line in content:
        print(f'Welcome, {line.rstrip()}')  # Remove leading/trailing whitespace