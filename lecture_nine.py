'''OOPS PILLARS
PILLAR 1: ENCAPUSLATION: wrapping up data and fucntions into single unit-> data hiding also
we can do data hiding in 3 ways
1. public attribute: accessible everywhere-> inside and outside the class
2. protected attribute: accessible inside the class and in the subclasses or child classes
3. private attribute: accessible only inside the class
there is no true protected and private attribute.
we can still access the private
'''

class BankAccount:
  def __init__(self, name, balance):
    self.name=name                                #publice attribute
    self.__balance=balance                         #this becomes protected in python by adding underscore in starting
    #and if we add double underscore then it becomes private attribute


    #we cannot access the private values like this account1.__balance: it will return error(data mangling: protect private attributes inside a class)
    #so for accesssing the private values we use the getters and setters methods
  def get_balance(self):
      return self.__balance
    
  def set_balance(self,newBalance):
      self.__balance=newBalance

account1=BankAccount("simran",100000)

account1.set_balance(200000)

print(account1.get_balance(),account1.name)
#print(account1._BankAccount__balance)                         #this is way to access private attribute but do not use this




'''PILLAR 2: INHERITANCE: resusing attribute and methods from a Parent(Base) class.
Parent attribute( two types)
1. protected: can be accessed in subclasses 
2. private: cannnot be accessed in subclass also
'''

class Employee:
   start_time="8AM"
   end_time="5PM"

class teacher(Employee):
   def __init__(self,subject):
      self.subject=subject


teacher1=teacher("hindi")

print(teacher1.subject, teacher1.start_time, teacher1.end_time)



'''TYPES OF INHERITANCE:
1. Single Level Inheritance: example we only inherit the teacher class from employee class only
2. Multilevel Inheritance: example particular department inherit the properties of teachers and teachers inherit the properties of employee
3. multiple inheritance: means which uses the properties of multiple classes
note: SUPER KEYWORD: by using this we can acess the constructor of the parent class
'''
#multilevel inheritance
class Employee:
   start_time="8AM"
   end_time="5PM"

class teacher(Employee):
   def __init__(self,subject):
      self.subject=subject

class professors(teacher):
   def __init__(self, subject,role):
      super().__init__(subject)
      self.role=role

teacher1=professors("hindi","senior")

print(teacher1.role, teacher1.subject)



#multiple inheritance
class teacher:

   def __init__(self,salary):
      self.salary=salary
      
class student:
   def __init__(self,marks):
      self.marks=marks

class TA(teacher,student):
   def __init__(self,salary, marks,name):
      super().__init__(salary)
      student.__init__(self,marks)
      self.name=name


TA1=TA(99,20000,"simran")

print(TA1.name, TA1.salary, TA1.marks)


'''PILLAR 3: ABSTRACTION: hiding internal details and showing only essential features
Abstract classes: blueprint for other classes
Abstract classes are part of ABC module
'''

from abc import ABC, abstractmethod

class animal(ABC):
   @abstractmethod
   def make_sound(self):
      pass                             #returns null value, the implementation is left

class Lion(animal):
   def make_sound(self):
      print("Roar!")

class Cat(animal):
   def make_sound(self):
      print("Meow!")   


lion=Lion()
lion.make_sound()

#we cannot make the object of the Animal class beacuse it is abstract class          a=animal()

cat=Cat()
cat.make_sound()


    

''''PILLAR 4: POLYMORPHISM: many forms
multiple functions: same name
Example: operator overloading(in python the + operator do addition and concatination of strings )

Types of Polymorphism
1. Function overriding
2. Duck Typing
'''

#1. Function overriding: it is done only when there is inheritance
#it basically means redefining the parent class function into child class
class Employee:
   def get_designation(self):
      print("designation=Employee")

class Teacher:
    def get_designation(self):
      print("designation=teacher")
#here we have two same name function but the more specific function will implement when we create object

T1=Teacher()
T1.get_designation()

#2. Duck Typing:  walks like a duck and quaks like a duck called as duck typing
#means if we have two different classes which are not linked with each other and they function which have similar functionality then we can give the same name to those functions

class Teacher:
   def get_designation(self):
      print("designation=teacher")

class Accountant:
   def get_designation(self):
      print("designation=Accountant")

T1=Teacher()
T1.get_designation()

A1=Accountant()
A1.get_designation()


