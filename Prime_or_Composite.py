
n=int(input("Enter a number:"))
f=0
p=[2,3,5,7]
o=[1,0]
for i in range(2,10):
    if n in o:
        print("It is neither a prime nor a composite number!")
        break
    elif n in p:
        break
    elif n%i==0:
        f+=1
if f==0:
    if n!=1 and n!=0:
        print("It is prime number!")
elif n!=0 and n!=1:
    print("It is a composite number!")



