# BOOLEAN INPUT PROGRAM

citizen = input("Are you a Indian (yes/no)?:").lower()== "yes"

if(citizen != "yes" or "no"):
    print("kindly give input as yes/no")
    citizen = input("Are you a Indian (yes/no)?:").lower()== "no"

else:
  age = int(input("Enter you Age:"))

if(citizen and age>=18):
    print("Eligible to vote")
else:
    print("Not Eligible to vote")