# Q13) Write a Python program that removes and prints every third number from a 
# list of numbers until the list is empty.

def remove_every_third(numbers):
    index = 2  
    while numbers:
        if index >= len(numbers):
            index = index % len(numbers)
        print(numbers.pop(index))
        index += 2 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
remove_every_third(numbers)
