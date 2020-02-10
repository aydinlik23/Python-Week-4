'''5-least_common_multiple.py

Write a function that gives the least common multiple of entered 2 input numbers. 
For example : function call: least_common_multiple(3,4) output : 12'''

def lcm(a, b):
    if(b == 0):
        return a;
    else:
        return lcm(b, a % b)
    
num1 = int(input(" Please Enter first Number : "))
num2 = int(input(" Please Enter the Second Number : "))

lcm = (num1 * num2)
print("\n Least_common_multiple ={2}".format(num1, num2, lcm))