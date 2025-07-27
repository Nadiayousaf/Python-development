name="nadia"
for i in (name):
    print(i)
    
    
b="sorry"
for i in range(2):
    print(b)
    
    
    
c="Mama miss you"
for i in range(20):
    print(c)
    
d="Happy Birthday"
for i in range(5): 
    print(d)
    if (i=="c"):
        print("This is special")
    else:
        print("somethng special")
        


for k in range(1,10,5):
    print(k)
    
i=int(input("Enter the number:"))
while(i<=6):
    print(i)
    i=+1
    
for i in range(11):
    print("7*i",i+1,"=",7*i+1)
    if i==10:
        break
    
c="thanks  "
for i in range(2):
    print(c)



#continue skip the iteration
#break statement use to exit the loop




for i in range(11):
  if i==12:
      print("Skip the iteration")
      continue
  print("7*i",i+1,"=",7*i+1)
   
a=2
b=3
c=4
d=5
g_mean=((a+b)/(c*d))
print(g_mean)

def CalculateGmean(a,b) :
    mean=((a+b) )
    print(mean)
if(a>b):
    print("first number is greater")
else:
    print("second number is greater")
CalculateGmean(2,3)
#Function in python



def hello_function():
    pass
print(hello_function())
    
def hello_function():
   print("hello") 
hello_function()


def hello_function():
   print("hello world") 
   print("hello world")
   print("hello world")
hello_function()

def hello_function():
   for i in range(10):
     print("hello world")
hello_function()

def hello_function():
    print('hello_function')
hello_function()
hello_function()
hello_function()



def hello_function():
    return'hello_function.'
print(hello_function())


def hello_function():
    return'hello_function.'
print(hello_function().upper())


def hello_function():
    a="hello"
    print(a.upper())
hello_function()

#passing the arguments in the function
def hello_function(greetings,name="nadia"):
    return'{}'.format(greetings,name)
print(hello_function("hi"))


def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
    courses= ["arts","maths"]
    info={'name':"nadia",'age':18}
student_info('arts','maths',name='nadia',age=18)

# * used for list
# ** used for dictionary
# here is courses are in the list and info is in the dictionary

def student_info(*args,**kwargs):
    print(args,kwargs)
    courses= ["arts","maths"]
    info={'name':"nadia",'age':18}
student_info('arts','maths',name='nadia',age=18)

def Range(*numbers):
  sum=0
  for i in numbers:
    sum=sum+i
    print(sum)
Range(4,5)

def Range(*numbers):
  sum=0
  for i in numbers:
    sum=sum+i
    print(sum)
Range(4,5)


total_sum = 0
input_range = input('Enter Input Range: ')

def get_sum(n):
    global total_sum
    for x in range(int(n)):
        print(f'Enter Number: {x+1}')
        val = int(input())
        total_sum = total_sum + val
get_sum(input_range)
print(total_sum)

#in simple method by using function
def Average(x,y,z):
    average=(x+y+z)/3
    print(average)
Average(5,6,7)


def double(x):
    return x*2
print(double(2))


#Lambda function in short time work
avg=lambda x,y,z:(x+y+z)/3
print(avg(5,6,7))


double=lambda x:x*2
print(double(2))



numbers=[1,2,3,4,5]
even_number=list(filter(lambda x: x%2==0,numbers))
print(even_number)


numbers_greater_than_3=list(filter(lambda x:x>3, numbers))
print(numbers_greater_than_3)

#len,max,min,sum in the functions
#Q: Given the list numbers = [3, 6, 2, 8, 4], what is the maximum value in the list?

numbers=[3,6,2,8,4]
max_value=max(numbers)
print(max_value)


values = [1, 5, 3, 9, 2]
maximum_value = max(values)
minimum_value = min(values)
length_of_list = len(values)
total_sum = sum(values)

print(f"Max: {maximum_value}, Min: {minimum_value}, Length: {length_of_list}, Sum: {total_sum}")
        
        

#Q: What is the output of sum([])?


total_sum = sum([])
print(total_sum) 


def Values(values):
     maximum_value = max(values)
     minimum_value = min(values)
     length_of_list = len(values)
     total_sum = sum(values)
     
print(f"Max: {maximum_value}, Min: {minimum_value}, Length: {length_of_list}, Sum: {total_sum}")
Values([1, 5, 3, 9, 2])


numbers=[4,6,8,10]
maximum_value=max(numbers,key=lambda x: x)
print(f"The maximum value in the list is: {maximum_value}") 


numbers = [10, 15, 7, 25, 3]
# Using lambda with max to find the maximum value
# maximum_value = max(numbers, key=lambda x: x)

print(f"The maximum value in the list is: {maximum_value}") 




def delete():
    if ("people hurt you"):
        print(delete )
    elif("have real friends"):
        print("Safe")
    else:
        print(exit)
