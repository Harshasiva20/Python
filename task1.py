# Task - 1
# 1. Display today's date
from datetime import date
today_date = date.today()
print("Today's Date:",today_date)

# 2. Display the current date and time
from datetime import datetime
current = datetime.now()
print("Current date and time:",current)
print(current.strftime("%d-%m-%y %H:%M:%S"))

# 3. calculate person's age from their given DOB
from datetime import date, datetime
dob = datetime.strptime(input("Enter DOB (DD-MM-YYYY): "), "%d-%m-%Y").date()
today = date.today()
age = today.year - dob.year
if (today.month, today.day) < (dob.month, dob.day):
    age -= 1
print("Age:", age) 

# 4. Find number of days inbetween two days
from datetime import date, datetime
date1 = datetime.strptime(input("Enter the date1 (dd-mm-yyyy):"),"%d-%m-%Y").date()        
date2 = datetime.strptime(input("Enter the date2 (dd-mm-yyyy):"),"%d-%m-%Y").date()
difference = abs(date1 - date2)
print("The number of days inbetween are:",difference.days)












