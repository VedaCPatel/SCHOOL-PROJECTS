n=int(input("Enter a 3 digit number:"))
r=0
for i in range(n):
    if i**2==n:
        r="It is a perfect number"
        break
    else:
        r="It is not a perfect number"
print(r)#perfect number

#Palindrome number
a=n//100
b=(n//10)%10
c=(n%100)%10
if a==c:
    print("It is a palindrome number!")
else:
    print("It is not a palindrome number!")

#armstrong number
if a**3+b**3+c**3==n:
    print("It is an armstrong number!")
else:
    print("It is not an armstrong number!")



