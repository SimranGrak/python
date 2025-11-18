#loops in python
#1: while loop:
count=0               #iterator
while(count<=4):
    print("hello world!", count)
    count+=1


#print in reverse using while loop
i=5
while(i>=1):
    print(i)
    i-=1



#print multiplication table of any number n
n=int(input("enter any number:"))

j=1
while(j<=10):
    print(n*j)
    j+=1


#important keyword in loops
#1. break: terminate loop
k=1
while(k<=10):
    if(k%5==0):
       break
    print(k)
    k+=1
print("out of loop now...")

#2. continue: skip the current iteration and move to next iteration

l=1
while(l<=10):
    if(l%3==0):
        l+=1
        continue
    print(l)
    l+=1
print("out of loop now...")


#print all the odd numbers from 1 to 10
m=1
while(m<=10):
    if(m%2==0):
        m+=1
        continue
    print(m)
    m+=1
print("here are odd numbers...")


#for loops: it is basically uses of sequesntial traversal
