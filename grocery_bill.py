# CALCULATING TOTAL GROCERY BILL

potato = int(input("Enter the quantity of potato:"))
onion = int(input("Enter the quantity of onion:"))
tomato = int(input("Enter the quantity of tomato:"))

total_amt_potato = potato * 50
total_amt_onion = onion * 45
total_amt_tomato = tomato * 35

print(f"\n Quantity of potato purchased: {potato} \n Total price of potato: ₹{total_amt_potato}")
print(f"\n Quantity of onion purchased: {onion} \n Total price of onion: ₹{total_amt_onion}")
print(f"\n Quantity of tomato purchased: {tomato} \n Total price of onion: ₹{total_amt_tomato}")

tot_amount = total_amt_potato + total_amt_onion + total_amt_tomato
print(f"\n The overall Grocery bill amount: ₹{tot_amount}")
