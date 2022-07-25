#calculating overall percent for boards grade. different method unlike the normal one.
m=int(input("Enter marks in maths:"))
e=int(input("Enter marks in english:"))
s=int(input("Enter marks in science:"))
ss=int(input("Enter marks in social science:"))
h=int(input("Enter marks in hindi:"))
c=int(input("Enter marks in computer:"))

if m<s and m<ss and m<c:
    sml=m
elif s<m and s<ss and s<c:
    sml=s
elif ss<m and ss<s and ss<c:
    sml=ss
else:
    sml=c

mp=((ss+m+s+c)-sml)/3

fp=(e+h+mp)/3

print("Overall percent:",fp,"%")