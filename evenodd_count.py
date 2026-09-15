even, odd = 0,0
for i in range(1,11):
    if (i%2 == 0):
        even = even + 1
        print(f" {i} = Even")
    else:
        odd = odd + 1
        print(f" {i} = Odd")
print(f"Total number of Even numbers: {even}")
print(f"Total number of Odd Numbers: {odd}")