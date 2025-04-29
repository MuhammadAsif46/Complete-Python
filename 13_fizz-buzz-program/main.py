# Fizz Buzz Program
# This program prints the numbers from 1 to 100. But for multiples of three it prints "Fizz" instead of the number and for the multiples of five it prints "Buzz". For numbers which are multiples of both three and five it prints "FizzBuzz".

till_number = int(input("Enter a number: "))
list_numbers = []

for num in range(1, till_number+1):
    result = ""
    if num % 3 == 0 and num % 5 == 0:
        result += "FizzBuzz"
    elif num % 3 == 0:
        result += "Fizz"
    elif num % 5 == 0:
        result += "Buzz"
    else:
        result = num
    list_numbers.append(result)
    
print(list_numbers)