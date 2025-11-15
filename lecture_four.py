#dictonary in Python
#dictionaries are used to store data values in key: value pairs
#dictionary is mutable, unordered(no indexes are there) and do not allow duplicate keys

dict={
  "name": "simran",
  "age": 22,
  "career":"btech",
  "city":"karnal",
  "marks":[90,78,90]
}

print(type(dict))

dict["city"]="noida"
print(dict)


#accessing particular element in dictionary
print(dict["marks"])


#we can also add the key: value in the dictionary as this is mutable
dict["job"]="Associate"

print(dict)

#null dictionary
null_dict={}

print(null_dict)

#add value in null dictionary
null_dict["name"]="simran"

print(null_dict)


#nested dictionary
dict1={
  "name":"simran",
  "marks":{
    "phy":98,
    "chem":90,
    "maths":99
  },
  "age":22
}

print(dict1["marks"]["chem"])                     #accessing particluar element in nested dictionary



#dictionary special methods
#1. keys: to return all keys in dictionary
print(dict.keys())

#we can type caste the key in different data type like list or tuple
print(list(dict.keys()))                          #list
print(tuple(dict.keys()))                         #tuple

#or we can find the length of dict through keys
print(len(dict.keys()))

#length of dictionary
print(len(dict))



#2. keys: to return all values in dictionary

print(dict.values())
print(dict1.values())                                   #returns the nested values also


#3. items: returns key: value pairs as tuples
print(dict.items())

print(list(dict.items()))


#we can individually access these tuples
pairs=list(dict.items())

print(pairs[0])



#4. get method: in python which returns the particular value of that key
print(dict.get("name"))

#or we can simple print the value of particular key
print(dict["name"])

#but the difference between them is get method when we type wrong key it simply prints none
#but the simple methods returns error which do not execute the after code

#5. update method: which is used to return the new key: value pair in dictionary
#or either they are used to overwrite the existing note: value not the key because keys are unique
print(dict.update({"name":"robin"}))

print(dict.update({"company":"HCLTech"}))
print(dict)





#Sets in Python
#sets stores unordered items and they are unique and mutable but elements in the sets are immutable

nums={1,2,3,5,5,2,"simran","simran"}            #it contains duplicate values but in output it returns only unique values, basically it ignores duplicate values

print(type(nums))
print(nums)


#how to create empty set
collection={}                            #it return the type of dictionary
print(type(collection))

#so we create empty set like
collection1=set()

print(type(collection1))


#set methods
#1. add method: it is used to add method in set
collection1.add(3)
collection1.add(4)
collection1.add(5)

print(collection1)

#2. remove method: it is used to remove method in set
collection1.remove(3)

#if we try to remove the value which do not exist
#collection1.remove(7)                               #it will return the key error, basically the value is key here

print(collection1)


#unhasable: which values change and whose hasing value comes different later: like dictionary and list
#collection1.add([1,2,3])                              #this will return typeError: unhasable list beacuse the list change according to time
print(collection1)

collection1.add((1,2,3))
print(collection1)


#3. clear: it is used to empty the set
collection1.clear()
print(len(collection1))
print(collection1)


#4. pop: it is used to remove the random values from the set
collection2={"hello","simran","grak"}
print(collection2.pop())
print(collection2.pop())



#important other sets method
#5. union method: combines both set values and return unique values and returns new set
set1={1,2,3}
set2={2,3,4}

print(set1.union(set2))
print(set1)
print(set2)              #set 1 and set 2 returns their old value and the new set will be made after union


#6. intersaction: it will combines common values and returns new set
print(set1.intersection(set2))


#Question 1: store following word meanings in a python dictionary
#table: "a piece of furniture", " list of facts and figures"
#cat: "a small animal"

words={
  "table": ["a piece of furniture","list of facts and figures"],
  "cat":"a small animal"
}

print(words)


#Question 2: you are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students
# "python","java","c++","python","javascript","java","python","java","c++","c"

subjects={"python","java","c++","python","javascript","java","python","java","c++","c"}

print(subjects)
print(len(subjects))


#Question 3: WAP to enter marks of 3 subjects from the user and store them in  a dictionary. Start with an empty dictionary and add one by one. Use subject name as key and marks as value.

subjects1={}
print(type(subjects1))

x=int(input("enter marks: "))
subjects1.update({"chem":x})
y=int(input("enter marks: "))
subjects1.update({"maths":y})
z=int(input("enter marks: "))
subjects1.update({"phy":z})
print(subjects1)


#Question 4: Figure out a way to store 9 and 9.0 as separate values in a set.(you can take help of built-in data types)
values={
  ("int",9),("float",9.0)
}

print(values)