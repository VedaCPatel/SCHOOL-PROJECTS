# Count all letters, digits, and special symbols from a given string
st=input("Enter a string:")
c1=''
c2=''
c3=''
for i in st:
    if i.isspace():
        continue
    elif i.isdigit():
        c1=c1+i
    elif i.isalpha():
        c2=c2+i
    else:
        c3=c3+i
print("The number of digits in", st, "is", len(c1))
print("The number of letters in", st, "is", len(c2))
print("The number of special symbols in", st, "is", len(c3))



