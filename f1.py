# read a paragraph find out the number of upper and lower case letters and no of words and no of digits
def para(a):
    i=0
    j=0
    k=0
    w=len(a.split())
    print("Number of words in the paragraph:", w)
    for c in a:
        if c.islower():
            i=i+1
        elif c.isupper():
            j=j+1
        elif c.isdigit():
            k=k+1
        else:
            continue
    print("Number of uppercase letters :", j)
    print("Number of lowercase letters: ", i)
    print("Number of digits:", k)

st=input("Enter a paragraph:")
para(st)