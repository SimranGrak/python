#Assignment Problems

'''Concept: Classes and Objects
Question 1: Create a BankAccount class with,attributes account_number, owner_name, and balance
Add methods to deposit, withdraw and check_balance
'''


class BankAccount:
   def __init__(self,account_number, owner_name, balance):
      self.account_number=account_number
      self.owner_name=owner_name
      self.balance=balance

   def deposit(self,amount):
      self.balance+=amount
      print(f"Deposited: {amount}")
      print(f"total balance: {self.balance}")

   def withdraw(self, amount):
      if amount>self.balance:
         print("insufficient balance")
      else:
         self.balance-=amount
         print(f" withdrawn: {amount}")
      print(f"total balance: {self.balance}")

   def check_balance(self):
      print(f"total balance: {self.balance}")


Person1=BankAccount(4632718,"simran",50000)

Person1.deposit(20000)


'''
Concept: Classes and Objects
Question 2: Create a class Book with the following attributes:
1. title
2. author
3. list of reviews
And add methods to:
1. add a new review
2. count reviews
3. display all reviews
'''

class Book:

   def __init__(self, title, author):
      self.title=title
      self.author=author
      self.reviews=[]               #empty list
      
   def new_review(self,review):
      self.reviews.append(review)

   def count_review(self):
      print(len(self.reviews))

   def displayAll_reviews(self):
      for r in self.reviews:
         print(r)


Book1=Book("harry potter","RK gupta")

print(Book1.title, Book1.author)

Book1.new_review("nice!")
Book1.new_review("Good!")

Book1.count_review()

Book1.displayAll_reviews()



'''
Concept: Encapuslation
Question 3: Create a class Student with private attributes _name, _roll_no, and _marks. Provide getter and setter methods with validation (e.g, marks cannot be negative, roll number has to be between 1 & 100 name cannot be empty)
'''

class Student:
   def __init__(self,name, roll_no, marks):
      self.__name=name
      self.__roll_no=roll_no
      self.__marks=marks

   def get_marks(self):
      if(self.__marks>0):
         print(f"marks are: {self.__marks}")

   def roll_no_range(self):
      if( self.__roll_no>1 and self.__roll_no<100):
         print(f"roll no is: {self.__roll_no}")

   def get_name(self):
      if(self.__name!=""):
         print(f"name is: {self.__name}")


Student1=Student("simran",12,99)

Student1.get_marks()
Student1.roll_no_range()
Student1.get_name()



'''
Concept: Function Overriding
Question 4: Create a class Shape with a method area()
Create a subclass Circle, Rectangle, and Triangle that override the area() method
'''
class Shape:
   def area(self):
      print("Area")

class Circle(Shape):
   def __init__(self,r):
      self.r=r

   def area(self):
      Area=3.14*self.r*self.r
      print(Area)

class Rectangle(Shape):
   def __init__(self,length, breadth):
      self.length=length
      self.breadth=breadth
   
   def area(self):
      Area=self.length*self.breadth
      print(Area)

class Triangle(Shape):
   def __init__(self,base, height):
      self.base=base
      self.height=height
   
   def area(self):
      Area=0.5*self.base* self.height
      print(Area)

Shape1=Shape()
Shape1.area()

Circle1=Circle(3)
Circle1.area()

Rectangle1=Rectangle(2,3)
Rectangle1.area()

Triangle1=Triangle(2,4)
Triangle1.area()




'''
Concept: Inheritance
Question 5: Create a base class Vehicle with attributes like brands and models. Create two subclasses Car and Bike that add extra attributes - seats (in car) and engine_cc(in Bike)
'''

class Vehicle:
   def __init__(self, brands, models):
      self.brands=brands
      self.models=models

class Car(Vehicle):
   def __init__(self,brands,models,seats):
      super().__init__(brands,models)
      self.seats=seats

class Bike(Vehicle):
   def __init__(self,brands,models, engine_cc):
      super().__init__(brands,models)
      self.engine_cc=engine_cc 


Car1=Car("Fortuner","topeModel",8)    
print(Car1.brands, Car1.models, Car1.seats)

Bik1=Bike("splender","oldModel",2)
print(Bik1.brands,Bik1.models, Bik1.engine_cc)


'''
Concept: Abstraction
Question 6: Create an abstract class Employee with and abstract method calculate_salary()
Create subclasses Intern, FullTimeEmployee, and ContractEmployee that implement the method differently
'''

from abc import ABC, abstractmethod

class Employee(ABC):
   @abstractmethod
   def calculate_salary(self):
      pass

class Intern(Employee):
   def calculate_salary(self):
      print("Intern salary!")

class FullTimeEmployee(Employee):
   def calculate_salary(self):
      print("Fulltime salary!")

class ContractEmployee(Employee):
   def calculate_salary(self):
      print("contact base salary!")

Intern1=Intern()
Intern1.calculate_salary()

FullTimeEmployee1=FullTimeEmployee()
FullTimeEmployee1.calculate_salary()

ContractEmployee1=ContractEmployee()
ContractEmployee1.calculate_salary()


'''
Concept: Constructor Overloading(with Default Parameters)
Question 7: Create a class Person that allows the constructor to work with:
1. name only
2. name+ age
3. name+age+address
As direct constructor overloading(multiple constructors) are not allowed but we have to use default parameters to simulate constructor overloading
'''

class Person:
   def __init__(self, name, age=None, address=None):
      self.name=name
      self.age=age
      self.address=address


p1=Person("simran",22,"sec-6, karnal")

print(p1.name, p1.age, p1.address)
      


'''
Concept: Instance and Class Attribute
Question 8: Create a class Player with:
1. a class variable player_count
2. instance variable name and level
Track how many players were created.
'''
class Player:
   player_count=0

   def __init__(self, name, level):
      self.name=name
      self.level=level
      Player.player_count+=1

P1=Player("simran",2)
P2=Player("suman",1)
P3=Player("punjab",1)

print(P1.player_count)



'''
Concept: Multiple Inheritance
Question 9: Create a following classes: Herbivore, Carnivore, Omnivore with some attributes and methods. Then create a class Bear that inherits from all the above classes and showcase how multiple inheritance works.
'''
class Herbivore:

   def __init__(self, legs):
      self.legs=legs

class Carnivore:

   def __init__(self, tommy):
      self.tommy=tommy


class Omnivore:
   
   def __init__(self, hands):
      self.hands=hands


class Bear(Herbivore, Carnivore, Omnivore):
   type="Bear"

   def __init__(self, legs, name, tommy, hands):
      Herbivore.__init__(self,legs)
      Carnivore.__init__(self,tommy)
      Omnivore.__init__(self,hands)
      self.name=name


B1=Bear(4,"cow","big", 2)

print(B1.name, B1.hands, B1.legs, B1.tommy)

