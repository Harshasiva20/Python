from math import ceil,floor
n = int(input("Enter the number of coins:"))
a = ceil(n/2)
count = 0
for i in range(0,a):
    for j in range(i+1):
        print("*",end = " ")
    print()
    count += 1
print(count)