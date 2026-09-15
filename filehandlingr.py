print("1.Reading the whole file")
print("=========================")
file = open("demofile.txt","r")
read = file.read()
print(read)
print()

print("2.Reading using character size")
print("================================")
file = open("demofile.txt","r")
read = file.read(50)
print(read) 
print()

print("3.Reading by lines")
print("===================")
file = open("demofile.txt","r")
line1 = file.readline()
print(line1,end="")
line2 = file.readline()
print(line2,end="\n")

print("4.Displaying in list structure")
print("================================")
file = open("demofile.txt","r")     #display the output in the form of list
read = file.readlines()
print(read)
print()

print("5.Accessing in for loop")
print("=========================")
file = open("demofile.txt","r")
for f in file:
    print(f,end="")






