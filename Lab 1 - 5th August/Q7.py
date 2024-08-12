# Q7) Write a Python program that accepts a filename from the user and prints the 
# extension of the file.
# Sample filename : abc.java
# Output : java

filename = input("Enter a filename: ")
extension = filename.split(".")
print("Extension:", extension[-1])
