#File I/O
'''
In python we have different types of files .text, .csv files so there we use the concept of file I/O operations, functions
in large models we need to take the data from different files
'''

#FILE OPERATIONS: open, read, close
f=open("sample.txt","r")
'''
r-> read
w-> write
there is a pointer type concept
'''

data=f.read()        # or we can readline to read line by line
print(data)
f.close()                               #it is manadtory to close the file after operation otherwise it create bug

#next is write operation: when we use this operation we overwrite our full file

f=open("sample.txt", "w")

f.write("this is suman\n hello")

f.close()


'''
LIST OF ALL FILE OPERATIONS
r-> reading(default)
w-> writing, truncates file first(it overwrite whole file)
x-> creates new and open for writing
a-> writing, appends at end
b-> binary mode
t-> text mode(default)
+-> opens disk file for update(r and w)

by default if we do not have any file then the w and a operation create the file and write something
'''

f=open("sample.txt", "a")

f.write("\n ekwndmsa\n frwedhjqk")

f.close()


#creating new file and write

# f=open("sample4.txt","x")

# f.write("hello champ!")
# f.close()

# a dn w operation by default creates new file and perform write operation
f=open("sample3.txt","a")

f.write("hello champ!")
f.close()


'''binary file example: audio files and video files
rt: read text file which is by default
rb: read binary files
wt: write text file
wb: write binary file
'''

#(+) operation which combines multiple operations
#a+, w+, r+

f=open("sample.txt","r+")

f.write("123")
print(f.read())        #the remaining text started reading
f.close()

#we have to imagine things in the form of pointer


# with keyword: in this keyword we do not need to explicitly close it automatically do after perfoming all operations our file which also better to avoid our file from corruption

with open("sample.txt","r") as f:
  data=f.read()
  print(len(data))
  print(f.read())



#delete files: special module is followed which is called a os(operating system) module
#it basically delete the particular file

import os

os.remove("sample3.txt")



'''ACTIVITY: WORD SEARCH
we have find the hello word in the file and if exist tell on which it exist
'''
data=True
line=1
word="hello"

with open("sample.txt","r") as f:
  while data:
     data=f.readline()

     if("hello" in data):
       print(f"{word} found at line {line}")
       break
     
     line+=1




#Exception handling: try, except, else, finally
'''
try: that part of code which might cause an error
finally: it runs whether there is any error or not
'''

try:
  number=int(input("enter any number:"))
  ans=10/number

except ZeroDivisionError:
  print(f" division by zero is not allowed!")

#we can write multiple exceptions here

else:
  print(f"ans is {ans}")

finally:
  print("end of code!")





'''
LIST COMPREHENSIONS: is a simple and concise way to do already made things
'''
#traditional way
#WAP to store the squares of numbers in list
squares=[]

for i  in range(6):
  squares.append(i*i)

print(squares)


#now we have more efficient way to do this with list comprehension
#[output for item in iterable if condition]-> format in list comprehension
sq=[i*i for i in range(6)]
print(sq)

#and if want to store the squares of only odd numbers
sq=[i*i for i in range(10) if i%2!=0]
print(sq)


#WAP to overwrite the numbers with zero if they are negative
nums=[-2,-9,0,5,3,-5]

nums=[0 if val<0 else val for val in nums]
print(nums)

#we can perform some functions inside the output



'''JSON Module
JSON(Javascript Object Notation): it is a popular format of storing the data like we have .csv and .txt format
In json we have key value pairs like dictionary in python
In json we have array but in python we call them list
In python we have dictionary but in json we call object
In python we have string but in json we have string
similarly in python we have None data type but in json we call null 
loads: it is used to convert json format into python
dumps: it is used to convert python format into json format
s in loads and dumps denotes the string
'''

import json

#convert json into python

json_str='{"name":"simran","isTeacher":true}'

py_obj=json.loads(json_str)

print(type(py_obj), py_obj)


#similary convert python into json

py_str={
  "name":"simran",
  "age":34,
  "isTeacher":True,
  "address":{
    "city":"karnal",
    "country":"India"
  }
}

json_stri=json.dumps(py_str)

print(type(json_stri), json_stri)

#if we deal with dictionary and string then we use loads and dumps

#but if we deals with files we use two functions a) load: is to read the json data and b) dump: it is to write in the json data

#reading json fromat data
import json

with open("data.json","r") as f:
  py_obj=json.load(f)

  print(type(py_obj), py_obj)


#writing python data into json data so we use here dump
import json

data={
  "company":"HCLTech",
  "city":"karnal"
}

with open("data.json","w") as f:
  json.dump(data, f, indent=4, sort_keys=True)



  






