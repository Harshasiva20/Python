money = float(input("Enter the money:"))
shop = input("Shop is open or not(yes/no):")

if(money >= 50):
    if(shop == "yes"):
        print("You can buy a Chocolate")
    else:
        print("Shop is closed")
else:
    print("You're not having Enough Money")