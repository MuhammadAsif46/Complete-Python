import random

print("Welcome to the Dice Game!")
# print(f'Number is: {random.randint(1, 6)}')

while True:
    print(f'Number is: {random.randint(1, 6)}')
    user_input = input('Do you want to roll the dice? (y/n): ')
    if user_input.lower() != 'y':
        print("Thanks for playing!")
        break