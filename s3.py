# Exercise 1A: Create a string made of the first, middle and last character
stg=input("Enter your full name:")
l=len(stg)
a=stg[0]
if l% 2==0:
    b = stg[(l // 2) - 1: (l // 2) + 1]
else:
    b=stg[(l//2)]
c=stg[l-1]
print(a, b, c)



