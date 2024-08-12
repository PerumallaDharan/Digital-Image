# Q9) Write a Python program to display the examination schedule. (extract the date 
# from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

exam_st_date = (11, 12, 2014)
print("The Examination will start from:")
for i in range(len(exam_st_date)):
    print(exam_st_date[i],end="")
    if i+1 is not len(exam_st_date):
        print(" / ",end="")
