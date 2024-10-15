DAA=float(input("enter marks:"))
DM=float(input("enter marks:"))
OS=float(input("enter marks:"))
SE=float(input("enter marks:"))
C=float(input("enter marks:"))
total=(DAA+DM+OS+SE+C)/5
print("your marks in percentage is",total,"%")
if total>95:
    print("grade:0")
elif total>80 and total<90:
    print("grade:A")
elif total>70 and total<80:
    print("grade:B")
else:
    print("grade:F")   