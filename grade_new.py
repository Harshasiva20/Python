sub1 = int(input("Enter Subject 1 mark: "))
sub2 = int(input("Enter Subject 2 mark: "))
sub3 = int(input("Enter Subject 3 mark: "))
sub4 = int(input("Enter Subject 4 mark: "))
sub5 = int(input("Enter Subject 5 mark: "))


total = sub1 + sub2 + sub3 + sub4 + sub5
average = total / 5


if sub1 >= 35 and sub2 >= 35 and sub3 >= 35 and sub4 >= 35 and sub5 >= 35:

    if average >= 90:
        grade = "A+"
    elif average >= 70:
        grade = "A"
    elif average >= 50:
        grade = "B"
    elif average >= 35:
        grade = "C"
    else:
        grade = "No Grade"
else:
