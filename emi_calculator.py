# CALCULATING THE EMI

loan = float(input("Enter the loan amount in INR:"))
month = int(input("Enter the month for repayment:"))
rate = 9
interest_amt = (rate/100)* loan
tot_amt = loan + interest_amt
emi = tot_amt / month

print(f"\nThe loan amount is: {loan}")
print(f"The interest rate is: {rate}")
print(f"The interest amount id: {interest_amt}")
print(f"Total repayable amount: {tot_amt}")
print(f"Total months of repayable: {month}")
print(f"The monthly EMI to pay is: {emi}")
