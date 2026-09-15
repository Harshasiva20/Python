number = int(input("Enter the number:"))
fact = 1
if number == 0:
    print("1")
else:
    for i in range(1,number+1):
        fact = fact*i
print(f"Factorial of the {number} is:{fact}")