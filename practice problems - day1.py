# practice programs

x,x = 20,30
y,y = x+10,x+20
print(x,y)


x,y =2,6
x,y = y, x+2
print(x,y)


"""x,y = 7,2,
x,y,z = x+1, y+3, z+10
print(x,y,z)"""


# swap of two numbers with third variable

a,b = 10,20
c = a
a = b
b = c
print (a,b)

# Swap of two numbers without third variable

a,b = 10,20
b,a = a,b
print (a,b)

#Swap of two numbers without third variable (another method)

a,b = 10,20
a = a+b
b = a-b
a = a-b
print (a,b)

#Arithmetic operators

a = 10
b = 3
print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)
print("Modulus:", a%b)
print("Exponent:", a**b)
print("Floor Division:", a//b)

#Relational operator (==, <, >, <=, >=,ArithmeticError !=)

a = 100
b = 100
print("Equal:", a==b)

#Assignment Operator

a = 10
a += 5
print (a)

a -= 3
print(a)

a *= 2
print(a)

#Membership Operator (in & not in)

print("r" not in "harsha")


#Precedence of operators

a = 10
b = 5
c = 3
print( a+b*c-2)                                                                 



