# CONVERT DAYS INTO YEARS, MONTHS AND DAYS - (INPUT - NO OF DAYS)

days = int(input("Enter the number of days: "))

years = days // 365

months = days // 30
days = days % 30


print("\nConverted Time")
print("Years :", years)
print("Months:", months)
print("Days  :", days)