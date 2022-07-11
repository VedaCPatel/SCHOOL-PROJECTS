N = int(input("Enter a 3-digit number:"))
D1= N // 100
D2= (N % 100) // 10
D3= N % 10

if D1==D3:
    print(N, "is a palindrome number :)")
else:print(N, "is not a palindrome number:(")