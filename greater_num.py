a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if(a>b and a>c):
    print(f"{a}is greater")
elif(b>a and b>c):
    print(f"{b} is greater")
elif(c>a and c>b):
    print(f"{c} is greater")
else:
    print("All numbers are Equal")