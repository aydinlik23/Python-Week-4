'''2-exact_divisor.py

Write a function that finds the exact divisors of a given number. 
For example: function call : exact_divisor(12) output : 1,2,3,4,6,12'''

import math

def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

print (list(divisorGenerator(100))