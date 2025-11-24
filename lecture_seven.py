#again learning strings through Prime course

#indexing: it basically means defines the position of every character
#indexing starts from 0
#python strings are immutable: we cannot assign other value to them

name="simran"

#name[1]="p"                                                #it will through an error
print(len(name))

for i in name:
  print(i)



#slicing

word="i love apnacollege"

print(word[2:8])

print(word[3:len(word)])


print(word[:])


#string formatting
#formatting: dynamic strings(values + variables)

#a) format(): introduced in py3
#it includes placeholder and placement

a=9
b=7
sum=a+b
#normal formatting
print("sum is {}".format(sum))                              #this is for numerical
print("language is {}".format("python"))                    #this is normally inserting the string

#we can multiple placeholders
print("sum of {} and {} is {}".format(a,b,sum))


#index based formatting
print("sum of {1} and {0} is {2}".format(a,b,sum))                   #a,b,sum are assigned inexes
#by default they print in order but if we do not want them in order


#value based formatting
#it is basically used when we want to reuse the variables
print("{a} sum of {b} and {a} is {b}".format(a=8, b=4))


#b)f-strings: introduced in 3.6 version
#in f-strings we use literal string interpolation

b=7
c=5
print(f"sum of {b} and {c} is {a+b}")

#we can print average also
print(f"average of {b} and {c} is {(a+b)/2}")



#Lists in python
#it is mutable: means we can assign value in the list
#meanwhile string is immutable

#find out the specific value and write the index of that value
#in programming we call this search as linear search

nums=[2,3,6,8,7,2]

idx=0

for i in nums:
  if(i==7):
    print(idx)
    break
  idx+=1


#Tuples in python: already discussed in previous lectures



#Given a list of tuples with info(name, subject):
#a) list all unique course
#b) list students enrolled in English
#c) create dictionary( student, set of courses)

info=[
  ("simran","hindi"),
  ("neha","english"),
  ("suman","maths"),
  ("suman","hindi"),
  ("punjab","english"),
  ("simran","english")
]

#a)
unique_couse=set()

for i in info:
    unique_couse.add(i[1])

print(unique_couse)

#b)
names=[]

for i in info:
    if(i[1]=="english"):
       names.append(i[0])

print(names)


#c)

new_dict={}

for name, course in info:
    if(new_dict.get(name)==None):
       new_dict.update({name:set()})
       new_dict[name].add(course)

    else:
       new_dict[name].add(course)       

print(new_dict)





