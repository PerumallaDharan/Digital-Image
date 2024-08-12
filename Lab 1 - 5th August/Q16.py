# Q16) Write a Python program that prints long text, converts it to a list, and prints all 
# the words and the frequency of each word.

from typing import Counter

def process_text(text):
    words = text.split()
    
    word_count = Counter(words)
    
    for word, frequency in word_count.items():
        print(f"{word}: {frequency}")

long_text = """
This is a sample text. This text is provided as a sample to test the word frequency counter. 
Feel free to modify the text and test the program with different inputs.
"""
print("\nWord Frequencies:")
process_text(long_text)
