# write a python program to read principle interest, rate of interest, time and display S.I=I=p*r*t/100.

p=int(input("Enter the principle interest: "))
r=int(input("Enter the rate of interest: "))
t=int(input("Enter the time period in years: "))
si=(p*r*t)/100
print("Simple interest for principle Rs.", p, " at the rate of interest ", r, "% in time period of ", t, "years is", si)

