print("Welcome to Gujarat electricity billing system !")
A=input("\nEnter your name:")
B=int(input("\nEnter your ID number:"))
C=int(input("\nEnter previous meter units:"))
D=int(input("Enter current meter units:"))
Area=int(input("\nEnter 1 for Urban or enter 2 for rural:"))

Un= D-C
fr=Un*1
mc=75


if Area==1:
    c1=3
    c2=4
    c3=5
    c4=6

else:
    c1=2
    c2=3
    c3=4
    c4=5

if Un<=100:
    uc=Un*c1
elif Un<=200:
    uc=(100*c1)+((Un-100)*c2)
elif Un<=300:
    uc=(100*c1)+(100*c2)+((Un-200)*c3)
else:
    uc=(100*c1)+(100*c2)+(100*c3)+((Un-300)*c4)

GM=uc+fr+mc

Tax=GM*(17/100)
NB=Tax+GM
print("\nElectricity bill reciept:-")
print("\nCustomer name:",A)
print("Customer ID:",B)
print("Area which customer belongs to (1 for urban and 2 for rural):",Area)
print("Amounts of units consumed this month=",Un)
print("Gross bill amount=",GM)
print("Net bill amount(Tax included)=",NB)




