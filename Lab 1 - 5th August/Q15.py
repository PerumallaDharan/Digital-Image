# Q15) Write a Python program to make combinations of 3 digits.

import itertools

def generate_combinations():
    digits = '0123456789'
    combinations = itertools.combinations(digits, 3)
    for combo in combinations:
        print(''.join(combo))

generate_combinations()
