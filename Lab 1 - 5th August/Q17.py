# Q17) Write a Python program to count the number of each character in a text file.

from collections import Counter

def count_characters_in_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    char_count = Counter(text)
    for char, count in char_count.items():
        print(f"{char}: {count}")

file_path = 'example.txt' 
count_characters_in_file(file_path)
