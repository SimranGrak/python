#Assignment Problems
#Python Fundamentals

#Question 1: Ask the user for a string and check whether it is a palindrome or not. A palindrome is a string which is same when we read it forward & backward.Eg-“madam”,“racecar”etc.


str=input("enter the string: ")

temp1=str[::-1]

if(temp1==str):
    print("yes, it is palindrome!")

else:
    print("no, it is not palindrome!")


#Question 2: Given a list of integers compute the average of all numbers in the list.

numbers=[3,6,1,6,4,2,6,4]

sum=0
for i in numbers:
    sum=sum+i
    avg=sum/len(numbers)

print(int(avg))


#Question 3: Input two lists of integers from the user. Merge them into one list and sort the result.
#Eg- list1=[1,2,7], list2=[2,4,5]
result=[1,2,3,54,5,7]


list1=list(map(int,input("Enter the list: ").split()))
list2=list(map(int,input("Enter the list: ").split()))

result=list1+list2

result.sort()

print(result)



#Question 4: Given a tuple of integers, create:
# A tuple of all even numbers
# A tuple of all odd numbers

full_tuple=(1,2,3,4,5,6,7,8,9,10)

even_list=[]
odd_list=[]

for i in full_tuple:
    if(i%2==0):
        even_list.append(i)  

    elif(i%2!=2):
        odd_list.append(i)  


print(tuple(even_list))
print(tuple(odd_list))


#Question 5: Create a dictionary where: 
# a) Keys= student names
# b)Values=marks(integer)
# Write a menu-based program where user presses a key(ʼAʼ,‘Bʼ,‘Cʼ,‘Dʼ)depending on the operation they want to perform on the dictionary:
# 1.A- Add a student
# 2.B-Update marks 
# 3.C-Search for a student
# 4.D-Display all students and marks




dict={}



while True:
  user_type=input("enter the operation(A/B/C/D/E):")
  if user_type=='A':
                name=input("enter the name")
                if dict.get(name)==None:
                    marks=int(input("enter marks:"))
                    dict[name]=marks
                    print(dict)
                else:
                    print("choose another name:")
  elif user_type=='B':
                name=input("enter the name whose marks you want to update:")
                if dict.get(name)==None:
                    print("choose another name!")
                else:
                    marks=int(input("enter the marks:"))
                    dict[name]=marks
                    print(dict)
  elif user_type=='C':
                name=input("enter the name you are searching for:")
                if dict.get(name)==None:
                    print("choose another name!")
                else:
                    print("yes, it exsist!")
  elif user_type=='D':
                print(dict)
  elif user_type=='E': 
         print("exiting program!")
         break
  else:
                print("invalid operation!")


#Question 6: Given a list of words:
words=["apple","banana","kiwi","cherry","mango"]

#Create a dictionary that maps each word to its length

dict={}

for i in words:
       dict[i]=len(i)
       
print(dict)


#Question 7: Write a program that takes a string from the user and prints the number of spaces in the string.
sentence=input("enter the sentence: ")

spaces=0
for i in sentence:
       if(i==" "):
              spaces=spaces+1
  
print(spaces)



#Question 8: Write a program to check whether two lists share no common elements.
#[Hint: use sets]
list1=list(map(int,input("enter the list: ").split()))
list2=list(map(int,input("enter the list: ").split()))

length1=len(list1)
length2=len(list2)

total_length=length1+length2

list1=set(list1)
lsit2=set(list2)

new_set=list1.union(list2)

length3=len(new_set)

if total_length==length3:
       print("no common!")
else:
       print("share common!")



#Question 9: Given a list, print all elements that appear more than once in the list.
#[Hint: use sets]

numbers=[1, 2, 3, 2, 1, 4, 3, 6, 2]

seen=set()
duplicates=set()

for num in numbers:
       if num in seen:
              duplicates.add(num)
       else:
              seen.add(num)

print(duplicates)



#Question 10: Ask the user for a string and print:
# a) All unique characters
# b) The count of unique characters


string=input("enter the string:")

new_set=set(string)

print(new_set)

print(len(new_set))






