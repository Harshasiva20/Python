# 1 Question
name = "Harsha"
print("Horizontal:",name)
print("Vertical:")
for letter in name:
    print(letter)

# 2 Question
print("First letter:", name[0])
print("Last letter:", name[-1])

# 3 Question
name = "Harsha"
print("My Name is:")
for letter in name:
    print(letter, end = "")

# 4 Question
print("\n""Total Characters in my name:",len(name))

# 5 Question
print("The data type of my name is:",type(name))

# 6 Question
name1 = name
print("name:",name)
print("name1:",name1)

# 7 Question
print("The memory_id of name:", id(name))
print("The memory_id of name1:",id(name1))

# 8 Question
print("My Name in Capital:",name.upper())

# 9 Question
print("My Name in lowerCase:",name.lower())

# 10 Question
print("First Letter only capital:",name.capitalize())

# 11 Question
name = "Harsha"
for i in range(len(name)):
    print(name[i],"-",i)

# 12 Question
fisrtname = "Harsha"
lastname = "Siva" 
fullname = fisrtname+" "+lastname
print(fullname)

# 13 Question
fullname = "Harsha.S"
print(fullname.split("."))
print(fullname)

# 14 Question
fisrtname, lastname = fullname.split(".")
print(fisrtname)
print(lastname)

# 15 Question
name = "Harsha"
print("Highest character in my name:",max(name))
print("Lowest character in my name:",min(name))
count = 0
for i in name:
    if name.count(i) > 1:
        count += 1
print("Total repeated characters in my name:",count)

