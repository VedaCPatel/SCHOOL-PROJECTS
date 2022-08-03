# write a python program to display largest numbers of given 3 numbers
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))

if a==b==c:
    print("All the three numbers are equal !")
elif a>b and a>c:
    print(a, " is the largest number out of the three numbers ! ")
elif b>a and b>c:
    print(b, " is the largest number out of the three numbers !")
else:
    print(c, " is the largest number out of the three numbers !")

