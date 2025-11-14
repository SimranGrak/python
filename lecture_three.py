#List in python
#List are like the array: They store multiple values of different data types
#meanwhile array in other languages(c++, java) store only similar type of elements but here list stores different data types

student=["simran",12,"Hindi",45.7]

print(student[3])



#list are mutable: means changeable
#we can change the value of any element in list
student[2]="english"
print(student)                         #output: ["simran",12,"english",45.7]



#list slicing  similar as in string
marks1=[24,67,89,90,44,98]

print(marks1[2:5])


#negative slicing similar as in string
print(marks1[-4:])


#list methods
#Append menthod: which insert the element in the last of the list
marks2=[45,67,90,89,78,12,83]
marks2.append(67)      #it makes the change in list but it returns none
print(marks2)                 #now here the changes will be listed after inserting value

#sort method: which sort the list: by default in ascending order
marks2.sort()         #similar as append it also returns none but it sorts the whole list
print(marks2)                #now it returns the sorted list


#sorting in list of string elements
fruits=["apple","mango","banana","orange","grapes"]
#fruits=fruits.sort()           #this is wrong way to sort
fruits.sort()
print(fruits)



#sort in descending oder in list
marks3=[46,33,89,67,47,25,90]
marks3.sort(reverse=True)
print(marks3)


#reverse in list: change permanently
marks3.reverse()
print(marks3)


#insert element in between the list
marks4=[67,89,45]
marks4.insert(1,78)
print(marks4)


#remove method: it removes the first occurance of that element
list=[1,4,1,5,7]
list.remove(1)
print(list)


#pop method: it deletes the element at particular index
list.pop(3)
print(list)





#Built-in datatype: Tuple
#similar as list but is immutable(assignment is not allowed, means cannot change the value) and enclosed in curly brackets
tup=(2,4,1,5)
print(type(tup))
print(tup)

#if there is a single value in tuple separate with comma otherwise python will consider that value as int, float, string
tup1=(1,)
print(tup1)
print(type(tup1))


#slicing in tuple: similar as string and list
tup3=(3,2,6,5,8)     #-1,-2,-3,-4
print(tup3[2:5])

#negative slicing similar as in string and list
print(tup3[-3:-1])               #-1: means 8 is excluded in python
print(tup3[-3:])



#tuple methods
#1. index: returns the index of first occurance of the element
tup4=(1,4,6,4,3,7,4)
print(tup4.index(6))


#2. count: returns the count of element in the tuple
print(tup4.count(4))



#Question 1: WAP to ask the user to enter names of their 3 favourite movies and store them in a list
movie1=input("enter first movie:")
movie2=input("enter second movie:")
movie3=input("enter third movie:")

movies=[]
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)


#Question 2: WAP to check if a list contains a palindrome of element   (Hint: use copy() method)
palindrome=[1,2,3,5,1]

pal=palindrome.copy()

pal.reverse()

if(palindrome==pal):
    print("yes, it is palindrome")
else:
    print("no, it is not palindrome")


#Question 3: WAP to count the number of students with the "A" grade in the following tuple
grade=("C","D","A","A","B","B","A")

print(grade.count("A"))


#store the above values in a list and sort them from "A" to "D"
grade1=["C","D","A","A","B","B","A"]

grade1.sort()
print(grade1)
