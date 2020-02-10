'''10-unique_list.py

Write a function that filters unique(unrepeated) all elements of a given list. 
For example : function call: unique_list([1,2,3,3,3,3,4,5,5]) output : [1, 2, 3, 4, 5]'''

# function to get unique values 
def unique(list1): 
	
	# insert the list to the set 
	list_set = set(list1) 
	# convert the set to the list 
	unique_list = (list(list_set)) 
	for x in unique_list: 
		print (x), 
	

list1 =[1, 2, 1, 1, 3, 4, 3, 3, 5,6] 
print("\n The_unique_list") 
unique(list1) 