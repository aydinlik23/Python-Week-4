'''8-counter.py

Write a function that takes an input from user and than gives the number of upper case letters and smaller case letters of it. 
For example : function call: counter("asdASD") output: smaller letter : 3 upper letter : 3'''

def counter(word):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for x in word:
        if x.isupper():
           d["UPPER_CASE"]+=1
        elif x.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", word)
    print ("Numb. of Upper letters : ", d["UPPER_CASE"])
    print ("Numb. of Lower letters : ", d["LOWER_CASE"])

counter('asdASD')