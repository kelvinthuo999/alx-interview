#!/usr/bin/python3

evenNumbers = [num for num in range(20) if num % 2 == 0]
print (evenNumbers)

for num in range(1, 21):
    if num % 3 == 0 and num % 5 == 0:
        print ('FizzBuzz')
    elif num % 3 == 0:
        print ('Fizz')
    elif num % 5 == 0:
        print ('Buzz')
    else:
        print (num)
