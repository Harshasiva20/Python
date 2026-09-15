#..Created calculator.py file which is a module now importing that module in this main.py file
import calculator
print(calculator.add(5,5))
print(calculator.sub(5,5))
print(calculator.mul(5,5))
print(calculator.div(5,5))



#Task 4
from Student import student_details, calculate_total, calculate_average, find_grade
student_details()

total = calculate_total()
print("Your total marks:", total)

average = calculate_average(total)
print("Your Average mark is:", round(average))

find_grade(average)


#Task 5
from currency import inr_to_usd, inr_to_eur, usd_to_inr, eur_to_inr

inr = float(input("Enter amount in INR: "))
print("USD:", inr_to_usd(inr))
print("EUR:", inr_to_eur(inr))

usd = float(input("Enter amount in USD: "))
print("INR:", usd_to_inr(usd))

eur = float(input("Enter amount in EUR: "))
print("INR:", eur_to_inr(eur))