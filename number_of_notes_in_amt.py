# NUMBER OF 500, 200, 100, 50 IN GIVEN AMOUNT

amount = int(input("Enter the amount: "))

note500 = amount // 500
amount = amount - (note500*500)           #amount = amount % 500

note200 = amount // 200
amount = amount - (note200*200)

note100 = amount // 100
amount = amount - (note100*100)

note50 = amount // 50
amount = amount - (note50*50)

print("\nNumber of Notes")
print("500 =", note500)
print("200 =", note200)
print("100 =", note100)
print("50 =", note50)

print("Remaining Amount =", amount)