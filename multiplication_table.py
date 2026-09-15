n = int(input("Enter the number:"))
r = int(input("Enter the range:"))
print(f"Multiplication Table of {n}")
for i in range (1,r+1):
    print(f"{n} * {i} = {n*i}")