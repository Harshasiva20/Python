# Task 4

def student_details():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    dept = input("Enter your department: ")
    ph_no = int(input("Enter your phone number: "))
    email = input("Enter your email: ")
    return name, age, dept, ph_no, email


def calculate_total():
    english = int(input("Enter your English mark: "))
    math = int(input("Enter your Math mark: "))
    stats = int(input("Enter your Statistics mark: "))
    total = english + math + stats
    return total


def calculate_average(total):
    average = total / 3
    return average


def find_grade(average):
    if average < 50:
        print("Grade is: C")

    elif average <= 60:
        print("Grade is: B")

    elif average <= 70:
        print("Grade is: B+")

    elif average <= 80:
        print("Grade is: A")

    elif average <= 90:
        print("Grade is: A+")

    elif average <= 100:
        print("Grade is: O")

    else:
        print("Invalid input")