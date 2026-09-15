days = int(input("Enter the number between 1 to 7:"))

if(days == 1):
    print("Monday")
elif(days == 2):
    print("Tuesday")
elif(days == 3):
    print("Wednesday")
elif(days == 4):
    print("Thursday")
elif(days == 5):
    print("Friday")
elif(days == 6 or days == 7):
    print("Weekend")    
else:
    print("Invalid entry, Days are between 1 to 7,Kindly give right value")
