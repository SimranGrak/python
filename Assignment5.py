#Assignment Problems

'''
Question 1: Create a program that:
a) opens a file "name.txt" in write mode
b) writes 5 names (one per line) entered by the user
c) then opens the same file in read mode and prints all names
'''


with open("name.txt","w") as f:
  for i in range(5):
    f.write(input("enter name:")+"\n")
  

with open("name.txt", "r") as f:
  print(f.read())


'''
Create a program that:
a) opens a file "log.txt" in append mode
b) adds a new log entry (like "program run successfully")
c) opens the file in read mode and print all logs
'''

with open("log.txt", "a") as f:
  f.write("\n"+"program run successfully")

with open("log.txt", "r") as f:
  print(f.read())



'''
Question 3: Create a program that:
a) has a list of numbers: [5,10,15,20,25]
b) uses a list comprehension to create a new list with only numbers greater than 15
c) prints the new list
'''


list=[5,10,15,20,25]

list1=[val for val in list if val>15]                #in this code append only updates but do not return any value simply returns None value

print(list1)



'''
Create a Python dictionary of 3 cities and their populations. Save it to "cities.json".
a) then load the JSON and print each city and its populaton.
b) Ask the user for a new city and its population -update this info in the json file
'''
import json

py_str={
  "city1":564327,
  "city2":43,
  "city3":34289
}

with open("cities.json","w") as f:
  json_str=json.dump(py_str, f, indent=4, sort_keys=True)
  
print(json_str)


with open("cities.json","r") as f:
  data=json.load(f)

print(data)

city=input("enter new city:")
population=int(input("enter the population of that city:"))

data[city]=population

with open("cities.json","w") as f:
  json_str=json.dump(data, f,indent=4)




'''
Question 5: Write a program that tries to open "data.txt" in read mode. if the file does not exixt, catch the exception and print "File not found!"
'''

try:
  with open("data.txt","r")as f:
    f.read()

except FileNotFoundError:
  print("File not found!")

finally:
  print("END OF ASSIGNMENT!")







