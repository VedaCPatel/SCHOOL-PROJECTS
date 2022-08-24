""" write a program to read a line of text and display each word and its frequency in each separate line"""
s=input("Enter a string:")
sl=s.split()
for w in sl:
    print("there are",sl.count(w),w,"in this string")
