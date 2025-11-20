'''functions in Python
block of statemnet which performs specific tasks
example: input(), print(), reverse(), empty() etc.
Note: functions are basically reusable components of code
function is basically divide into 2 parts
1.)definition: which defines the logic
2.)call or invoke: means when we call the function'''


#we can create a fucntion on our own
#def: is used to define a function
#basic function
def hello():                            #definition
    print("hello")

hello()                                  #call a function

#we can call function infinite times


#basically function is like a box which takes some value as input and then return output
#means it takes parameters and return output

#function to create sum of two number

def sum(a,b):                  #a,b are placeholders
    s=a+b
    return s                    #return is a keyword


ans=sum(3,3)
print(ans)
    #or
print(sum(3,4))



#write a function which take 3 values and return the average of these values

def avg(a,b,c):
    average=(a+b+c)/3
    return average


ans=avg(3,3,2)

print(ans)



#using default parameters
#it basically means when we do not give any argument 
#non default parameters come first and default parameters comes at last
def def_par(a,b=1):
    s=a+b
    return s

print(def_par(5))




#types of functions
#a) built-in function: like print(), reverse(), range() etc.
#b) user defined function: which we create on our own



#lambda function
#it is anonymous function: we do not use them to perform complex tasks
sum=lambda a,b,c: a+b+c                            #expression is only one(a+b+b)
#parameters can be more than 1
#sum is a function name
print(sum(3,4,8))




#Write a function to print factorial of 'n'
def fact(a):
    factorial=1
    for i in range(1,a+1):
        factorial=factorial*i
        
    return factorial


print(fact(5))
