# Q11) Write a Python function that takes a sequence of numbers and determines 
# whether all the numbers are different from each other.

def fun(data):
    if len(data) == len(set(data)):
        print("All numbers are distinct")
    else:
        print("All numbers are not distinct")

ls=list(map(int,input("Enter the numbers: ").split()))
fun(ls)



