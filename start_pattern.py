# Increasing Triangle
"""for i in range(1,6):
    for j in range(1,i+1):
        print("*", end=" ")
    print()

# Decreasing Triangle
for i in range(1,6):
    for j in range(i,6):
        print("*", end =" ")
    print()


# Right side triangle
for i in range(1,6):
    for j in range(i,6):
        print(" ", end =" ")
    for j in range(1,i+1):
        print("*", end = " ")
    print()"""

# Box number pattern
r = 3
c = 5
num = 1

for i in range(r):
    for j in range(c):
        print(num, end="\t")
        num = num + 1
    print()