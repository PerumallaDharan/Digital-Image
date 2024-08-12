# Q6) Write a Python program that accepts a sequence of comma-separated 
# numbers from the user and generates a list and a tuple of those numbers
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')


input_data = input()
number_list = input_data.split(',')
number_tuple = tuple(number_list)
print("List:", number_list)
print("Tuple:", number_tuple)
