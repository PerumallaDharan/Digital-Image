# Q12) Write a Python program that creates all possible strings using the letters 'a', 
# 'e', 'i', 'o', and 'I'. Ensure that each character is used only once. 

import itertools

def generate_strings():
    letters = ['a', 'e', 'i', 'o', 'I']
    permutations = itertools.permutations(letters)
    for p in permutations:
        print(''.join(p))

generate_strings()
