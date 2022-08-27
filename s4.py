# Exercise 4: Arrange string characters such that lowercase letters should come first
st=input("Enter a string:")
c=0
i=0
e=''
f=''
for c in st:
    if c.islower():
        e=e+c
for i in st:
    if i.isupper():
        f=f+i

print(e+f)


