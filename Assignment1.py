#Python Fundamentals (Assignment 1)
#Question 1: Write a program that asks the user for their name and age, then prints a sentence like:
#Hello Shradha, you are 21 years old!

name=input("enter your name:")
age=int(input("enter your age:"))

print("Hello ",name,", your are ",age,"old!")


#Question 2: Take two numbers as input from the user and print their sum, difference, product, and quotient
a=int(input("enter first number:"))
b=int(input("enter second number:"))

print("sum is:",a+b)
print("difference is:",a-b)
print("product is:",a*b)
print("quotient is:",a/b)


#Question 3: Ask the user to enter two integers and one float.Convert them all to floats and print their average.
c=int(input("enter first number:"))
d=int(input("enter second number:"))
e=float(input("enter third number:"))

print("average is:", float((c+d+e)/2))


'''Question 4: The user enters a string containing a number(e.g."45",).Convert it to
a) an integer
b) a float
c)a string again
Print all three values with their types
'''

user=input("enter a number: ")

int_type=int(user)                      #string → integer
                                         #string → float
                                         #string → string
float_type=float(user)
string_type=(user)

print(type(int_type))
print(type(float_type))
print(type(string_type))


#Question 5: Evaluate and print the result of the following expression
x=10+3*2**2

'''Based on what you learnt in thel ecture explain why the output is what it is
first the exponent power will solve and after this multiplication is going to solve and then sum operator is going to solve
10+3*4
10+12
22: Output'''


#Question 6: Write a program to swap values of two numbers entered by the user
value1=int(input("enter first number:"))
value2=int(input("enter second number:"))

value=value1
value1=value2
value2=value

print("first number: ",value1)
print("second number is: ",value2)


'''Question 7: Ask the user for a temperature in Celsius(stringinput). Convert it to float,then calculate and print temperature in Fahrenheit.
Conversion formula:
FahrenheitTemp=(CelsiusTemp *(9/5))+32
'''
CelsiusTemp=float(input("enter temperature in Celcius:"))
FahrenheitTemp=(CelsiusTemp *(9/5))+32

print(FahrenheitTemp)


'''Take the radius(r) as user input and print the area
Use the formula: Area=3.14*r**2'''

r=float(input("enter the radius:"))
Area=3.14*r**2

print(Area)


'''Ask the user for: Principal(P),Rate(R),Time(T). Convert all float to and compute simple interes
SI=(P*R*T)/100'''

P=float(input("enter principal:"))
R=float(input("enter Rate:"))
T=float(input("enter Time:"))

SI=(P*R*T)/100

print(SI)


'''Take a decimal number as input(like 45.78) and output its
a) integer part- 45
b) fractional part- .78
'''

number=float(input("enter the number:"))
decimal_type=int(number)
print(decimal_type)

fractional_type=(number-decimal_type)
print(fractional_type)


