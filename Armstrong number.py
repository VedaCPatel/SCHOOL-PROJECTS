N=int(input("Enter a 3-digit number:"))
D1=N//100
D2=(N%100)//10
D3=N%10
if (D1**3)+(D2**3)+(D3**3)==N:
    print(N, "is an armstrong number !")
else:
    print(N, "is not an armstrong number :(")