delete()
        
        
def Calculate_Sum(a,b,c,d):
    Sum = a + b
    if Sum == 10:
       Sum1 = c + b
       if Sum == 20:
           Sum2 = c + d
       if Sum == 30:
          if Sum2 % 2  == 0:
                   print(f'Sum: {Sum2} Even')
          if Sum2 % 2 != 0:
                   print(f'Sum: {Sum2} Odd')
          else:
            print(f'Sum Is: {Sum}')

a = int(input('Enter Number 1: '))
if a < 0:
    print('A is lower then 0')
    a = int(input('ReEnter Number 1: '))
    b = int(input('Enter Number 2: '))
    c = int(input('Enter Number 3: '))
    d = int(input('Enter Number 4: '))

Calculate_Sum(a,b,c,d)
        
        
        
    
def calculate_sum(num1,num2):
 number1=int(input("Enter the first number:"))
 number2=int(input("Enter the second number:"))
 sum=number1+number2
 print(sum)
 for x in range(user_range):
        print(f'Enter Number {x+1}')
        inp = input()
        SUM = SUM + int(inp)
        print(f'Sum: {SUM}')
if sum==10:
  num1=int(input("re-enter the first digit:"))
  sum=num1+number2
  if sum==20:
    num2=int(input("Enter the second digit:"))
    sum=num1+num2
    if sum==30:
      num1=int(input("Enter the first number:"))
      num2=int(input("Enter the second number:"))
      result=num1+num2
    print(f"number1:{num1}")
    print(f"number2:{num2}")
calculate_sum(2,4)
    
    
    
    
number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))
sum=number1+number2
print(sum)
for x in range(user_range):
        print(f'Enter Number {x+1}')
        inp = input()
        SUM = SUM + int(inp)
        print(f'Sum: {SUM}')
if sum==10:
  num1=int(input("re-enter the first digit:"))
  sum=num1+number2
  if sum==20:
    num2=int(input("Enter the second digit:"))
    sum=num1+num2
    if sum==30:
      num1=int(input("Enter the first number:"))
      num2=int(input("Enter the second number:"))
      result=num1+num2
      
def Calculate_Sum(a,b,c,d,user_range):
    Sum = a + b
    if Sum == 10:
        if Sum == 20:
           if Sum == 30: 
             Sum1 = c +b
             Sum2 = c + d
    for x in range(user_range):
           print(f'Enter Number {x+1}')
           inp = input()
           SUM = SUM + int(inp)
           print(f'Sum: {SUM}')
a = int(input('Enter Number 1: '))
if a < 5:
    print('A is lower then 5')
    a = int(input('ReEnter Number 1: '))
    b = int(input('Enter Number 2: '))
    c = int(input('Enter Number 3: '))
    d = int(input('Enter Number 4: '))
user_range=int(input("Enter the number:"))
Calculate_Sum(a,b,c,d,user_range)



#Loops Questions
#Question 1: Print Numbers from 1 to 10
for i in range(1,10):
    print(i)
     
 #Question 2: Sum of First N Natural Numbers   
N=10
sum_N=0
i=1
while(i<=N):
    sum_N+=1
    i+=1
    print("Sum of first",N,"natural numbers is:",sum_N)
    #print even numbers from(1,20)
    for  i in range(1,21):
     if i % 2==20:
          print(i)
          
    #reverse a string
str='nadia'
for i in range(-1,-len(str)-1,-1):
     print(str[i])


N = 10  # You can change this value
a, b = 0, 1
count = 0

while count < N:
    print(a)
    a,b=b,a+b
    count += 1
    
def print_Numbers(n):
    for i in range(1,n+1):
        print(i)
print_Numbers(10)

def sum_of_natural_numbers(n):
    total=0
    for i in range(1,n+1):
        total+=1
        return total
    result=sum_of_natural_numbers(10)
    print("sum of 10 natural numbers is :", result)
    
  
def Even_numbers(n):
    for i in range(1,n+1):
        if i%2==0:
            print(i)
Even_numbers(20)


str=input("Enter the string:")
def reverse_string():
    str[0]
    for i in range(-1,-len(str)-1,-1):
        print(str[i])
reverse_string()

def Check_Numbers(number):
    if number>0:
        return "it is positive"
    elif number<0:
       return"it is negative"
    else:
        return"exit"
print(Check_Numbers(8))
print(Check_Numbers(-44))
print(Check_Numbers(9))


def get_grade(score): 
    if not (0 <= score <= 100):
        return "Invalid score, must be between 0 and 100."
    if score>=90:
        return "A"
    elif (score>=80):
        return "B"
    elif(score>=70):
        return "C"
    elif(score>=60):
        return "D"
    
    else:
        return "f"
