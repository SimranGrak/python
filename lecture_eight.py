#OOPS: Object Oriented Programming
'''Prodecural programming: it means using the function for reusing the functions
we use OOPS for the real life practical use
where it is not possible to copy paste all the items for 1000 times

classes: it is basically a type of blueprint which is used to make 1000 things similarly.
suppose we have factory of Audi car, so they have created one blueprint for the car and all cars follows the same structure while designing


Class: blueprint of object. it does not take space in the memory
Object: instance of class, which actually exist and take space in the memory'''


#how to create class
class student:                                                     #this is class
  subject="Python"
  college="MMDU"


stu1=student()                                                        #this is object
#similary we can create for 1000 students
print(stu1.subject, stu1.college)                                      #how to access the object



#class basically contains two things
#a) properties/attributes: features
#b) behaviour/methods: functions in simple language


#when we create a empty set
s=set()          #its type is class set
#means here the set is class and s is object



#Important and first method in every class is CONSTRUCTOR
#__init__ method inside the constructor: it is called everytime when we create an object and this gets call automatically
#if we do not create init and python creates and run it by default
#CONSTRUCTOR: it is used to create the  objects 

#constructor is special method inside the class. constrcutor names as __init__ which means to initilaize.
class car:
  def __init__(self,model):
    self.model=model

alto=car("800")

print(alto.model)


#similarly init method we can create other methods in python

class bike:
  def __init__(self,name,km):            #self parameter is bascially a reference which object call this method
    self.name=name
    self.km=km
  
  def speed(self):
    return self.km


bike1=bike("splender","23")

print(bike1.speed())


#types of constructor
#a) default constructor: which have only self parameter
#b) parameterized constructor: which have more than self parameters

#IN PYTHON ONLY ONE INIT METHOD OR ONE CONSTRUCTOR IS ALLOWED
#IF WE CREATE TWO IT BY DEAULT TAKES THE LAST INIT METHOD AND CODE WORKS FINE



#ATTRIBUTES: two types
#a) class attributes: created by class only. they are common for all objects
#b) instance attributes: created by particular object only. but they are unique for every object

class student:
  college="ABC"          #this is class attribute

  def __init__(self,name):
    self.name=name                #this is instance attribute

stu1=student("simran")

print(stu1.name)



#METHODS: 
#a) instance method: which have self parameter
class laptop:
  storage_type="SSD"

  def __init__(self,RAM, type):
    self.RAM=RAM
    self.type=type

  def get_info(self):
    print(f"this is RAM: {self.RAM} and type: {self.type} and the storage type: {self.storage_type}")     #isntance  method
#so here the instance method already access the instance attribute but here it can also the class attribute

L1=laptop("64gb","hp")
L2=laptop("256gb","acer")

L1.get_info()


#b) class method:
#in class method we have first parameter is clas similar as instance method: it basically refers to that class
# note: they cab only access class attribute not the instance attribute
class student:
  college="ABC"         

  def __init__(self,name):
    self.name=name    


#in class method we use @classmethod(it is a tupe of function) at the top called as decorator: if we write on any function basically it change the behaviour to class method

  def student_info(cls):
    print(f"student college name={cls.college}")

stu1=student("simran")

print(stu1.name)
stu1.student_info()



#c) static methods: they do not have any compulsory parameter
#use decorator called @staticmethod
#do not access instance or class attribute and works like a normal function just kept inside class
#WHY: Because sometimes you want a function inside a class for better grouping/organization,
#even though the function does not need access to class or object data.


class student:
  college="ABC"          

  def __init__(self,name):
    self.name=name     

  @staticmethod
  def cal_marks(marks):
    final_marks=marks*100/100
    print(f"final mraks:{final_marks}")          

stu1=student("simran")

print(stu1.name)
stu1.cal_marks(500)




#Practice Problem
'''Design and create an online store for Products(name, price).
track total products being created.
create a static method to calculate discount on each product based on a % parameter.
'''
class products:
  count=0
  
  def __init__(self,name,price):
    self.name=name
    self.price=price
    products.count+=1

  def get_items(self):
    print(f"the product name is {self.name} and the price is {self.price}")

  @classmethod
  def get_count(cls):
    print(f"total products created are: {cls.count}")

  @staticmethod
  def get_discount(price, discount):
    print(f"discount price={price- (price*discount/100)}")

product1=products("hoodie",1500)
product2=products("jeans",2000)
product2=products("skirt",1000)


product1.get_items()
product2.get_items()
products.get_count()
product1.get_discount(product1.price,10)


  

