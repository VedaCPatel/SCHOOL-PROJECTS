n=int(input("Enter a value:"))
a=1
for i in range(n+1,0,-1):
    v=((i-1)*' ')+(a-1)*'*'
    a+=1
    print(v)




