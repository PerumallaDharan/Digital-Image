#Q1) Write a Python program to print the following string in a specific format (see 
# the output).

# s="""
# Twinkle, twinkle, little star, 
#       How I wonder what you are!  
#             Up above the world so high,      
#             Like a diamond in the sky.  
# Twinkle, twinkle, little star,  
#       How I wonder what you are """
# print(s)

#Q2) Write a Python program to find out what version of Python you are using.
# import sys
# print(sys.version)

#Q3) Write a Python program to display the current date and time.
# import datetime
# current=datetime.datetime.now()
# print(current)

#Q4) Write a Python program that calculates the area of a circle based on the radius 
# entered by the user.
# def circle_area(n):
#     area=3.14*(n**2)
#     print(area)
    
# print("Enter the radius of the circle:")
# r=float(input())
# circle_area(r)

#Q5) Write a Python program that accepts the user's first and last name and prints 
# them in reverse order with a space between them.
# fn=input("Enter the first name:")
# ln=input("Enter the last name:")
# print("reversed name:",ln+" "+fn)

#Q6) Write a Python program that accepts a sequence of comma-separated 
# numbers from the user and generates a list and a tuple of those numbersSample 
# data : 3, 5, 7, 23
# ls=list(map(int,input("Enter the data:").split(",")))
# tu=tuple(ls)
# print(ls)
# print(tu)

#Q7) Write a Python program that accepts a filename from the user and prints the 
# extension of the file.
# Sample filename : abc.java
# Output : java
# s=list(map(str,input("Enter the file name:").split(".")))
# print(s[-1])

#Q8) Write a Python program to display the first and last colors from the following 
# list.  color_list = ["Red","Green","White" ,"Black"]
# color_list = ["Red","Green","White" ,"Black"] 
# print(color_list[0],color_list[len(color_list)-1])

#Q9) Write a Python program to display the examination schedule. (extract the date 
# from exam_st_date).  exam_st_date = (11, 12, 2014)
# exam_st_date = (11, 12, 2014)
# print("The Examination will start from:")
# for i in range(len(exam_st_date)):
#     print(exam_st_date[i],end="")
#     if i+1 is not len(exam_st_date):
#         print(" / ",end="")

#Q10) Write a Python program that accepts an integer (n) and computes the value 
# of n+nn+nnn. Sample value of n is 5 , Expected Result : 615
# n=int(input("Enter the number:"))
# print(n+(n*10+n)+(n*100+n*10+n))

# Q11) Write a Python function that takes a sequence of numbers and determines 
# whether all the numbers are different from each other.
# def fun(data):
#     if(len(data)==len(set(data))):
#         print("All the numbers are distinct")
#     else:
#         print("Numbers are not distinct ")
# ls=list(map(int,input("Enter the sequence seperated by comma:").split(",")))
# fun(ls)

#Q12) Write a Python program that creates all possible strings using the letters 'a', 
# 'e', 'i', 'o', and 'I'. Ensure that each character is used only once. 
# import itertools
# chars = ['a', 'e', 'i', 'o', 'I']
# for s in itertools.permutations(chars):
#   print(''.join(s))

#Q13) Write a Python program that removes and prints every third number from a 
# list of numbers until the list is empty
# num=list(map(int,input("Enter the numbers seperated by comma:").split(",")))
# i=2
# while num:
#     print("Removed number:",num.pop(i))
#     if(num):
#         i=(i+2)%len(num)

#Q14) Write a Python program to identify unique triplets whose three elements sum 
# to zero from an array of n integers.
# def three_sum(nums):
#     result = []
#     nums.sort()
#     for i in range(len(nums) - 2):
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue
#         l, r = i + 1, len(nums) - 1
#         while l < r:
#             s = nums[i] + nums[l] + nums[r]
            
#             if s > 0:
#                 r -= 1
#             elif s < 0:
#                 l += 1
#             else:
#                 result.append((nums[i], nums[l], nums[r]))
#                 while l < r and nums[l] == nums[l + 1]:
#                     l += 1
#                 while l < r and nums[r] == nums[r - 1]:
#                     r -= 1
#                 l += 1
#                 r -= 1
#     return result
# num=list(map(int,input("Enter the numbers seperated  by comma:").split(",")))
# print(three_sum(num))

#Q15) Write a Python program to make combinations of 3 digits.
# d=list(map(int,input("Enter the 3 numbers seperated by comma:").split(",")))
# for i in range(0,3):
#     for j in range(0,3):
#         for k in range(0,3):
#             if(i!=j&j!=k&k!=i):
#                 print(d[i],d[j],d[k])

#Q16) Write a Python program that prints long text, converts it to a list, and prints all 
# the words and the frequency of each word.
# text = input("Enter a long text: ")
# word_list = text.split()

# word_freq = {}
# for word in word_list:
#   if word in word_freq:
#     word_freq[word] += 1
#   else:
#     word_freq[word] = 1

# print("All the words and their frequencies:")
# for word, freq in word_freq.items():
#   print(f"{word}: {freq}")

#Q17) Write a Python program to count the number of each character in a text file.
# def count_characters(filename):
#   char_counts = {}
#   with open(filename, 'r') as file:
#     for line in file:
#       for char in line:
#         if char in char_counts:
#           char_counts[char] += 1
#         else:
#           char_counts[char] = 1

#   return char_counts

# filename = 'file.txt'
# counts = count_characters(filename)
# for char, count in counts.items():
#   print(f"Character '{char}': {count}")

#Q18) Write a Python program that retrieves the top stories from Google News.
# from GoogleNews import GoogleNews
# googlenews = GoogleNews()
# googlenews.search('India')
# googlenews.get_page(1)
# result = googlenews.result()
# for x in result:
#   print("-"*50)
#   print("Title--",x['title'])
#   print("Date/Time--",x['date'])
#   print("Description--",x['desc'])
#   print("Link--",x['link'])

#Q19) Write a Python program to get a list of locally installed Python modules.
# import pkg_resources
# installed_packages = pkg_resources.working_set
# installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
#      for i in installed_packages])
# print(installed_packages_list)

#Q20) Write a Python program to display some information about the OS where the 
# script is running
import platform as pl
os_profile = [
    'platform',
    'processor',
    'python_build',
    'python_compiler',
    'python_version',
    'release',
    'system',
    'uname',
    'version',
]
for key in os_profile:
    if hasattr(pl, key):
        print(key + ": " + str(getattr(pl, key)()))
