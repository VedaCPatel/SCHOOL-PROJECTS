# listing the number of vowels in a string
V=['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
n=0
st=input("Enter a string:")
for c in st[0:]:
    if c in V:
        n=n+1
    else:
        continue
print(n)











