# Checking whether the given number is prime number
num = int(input("Enter the number you have to check:"))
count = 0
for i in range(1,num+1):
       if num%i == 0:
           count+=1
if count == 2:
     print(f"{num } is a prime number")
else:
     print(f"{num} is not a prime number")
     
       
# Finding prime numbers within the given range
num1= int(input("Enter the starting number:"))
num2 = int(input("Enter the ending number:"))
for i in range(num1, num2+1):
       count = 0
       for j in range(1, i+1):
         if i%j == 0:
           count+=1
       if count == 2:
             print(i)
       