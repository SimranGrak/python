#strings

#concatention
str1="simran"
str2="grak"

com=str1+str2

print(com)

#escape sequence characters
line="this is very bad\nsimran"

line2="i hate you \tsimran"

print(line2)
print(line)


#while we calculate the length of string it also include spaces also
line3="i hate you \tsimran"

print(len(line3))


#indexing: every character in python is assigned a unique identity
str="simran grak"

ch=str[5]
print(ch)

#we cannot change the value of character through indexing
#it does not support item assignment
#str[4]="r"
print(str)


#slicing: very important topic in terms of Machine learning
#slicing: accessing the part of string
#and one main thing ending index never include 
str1="simran robin"

ch1=str1[2:12]

# or

ch2=str1[2:]

# or

ch3=str1[2:len(str1)]

#above all print the same output

print(ch3)
print(ch2)
print(ch1)

ch4=str1[:7]            #this is also follow the same pattern as above

print(ch4)


#negative index: it is the feature available only in python
str2="simran"



print(str2[-3:-1])


#some important python functions
name="i am deeply attached with my Robin"

print(name.endswith("bin"))

print(name.capitalize())           #this function capitalize the first character of string
#also keep in mind it do not make the change into oringianl string It do only one time change

print(name)     #i am deeply attached with my Robin

#if we want the permanent change into string then we simply mention in the string in the first
name=name.capitalize()
print(name)


#replace function: which replace the old value with new value
print(name.replace("robin","Robin Chaudhary"))      #it also make the one time change

print(name)


#find function: find the character in the particular string
print(name.find("m"))  


#count function: this function simply counts the occurance of that particular character of the string
print(name.count("robin"))



#question 1: Write a program to input user's name and print its length
user=input("enter your legal first name:")
print(user)
print(len(user))

#question 2: write a program to find the occurrence of '$' in a string
user1="hi i usually earns $5000 per month and he earns $7000 per mnonth"

print(user1.count("$"))




#New concept: Conditional statements
age=int(input("enter age of student:"))

if(age>18):
    print("can vote")                              #must include 4 spaces(indentation)
elif(age==18):
    print("make your voter ID")
else:
    print("need to wait")


#question: Grade based on marks
marks=int(input("enter marks of the student:"))

if(marks>=90):
    Grade= "A"
elif(marks>80 and marks<90):
    Grade= "B"
elif(marks>70 and marks<80):
    Grade= "C"
else:
    Grade= "D"

print("marks of the student are:",Grade)



#nesting: One statement inside other statement
age1=90

if(age>18):
    if(age>90):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")


#question 1: WAP to check if a number entered by user is odd or even
number=int(input("enter number:"))

if(number%2==0):
    print("even")
else:
    print("odd")


#queston 2: WAP to find the greatest of 3 numbers entered by the user
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))

if(a>b and a>c):
    print("first number is greater:",a)
elif(b>a and b>c):
    print("second number is greater:",b)
else:
    print("third number is greater:",c)



#queston 3: WAP to find the greatest of 4 numbers entered by the user
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
d=int(input("enter fourth number:"))

if(a>b and a>c and a>d):
    print("first number is greater:",a)
elif(b>c and c>d):
    print("second number is greater:",b)
elif(c>d):
    print("third number is greater:",c)
else:
    print("fourth number is greater")







#question 4: WAP to check if a number is multiple of 7 or not.
number1=int(input("enter the number1:"))

if(number1%7==0):
    print("multiple of 7")
else:
    print("not multiple of 7")



