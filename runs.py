runs = int(input("Enter the runs:"))

if(runs >= 100):
    print("Century")
elif(runs >= 50):
    print("Half Century")
elif(runs > 0):
    print("Good Innings")
elif(runs == 0):
    print("Duck Out")
else:
    print ("Kindly give right input")