s=input("Enter a string:")
p=0
s=s.upper()
for i in s[::1]:
    for j in s[::-1]:
        if i==j:
            p="is a palindrome string!"
        else:
            p="is not a palindrome string!"
print(s,"",p)
