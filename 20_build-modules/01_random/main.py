# python Built-in Module
# - random

import random

print(random.random())
print(random.randint(1, 100))
print(random.uniform(1, 100))
print(random.randrange(1, 100, 2))
print(random.choice([1, 2, 3, 4, 5]))
print(random.sample([1, 2, 3, 4, 5], 3))
print(random.shuffle([1, 2, 3, 4, 5]))


fruits = ["apple", "banana", "cherry","kivi","mango"]
print(random.choice(fruits)) 


print(fruits)
print(random.shuffle(fruits))
print(fruits)