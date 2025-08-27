

#=------“The goal is not to finish fast, the goal is to become unstoppable and build logics .”-------------

#Loops Questions
#Basics

for x in range(1,11):
    print(x,end=' ')

Sum=0
for x in range(1,20):
    if x%2==0:
      Sum=Sum+x
print(f"Sum of even numbers is:",Sum)

Sum=0
for x in range(1,10):
    Sum=Sum+x
print(f"Sum of Natural Number is :",Sum)

lst=[10,20,30,40,50]
for x in lst:
 print(x,end=' ')

num=10
while num>=1:
    print(num,end=' ')
    num-=1

for i in range(1,10):
    squ=i*2
    print(squ)

num=7
for i in range(1,11) :
    result=i*num
    print(f"{num}*{i}={result}")


def reverse_String():
 Str="Hello"
 reverse_Str=""
 for i in range (len(Str)-1,-1,-1):
     reverse_Str +=Str[i]
 print(reverse_Str)
reverse_String()

for i in range(1,100):
    if i%3==0 and i %5==0:
        print(i)

count=0
Lst=[12,65,90,33,102]
for item in Lst:
    count+=1
print("Total Count",count)

#Loops medium Questions

#---------------Factorial
#The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
#5!=5*4*3*2*1=


def factorial():
    num=10
    Factorial=1
    for i in range(1,num+1):
        Factorial*=i
        print(f"Factorial of {i} is:{Factorial}")
factorial()




def reverse():
    number=1234
    reverse_number=""
    number=str(number)
    for i in range(len(number)-1,-1,-1):
        Reverse=reverse_number+number[i]
        print(Reverse)
reverse()


def reverse():
    number=1234
    reverse_number=""
    for digit in reversed(str(number)):
        reverse_number += digit
    print(reverse_number)
reverse()


def count_vowels():
    String=input("Enter the String:")
    vowels="AEIOUaeiou"
    count=0
    for item in String:
        if item in vowels:
         count+=1
    print(f"Count Vowels",count)
count_vowels()


def Sum_of_digits():
    Sum=0
    Digits=input("Enter the digit:")
    for i in Digits:
        Sum+=int(i)
    print(Sum)
Sum_of_digits()





#conditionals

def check_number():
    number=98
    if number>0:
        print("Number is positive.")
    else:
        print("Number is negative.")
check_number()


def check_grade():
    Marks=int(input("Enter the marks:"))
    if Marks>90:
        print("A")
    elif Marks>80:
        print( "B")
    elif Marks>70:
         print("C")
    else:
        print("F")
check_grade()


def check_leap_year():
    year=int(input("Enter the Year:"))
    if year%400==0:
        print("Leap year")
    else:
        print("Not leap year")
check_leap_year()

def largest_number():
    number1=int(input("Enter number1:"))
    number2=int(input("Enter number2:"))
    number3=int(input("Enter number3:"))
    if number1>number2 and number1>number3:
        print(f"largest:{number1}")
    elif number2>number1 and number2>number3:
        print(f"largest:{number2}")
    else:
        print(f"Smallest Number:{number3}")

largest_number()




def Atm_Simulator():
    balance=int(input("Enter the balance: "))
    With_draw_amount=int(input("Enter With_draw_amount: "))
    def with_draw():
        if With_draw_amount>balance:
            print("Insufficient balance")
        elif With_draw_amount*500:
            print("Transaction Successful.")
            remaining_balance=(balance)-(With_draw_amount)
            print(f"remaining_balance:{remaining_balance}")
        else:
            print("Amount must be multiple of 500.")
    with_draw()
Atm_Simulator()


#Loops and conditionals:


def count_Even_odd():
    lst = [12, 5, 7, 20, 8, 13]
    even_count=0
    odd_count=0
    for item in lst:
        if item%2==0:
            even_count+=1
        elif item%2!=0:
           odd_count+=1
    print(f"Even Number", even_count)
    print(f"odd Number",odd_count)
count_Even_odd()


def count():
 positive_count=0
 negative_count=0
 zero_count=0
 List = [0, -5, 7, 9, -2, 0, 11]
 for item in List:
     if item>0:
        positive_count+=1
     elif item<0:
         negative_count+=1
     elif item==0:
         zero_count+=1
 print(f"positive Number",positive_count)
 print(f"Negative Number",negative_count)
 print(f"Zero number",zero_count)
count()


#count method use for count the words
#len method is also used for specific word count
def word_counter():
    Sentence=input("Enter the Sentence:")
    words=Sentence.split()
    count=len(words)
    print("Count words",count)
word_counter()



def word_counter():
    Sentence=input("Enter the Sentence:")
    target_word=input("Enter the target word: ")
    words=Sentence.split()
    count=words.count(target_word)
    print(f"target word {target_word} appears {count} times.")
word_counter()





#Right angle triangle

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

#inverted right nagle triangle
n=5
for i  in range(n,0,-1):
  for j in range(i):
    print("*",end=" ")
  print()

  #Number TRiangle
n=5
for i in range(1,n+1):
   for j in range(1,i+1):
    print(j,end=" ")
   print()


n=5
for i in range(n,0,-1):
   for j in range(i):
      print(j,end=" ")
   print()

   #Right Allighned triangle
n=5
for i in range(1,n+1):
   for j in range(n-i):
      print(" ",end=" ")
   for j in range(1,i+1):
      print(j,end=" ")
   print()


arr=[10,20,30,40]
arr[0] ,arr[3] = arr[3], arr[0]
print(arr)


def swap_element(lst,i,j):
    lst[i],lst[j]=lst[j],lst[i]
    numbers=[10,20,30,40,50]
    swap_element(numbers,0,3)
    print(numbers)
