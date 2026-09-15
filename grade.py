# GARDE OBATINED BY THE STUDENT BASED ON THE MARK SECURED


Tamil = int(input("Enter Tamil mark: "))
English = int(input("Enter English mark: "))
Physics = int(input("Enter Physics  mark: "))
Chemistry = int(input("Enter Chemistry  mark: "))
Maths = int(input("Enter Maths mark: "))


total = Tamil+ English + Physics + Chemistry + Maths
average = total / 5


if Tamil >= 50 and English >= 50 and Physics >= 50 and Chemistry >= 50 and Maths >= 50:

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

    print("\nResult:")
    print("Total =", total)
    print("Average =", average)
    print("Grade =", grade)
    print("Result = PASS")

else:
    print("\nResult:")
    print("Total =", total)
    print("Average =", average)
    print("Grade = No Grade")
    print("Result = FAIL")

    print("\nFailed Subjects:")

if Tamil < 50:
        print("Tamil =", Tamil)

if English < 50:
        print("English =", English)

if Physics < 50:
        print("Physics =", Physics)

if Chemistry < 50:
        print("Chemistry =", Chemistry)

if Maths < 50:
        print("Maths =", Maths)