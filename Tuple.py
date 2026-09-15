#1 
flowers = ("Jasmine","Rose","Hibiscus","Daisy","Sunflower")
print(f"\nFlowers:{flowers}")
print("Data type:",type(flowers))

#2
f1,f2,f3,f4,f5 = flowers
print()
print(f1)
print(f2)
print(f3)
print(f4)
print(f5)

#3
print("\nFirst element:",flowers[0])
print("Last element:", flowers[(len(flowers)-1)])

#4
print("\nLength of the tuple is:",len(flowers))

#5
print("\nMemory ID of flowers:",id(flowers))

#6
print("\nAll elements in tuple:")
for i in flowers:
    print(i)
    
#7
print("\nCount of all elements in tuple:")
flowers1 = ("Jasmine","Rose","Hibiscus","Daisy","Sunflower","Daisy")
for i in set(flowers1):
    print(f"{i}:{flowers1.count(i)}")

#8
print("\nIndex of tuple elements:")
for i in flowers:
  print(f"Index of {i}:{flowers.index(i)}")

#9
print("\nFirst 3 elements:",flowers[:3])

#10
print("\nLast 3 elements:",flowers[(len(flowers)-3):])

#11
print("\nSkip 1st and print rest:",flowers[1:])

#12
print("\nSkip last and print rest:",flowers[:(len(flowers)-1)])

#13
print("\n2nd to next 2 elements:",flowers[1:(len(flowers)-1)])

#14
print("\nElement present or not:")
element = "Daisy"
if element in flowers:
   print(f"Element {element} found at {flowers.index(element)}")

#15
flowers = flowers+("Lilly",)
print("\nNew element:",flowers)

#16
flowers = flowers[:3] + ("Lotus",) + flowers[3:]
print("\nNew element at 3rs index:",flowers)

#17
print("\nCombine two tuple:")
a = (1,2,3)
b = (4,5,6)
c = a + b
print(c)

#18
print("\nCombine two tuple and check:")
a = (1,2,3)
b = (4,5,6)
c = a + b
print(c)
if a==b==c:
   print("Same")
else:
   print("Different")

#19
print()
name = ("Mastering in python")
for i in range(3):
  print(name, end = "\t")

#20
print("\nCount:")
numbers = (5,8,5,2,5,6,5)
for i in numbers:
   if i == 5:
      count =  numbers.count(i)
print(i,"=",count,"times")   

#21
print("\nConvert tuple into list:")
data = (10,20,30,40)
list1 = list(data)
print("list:",list1)

#22
print("\nConver list into tuple:")
tuple1 = tuple(list1)
print(tuple1)

#23
marks = [100,200,300,400]
print("\nMaximum:",max(marks))
print("Minimum:",min(marks))

#24
student = ("Arun", 21, "CSE")
name,age,dept = student
print("\nName:",name)
print("Age:",age)
print("Dept:",dept)

#25
print("\n3 Tuples combine:")
a = (1,3,5)
b = (2,4,6)
c = (8,9,0)
d = a + b + c
print("Tuples:",d)

#26
print("\nRemove dupliactes:")
numbers = (5,8,5,2,5,6,5)
for i in set(numbers):
   print(i, end =" ")

#27
print("\nSort the tuple:")
number = (7,2,9,5,4,1)
print("\nAscending order:",sorted(number))

#28 = Real time [List]
available_quantity = ["Tv","Refridgerator","Washing Machine","Air Conditioner"]
Stock = [200,125,150,200]

print("\nBefore Delivery Stock:")
print("==========================")
for i in range(len(available_quantity)):
    print(available_quantity[i],":",Stock[i])

item = input("\nEnter the item:").title()
quantity = int(input("\nEnter the quantity:"))

if item in available_quantity:
   index = available_quantity.index(item)
   if Stock[index] >= quantity:
      Stock[index] = Stock[index] - quantity
      print(f"{available_quantity[index]} Delivered")
   else:
      print("Insufficient Quantity")
else:
   print("Item Not Available")

print("\nUpdated Stock:")
print("===================")
for i in range(len(available_quantity)):
   print(available_quantity[i],":",Stock[i])

#29 = Real time (Tuple)
available_quantity = ("Tv","Refridgerator","Washing Machine","Air Conditioner")
Stock = (200,125,150,200)

print("\nBefore Delivery Stock:")
print("==========================")
for i in range(len(available_quantity)):
    print(available_quantity[i],":",Stock[i])

item = input("\nEnter the item:").title()
quantity = int(input("\nEnter the quantity:"))

if item in available_quantity:
   index = available_quantity.index(item)
   if Stock[index] >= quantity:
      list_stock = list(Stock)
      list_stock[index] = list_stock[index] - quantity
      Stock = tuple(list_stock)
      print(f"{available_quantity[index]} Delivered")
   else:
      print("Insufficient Quantity")
else:
   print("Item Not Available")

print("\nUpdated Stock:")
print("===================")
for i in range(len(available_quantity)):
   print(available_quantity[i],":",Stock[i])




