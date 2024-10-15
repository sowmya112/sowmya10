print("calculator")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
ch=int(input("enter choice(1-4):"))
if ch==1:
    a=int(input("enter A:"))
    b=int(input("enter B:"))
    C=a+b
    print("sum=",C)
elif ch==2:
    a=int(input("enter A:"))
    b=int(input("enter B:"))
    C=a-b
    print("subtraction=",C)
elif ch==3:
    a=int(input("enter A:"))
    b=int(input("enter B:"))
    C=a*b
    print("product=",C)
elif ch==4:
    a=int(input("enter A:"))
    b=int(input("enter B:"))
    C=a/b
    print("quotient=",C)
else:
    print("invalid choice")
    
