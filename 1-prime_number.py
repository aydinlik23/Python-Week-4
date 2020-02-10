'''1-prime_number.py

Write a function that checks if any given number is a prime number or not. 

For example: function call : prime_number(123) output : 123 is not prime number'''

def prime_number(Number):
    count = 0

    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
    return count


Number = int(input(" Please Enter any Number: "))

cnt = prime_number(Number)

if (cnt == 0 and Number != 1):
    print(f"{Number} is a Prime Number")
else:
    print(f"{Number} is not a Prime Number")