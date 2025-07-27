
# Day 01
# Question 01
def validate_string():
    s="good girl"
    try:
        if len(s)>=(5):
          print(True)
        else: 
         raise ValueError("String is shorter than 5 character" )
    except Exception  as e:
            print(f'Error:{e}')
validate_string()
#Question 02
#Count vowels in text

def count_vowels():
   s  = "Nadia Yousaf"
   vowels = "AEIOUaeiou"
   count = 0
   for char in s:
      if char in vowels:
          count+=1
   print(f"The vowels in the string are:{count}")
   return count
count_vowels()

#Q3

def square():
    n=int(input("Enter the number:"))
    sq=n**2
    print(f"The square of n  is:{sq}")
square()
#q4
#print odd numbers
def odd_numbers():
    n=int(input("Enter number:"))
    for i in range(1,n+1):
        if i %2!=0:
         print(i)
        else:
           pass
odd_numbers()
#Q5
num1=int(input("Enter number:"))
num2=int(input("Enter number:"))
try:
    if num1/num2:
        print(True)
    else:
            raise ValueError("Invalid input")
except Exception as e:
    print(e)

#Q6
lst=[2,4,6,8]
numbers=map(lambda x:x*3,lst )
print(list(numbers))
for num in numbers:
    print(num)

#Q7
#String filtering pipeline

data=["alice1","Bob!","eve","mallory2"]
capitalized=map(lambda s:s.capitalize(),data)
filtered=map(lambda s:s.is_alpha(),capitalized)
print(list(filtered))

#Q8

def make_power(n):
    return lambda x:x**n
square=make_power(2)
cube=make_power(3)
print(square(5))
print(cube(2))

#Q9
#Generate fibonacci even numbers

def generate_fibonacci():
    n = int(input("Enter number:"))
    try:
        if n % 2 == 0:
            print("Even numbers")
        else:
            raise ValueError("the number is not even")

    except Exception as e:
      print(e)
    for num in range(1, 10):
      filtered = filter(lambda x: num % 2 == 0, range(1, num + 1))
      print(list(filtered))

generate_fibonacci()

#Q10
# Custom file factory

def make_filter(divisor,min_value):
    return lambda x:x %divisor==0 and x>min_value
divisor=2
min_value=4
filtered=filter(lambda x: x % divisor==0, range(1,50))
print(list(filtered))

#Q11
#mixed data processor


from functools import reduce

def safe_int(s):
    try:
        return int(s)
    except  ValueError:
        print("Invalid input")

def mixed_data_processor(data):
    converted = map(lambda x: safe_int(x), data)
    filtered = [x for x in converted if x is not None and x > 0]
    if not filter:
        return "No valid input"

    total = reduce(lambda x, y: x + y, filtered)
    average = total/ len(filtered)
    print(average)

data=["10","two","30","fifty"]
mixed_data_processor(data)

#Q 12
#  custom filter
