# # print('Enter a number: to check if that is Even or not')

# while True:
#     number = int(input('Enter a number: '))
#     if number % 2 == 0:
#         print(f'{number} is Even')
#     else:
#         print(f'{number} is Odd')
#     choice = input('Do you want to continue? (y/n): ')
#     if choice.lower() != 'y':
#         print('Exiting the program.')
#         break
#     else:
#         print('Continuing the program...')
#     print('Enter a number: to check if that is Even or not')
    

# # count 
# count = 1
# while count <= 5:
#     print(count)
#     count += 1


# # msg

# msg = ''
# while msg != 'exit':
#     msg = input('Enter a message (type "exit" to quit): ')
#     if msg != 'exit':
#         print(f'You entered: {msg}')
#     else:
#         print('Exiting the program.')


# # flaq

# flag = True
# while flag:
#     msg = input('Enter a message ')
#     if msg == 'exit':
#         flag = False
#         print('Exiting the program.')
#     else:
#         print(f'You entered: {msg}')



# while loop:
num = [1,28,20,21,40,50,20]
# print(num)

while 20 in num:
    num.remove(20)




# print(num)


# useful concepts
# break: to stop the loop

num = [10, -20, 30, -40, 50, -60, 70, 80]

for n in num:
    if n == 30:
        break
    print(n)

# continue: - to stop current iteration of loop and start next iteration

num1 = [10, -20, 30, -40, 50, -60, 70, 80]

for n in num1:
    if n == 30:
        continue
    print(f'hello {n}')
    # print('hello')