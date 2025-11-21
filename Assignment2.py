#Assignment Problems

'''Question 1: Write a program that takes salary as input. Using conditional statements,calculate the final tax rate based on these rules.
a) if salary <30000-> 5%
b) if salary is 30000-70000-> 15%
c) if salary >70000-> 25%'''

salary=int(input("enter your salary:"))

if(salary<=30000):
    print("5% tax")

elif(30000<salary<=70000):
    print("15% tax")

elif(salary>70000):
    print("25% tax")


#Question 2: Write a function that takes two integers a and b and prints all even numbers between them(inclusive)
a=int(input("enter first number:"))
b=int(input("enter second number:"))

if(a%2!=0):
    for i in range(a+1,b+1,2):
        print(i)
elif(a%2==0):
    for i in range(a,b+1,2):
        print(i)



'''Question 3: Write a function that prints the digits of a number, n:
For eg: n=312 there are 3 digits in it 3, 1, 2 and we need to print them.

[Hint: The right most digit of a number N is N %10.
And to remove the right most digit from a number, we can do N=N/10.]
'''

def print_digit(N):
  rev=0                                      #firstly we reverse the number N
  temp=N

  while temp>0:
    rev=rev*10+(temp%10)
    temp=temp//10

  while rev>0:
    print(rev%10)
    rev=rev//10


print_digit(312)

print("stop")

#Question 4: write a function to return the count the number of digits in a number n.
def count_digit(n):
  count=0
  while(n>0):
    count+=1
    n=n//10
  return count
   

print(count_digit(31326))



#Question 5: write a function to return the sum of digits of a number, n
def sum_digit(n):
   sum=0
   while(n>0):
      sum+=n%10
      n=n//10
   return sum


print(sum_digit(int(input("enter number:"))))

print("stop")

#Question 6: write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5

for i in range(1,101):
   if(i%3==0 and i%5==0):
      print(i)



#Question 7: design a program to continuously input a number n from user and print if it is positive or negative until the user enters 'quit'.

while True:
   n=input("enter a number or type quit to stop:")

   if(n=="quit"):
      break
   
   n=int(n)
   
   if(n>0):
      print("positive")

   elif(n<0):
      print("negative")

   else:
      print("Zero")   



'''Question 8: Letʼs create a Simple calculator that performs arithmetic operations. Create a function calculator(a,b, operation) that performs addition, subtraction, multiplication, or division based on the operation parameter.
[operation parameter can have values '+', '-', '*' & '/']'''


def calculator(a,b):
   n=input("enter operator:")

   if(n=="+"):
      sum=a+b
      return sum
   elif(n=="-"):
      subtraction=a-b
      return subtraction
   elif(n=="*"):
      multiplication=a*b
      return multiplication
   elif(n=="/"):
      division=a//b
      return division
   

print(calculator(6,2))



#Question 9: Write a function is_prime(n) that returns true if n is a prime number and false otherwise, using a loop.
# [Hint-
# a) We only check prime for 2 or numbers greater than 2. 2 is the smallest prime number.
# b) A non-prime number, n, will always get divided by atleast one number in range[2,n-1].
# Eg-For number 9 weʼll check in range(2,8) & itʼll get divided by 3. So 9 is non-prime & weʼll return false for it.
# For number weʼll check in range(2,6) & it wonʼt get divided by any. So 7 is prime & weʼll return true for it] 

def is_prime(N):
   for i in range(2,N):
      if(N%i==0):
          return False
   return True
      

print(is_prime(9))




#Question 10: Letʼs create a “Number Guessing Game”. Given a secret number (already decided by you),write a program that asks the user to guess it and prints:
# a)"Too high" if the guess  is above the number
# b) "Too Low" if the guess is below
# c) "Correct!" if the guess matches
         
      
secret=67

while True:
  number=int(input("enter the number: "))

  if(secret>number):
      print("too low")
  elif(secret<number):
      print("too high")
  elif(secret==number):
      print("correct!")
      break

