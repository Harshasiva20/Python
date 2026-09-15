# Sequence Data types in python:
# 1.String  2.List  3.Tuple 4.Set 5.Dictionary 
# List = A list is an ordered, mutable sequence data type           
#        that can store different data types and duplicate values.
# Methods in list = append(), extend(), insert(), remove(), pop(), clear(), index(), count(),
#                   sort(), reverse(), copy().
# List creation = All list is created by enclosing elements inside square brackets[]
#                with each element separated by commas.

#1
students = ["harsha", "gayathri", "thanigai", "mohana", "shakthi"]
#2
print ("The list is:",students)
#3
print("First element:",students[0])
#4
print("Last element:",students[len(students) - 1])   #last element
print("Last element:",students[-1])                  # Another method for last element
#5
print("Lenght of the list:",len(students))
#6
print("Data type of the list:",type(students))
#7
students.append("gokula")
print("Adding new element to the list:",students)
#8
students.insert(2,"mithra")
print("Inserting new element in 2nd position:",students)
#9
students[2] = "nandhitha"
print("Changes in the list at 2nd position:",students)
#10
students.remove("nandhitha")
print("After removing one value:",students)
#11
students.pop(len(students)-1)
print("Remove last item using index:",students)
#12
students.pop()
print("Removing last item from the list:",students)
#13
students.sort()
print("Ascending order:",students)
#14
students.sort(reverse=True)
print("Descending order:",students)
#15
students.reverse()
print("Reversing:",students)
#16
print("Count of the harsha element:",students.count("harsha"))
#17
print("Index of harsha element:",students.index("harsha"))
#18
students_2 = students
print("students_2:",students_2)

#19
if type(students) == type(students_2):
    print("same data type:",type(students))
else:
    print("not same data type")
if students == students_2:
    print("Same list")
else:
    print("Not same")

#20
print("All elements in list using for loop:")
for i in students_2:
    print(i, end = ",")

#21
print("\nAll elements in the list using while loop")
i = 0
while(i < len(students_2)):
    print(students_2[i], end = ",")
    i += 1

#22,23
num = [1,2,3,4,5]
print("\nEven numbers from the list:")
for i in num:
    if i%2 == 0:
        print(i, end =" ")
print("\nOdd numbers from the list:")
for i in num:
    if i%2 != 0:
        print(i, end =" ")

#24
print("\nSum of all numbers in a list")
sum = 0
for i in range(len(num)):
    sum = sum + num[i]
print (sum)

#25
print("Largest number:", max(num))
#26
print("Smallest number:", min(num))

#27
print("Average of the list:")
avg = sum/len(num)
print(avg)

#28
even, odd = 0,0
for i in num:
    if (i%2 == 0):
        even = even + 1
    else:
        odd = odd + 1
print(f"Total number of Even numbers: {even}")
print(f"Total number of Odd Numbers: {odd}")

#29
num_2 = [1,2,2,3,4,4,5,6]
print("Removing dupliactes:")
num_2 = list(set(num_2))
print(num_2)

#30
print("Merge of two list:")
num.extend(num_2)
print(num)

#31
num = [1,2,3,4,5]
num_2 = [1,2,3,4,5,6]
print("Common elements in list:")
for i in num:
    if i in num_2:
      print(i, end=" ")

#32
print("\n2nd largest number in list:")
num_2.sort()
print(num_2[len(num_2)-2])

#33
print("left rotation:")
num = [1, 2, 3, 4, 5]
first = num.pop(0)
num.append(first)
print(num)

#34
print("right Rotation:")
num = [1, 2, 3, 4, 5]
last = num.pop(len(num)-1)
num.insert(0,last)
print(num)

#35
print("checking element 4 exist or not:")
element = 4
if element in  num:
        print(f"element {element} is present")
else:
        print(f"Element {element} is not present")

#36
print("Converting string into list")
name = "Harsha"
name_list = list(name)
print(name_list)
print(type(name_list))

#37
print("Converting list into string")
num_list = [5,4,3,2,1]
numbers = str(num_list)
print(numbers)
print(type(numbers))

#38
print("Split list into two parts:")
num = [1,2,3,4,5]
mid = len(num) // 2
first = num[:mid]
second = num[mid:]
print("First Part :", first)
print("Second Part:", second)

#39
print("swap first and last element:")
first = num[0]
last = num[len(num)-1]
num[0]= last
num[-1] = first
print(num)

#40
print("Frequency of each element:")
num = [1, 3, 2, 2, 3, 4, 3, 5, 5]
for i in set(num):
    print(i, "->", num.count(i))

#41
print("Remove all occuerences of a given element:")
num = [1, 2, 3, 2, 4, 2, 5]
element = 2
new_list = []
for i in num:
    if i != element:
        new_list.append(i)
print(new_list)

#42
print("Squares of numbers from 1 to 20:")
square = []
for i in range(1,21):
    sq = i*i
    square.append(sq)
print(square)

#43
print("Adding 2 integers, 1 float, 1 boolean:")
data_list = [67,89,44.576, True]
square.extend(data_list)
print(square)

#44
print("Integer elements and their count:")
new_data = ["harsha",33,78,"gayathri",87]
new_data_list = []
count =0
for i in new_data:
    if type(i) == int:
        count += 1
        new_data_list.append(i)
print("Integer list:",new_data_list)
print("The count of integer elements are:",count)

#45
print("Finding empty list:")
data = [[1, 2], [], [3, 4], [], [5]]
for i in range(len(data)):
    if data[i] == []:
        print("Empty list found at index", i) 

#46
print("Copying the list:")
list1 = [6,7,8,9]
list2 = list1
print("list 1:",list1)
print("list 2:",list2)
list1.append(1)
print("list 1:",list1)
print("list 2:",list2)

#47
print("Deleting the list and its elements:")
del list2
print(list2) 

#48
print("join method:")
trip = ["i'm","Travelling","to","USA"]
print("_".join(trip))

#49
print("Remove the vowels:")
letters =["a","b","c","d","e","f","g","h","i","j"]
vowels = ["a","e","i","o","u"]
for i in vowels:
    if i in letters:
        letters.remove(i)
print(letters)         

