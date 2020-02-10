'''9-alphabetical_order.py

Write a function that takes an input form user which separates the words hyphen icon(-) and 
sort the words alphabetical order and then adds hyphen icon (-) between them and gives the output of it.
For example: input= green-red-yellow-black-white output= black-green-red-white-yellow'''

def list(order):
    for x in order:
        print(x)
color = ['Green', 'Red', 'Yellow', 'Black', 'White']
list = sorted(color)
print(list)