print("hello")                            #print is function

name="simran"
age=22
price=23.4

print(type(name))
print(type(age))
print(type(price))


#string can be represent with single, double and triple quotes
name1='simran'
name2="simran"
name3='"simran"'

print(name3)


#In boolean use capital T and F in starting
old=False
new=True

print(type(old))


#none type: which do not hold any value
a=None

print(type(a))


#python is case sensitive captial and small letters have different meaning

"""
This is multi line comment
"""

b=2
c=6

print(b**c)

#assignment operator
num=5
num**=2

print(num)


#type conversion and type casting
d=float("2")
e=4.2

print(d+e)

f=2
f=str(f)

print(type(f))
print(f)


#input from the user by default have the string type
value=int(input("enter your val:"))

print(type(value))
print(value)



#write a program to input 2 numbers and print their sum
num1=int(input("enter your num1:"))
num2=int(input("enter your num2:"))

sum=num1+num2
print(sum)



#write a program to input side of square and print its area
val=int(input("enter val:"))

area=val*val

print(area)


#write a program to input 2 floating point numbers and print their average
val1=float(input("enter val1:"))
val2=float(input("enter val2:"))

average=(val1+val2)/2

print(average)