print(get_grade(89))
print(get_grade(88)) 
print(get_grade(77))  
print(get_grade(83))
print(get_grade(74))
print(get_grade(65))
print(get_grade(40))
print(get_grade(8))


number=int(input("Enter the number:"))
def Even_or_odd():
    if number%2==0:
        return("Even number")
    else:
          return("odd number")
print(Even_or_odd())  



def Even_or_odd(number):
    if number%2==0:
        return("Even number")
    else:
          return("odd number")
print(Even_or_odd(45)) 
            
            


def is_leap_year(year):
    if year%400==0:
        return("leap year")
    else:
        return("it is not leap year")

print(is_leap_year(2025)) 
print(is_leap_year(2022)) 
print(is_leap_year(2024)) 
print(is_leap_year(2023)) 
        
        
user_input = input("Enter a string: ")
def count_vowels():
    vowels = "aeiou"
    count = 0
    for char in user_input:
        if char in vowels:
            count += 1
    print(f'The number of vowels in "{user_input}" is: {count}')
count_vowels()
       
def fizzbuzz():
    for i in range(1,101):
        if i%3==0 and i%5==0:
            print("fizzbuzz")
        elif(i%3==0):
            print("fizz")
        elif(i%5==0):
            print("buzz")
        else:
            print(i)
fizzbuzz()

def Calculator():
    print("Selection of number")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")

choice=input("Enter choice(1/2/3/4):")
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number\\2:"))

if choice=='1':
    result=num1+num2
    print(result)
elif choice=="2":
    result=num1-num2
    print(result)
elif choice=="3":
    result=num1*num2
    print(result)
elif choice=="4":
    if num2!=0:
        result=num1/num2
        print(result)
    else:
        "invalid input"
Calculator()

str="Nadia"
def Reverse_String():
    for i in range(-1,-len(str)-1,-1):
        print(str[i])
Reverse_String()

def MCQS(MCQ1):
 Question1="What is your age?"
options=input("select the option:a/b/c ")
a='14'
b='18'
c='17'
print(MCQS(options))


def mcq1(statement1,options):
    print(statement1) 
    user_input1=input("enter the option:a/b/c ") 
    return user_input1
options=({'a':'18'},{'b':'20'},{'c':'19'})
statement1=f'What is your age? The "{options}"are:options)'
def mcq2(statement2,options):
    print(statement2)
    user_input2=input("enter the option:a/b/c ") 
    return user_input2
options=({'a':"nadia"},{'b':"Ahmad"},{'c':"Noor"})
statement2=f'What is your name? The "{options}"are:options)'
print(mcq1(statement1,options))
print(mcq2(statement2,options))
print(options)


class Quiz:
    def start(self,):
        print(f'"when start the app:"a.options,a.MCQ1,a.MCQ2')
options=({'a':'18'},{'b':'20'},{'c':'19'})
user_input1=input("enter the option:a/b/c ")
MCQ1=f'What is your age? The "{options}"are:options)'
print(MCQ1)

user_input2=input("enter the option:a/b/c ")
options=({'a':"nadia"},{'b':"Ahmad"},{'c':"Noor"})
MCQ2=f'What is your name? The "{options}"are:options)'
print(MCQ2)
a=Quiz()
a.options=options=({'a':'18'},{'b':'20'},{'c':'19'})
a.MCQ1=MCQ1=f'What is your age? The "{options}"are:options)'
a.MCQ2=MCQ2=f'What is your name? The "{options}"are:options)'
a.start()

total=0
for i in range(5):
    number=int(input("Enter the number{i+1}:"))
    total+=number
    print("the sum of the number is:",total)
      
correct_number=7
while True:
    Guess=int(input("Enter the guess number"))
    if Guess==correct_number:
         print("congratulations")
    else:
        print("try again")

number=int(input("Enter the number:"))
for i in range(1,11):
    print(f'{number}*{i}={number*i}')
    



names = []
for i in range(3):
    name = "nadia","ahmad","mansha"
print("Names in reverse order:", name[::-1])


correct_password=''
while correct_password!="python123":
  user_input=input("enter the password:")
  print("ACCESS")


#Question1
'''Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  2 to 5 , print Not Weird
If  is even and in the inclusive range of  6 to 20 , print Weird
If  is even and greater than 20 , print Not Weird'''

number=int(input("Enter the numberer:"))
if ("number is odd"):
    print("weired")
elif("number is even" and "in the range(2 to 5)"):
        print("not weired")
elif ("number is even" and "in the range(6 to 20)"):
            print("weired")
elif ("number is even"and "number>20"):
    print("not weired")
else:
    print(exit)
                
number=30
if ("number is odd"):
    print("weired")
elif("number is even" and "in the range(2 to 5)"):
        print("not weired")
elif ("number is even" and "in the range(6 to 20)"):
            print("weired")
elif ("number is even"and "number>20"):
    print("not weired")
else:
    print(exit)       
        
