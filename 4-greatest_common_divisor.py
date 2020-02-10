'''4-greatest_common_divisor.py

Write a function that gives the greatest common divisor of any entered 2 numbers. 
For example: function call: greatest_common_divisor(15,25) output:5'''

def gcd(a, b):
    if(b == 0):
        return a;
    else:
        return gcd(b, a % b)
    
num1 = int(input(" Please Enter the First  Number : "))
num2 = int(input(" Please Enter the Second Number : "))

gcd = gcd(num1, num2)
print("\n Greatest_common_divisor = {2}".format(num1, num2, gcd))