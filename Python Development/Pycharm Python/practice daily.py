
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

# Word_length_filtered
def word_length_filtered(data):
    try:
        filter_list=filter(lambda w:len(w)>=5,data)
        capital_letter=map(lambda w:w.upper(),filter_list)
        return list(capital_letter)
    except Exception as e:
        print(e)
print(word_length_filtered(["hello","World!","PY","Exception","None"]))

#Classify NuMBERS
def classify_numbers(nums):
    result=[]
    for x in nums:
      try:
          if  not isinstance(x,int):
             raise ValueError (f"{x} is not an integer")
          tag="even" if x%2==0 else "odd"
          result.append(f"{tag}:{x}")
      except Exception as e:
         print("Warning",e)
    return result

output=classify_numbers([10, "a", 7, 0, 3.14])
print(f"result:",output)

# Student_Grade_Calculator:
def Student_Grade_calculator():
    grade_dict={
        "Alice": [95, 82, 100],
        "Bob": [70, "eighty"],
        "Charlie": []
    }


    def assign_grades(average):
     if average>=90:
         return "A"
     elif average>=80:
         return"B"
     elif average>=70:
         return "C"
     elif average>=60:
         return "D"
     else:
         return "F"

    def grade_students(grade_dict):
         for name, marks in grade_dict.items():
             try:
                 if not marks:
                     raise ValueError("no marks")

                 average = sum(marks) / len(marks)
                 grade=assign_grades(average)
                 print([f" 'name': {name} , 'average': {average},'grade': {grade}"])
             except Exception as e:
                 print(f"Error Processing :{name} and {e}")
    grade_students(grade_dict)
Student_Grade_calculator()

#reverse non palindrome
def reverse_non_palindrome(string):
    def reverse(s):
        if not isinstance(s,str):
            raise TypeError("s is not a string")
        return s[::-1]
    reverse_string=[]
    for item in string:

        try:
          if  reverse(item).lower() != item.lower():
             reverse_item=reverse(item)
             reverse_string.append(reverse_item)
        except Exception as e:
         print(e)

    return reverse_string
result=reverse_non_palindrome(["madam", "hello", 123, "Racecar", "python"])
print(result)

#--------------------------------------------Validation Questions----------------------------
#----------------------------------------------------------
#Positive integer validator
def positive_integer_validator():
    while True:
        num=int(input("Enter number:"))
        try:
            if num >0 :
                print(f"Valid input:{num}")
                break
            else:
                print("number is positive")
        except Exception as e:
            print(e)
            print("Invalid number.Enter number again.")
positive_integer_validator()

#Age Range checker

def Age_Range_Checker():
    age=int(input("Enter Your age: "))
    while True:
     try:
            if 1 <= age <=120:
                print(f"Age Accepted: {age}")
                break
            else:
                print("Age must be between 1 and 120.")
                break
     except Exception as e:
            print(e)
            print("invalid input. please Enter a number.")

Age_Range_Checker()

# Password Validator
def password_validator():
    password=input("Enter password:")
    while True:
        try:
            if len(password)<8:
                print("Password must be at least 8 characters.")
            elif " " in password:
                print("Password can not have spaces.")
            else:
                print ("correct password.")
            break
        except Exception as e:
            print(e)
            print("invalid password.")
password_validator()


#
def CustomException():
    pass
def validate_age():
    age=int(input("Enter the age:"))
    try:
        if age>=0:
            print(f"Age is {age}")
            raise CustomException("invalid age.")
        else:
            print('Invalid age')
    except Exception as e:
        print(e)
    except CustomException as e:
        print(e)

validate_age()
# Validation of Password:
def password_validation():
    password=input("Enter password:")
    try:
        if len(password)>8:
            print("password is too long.")
        else:
            print("password is valid. ")
    except Exception as e:
        print(e)
password_validation()



def password_validation(password):
    special_char="!@#$%^&*."
    if len(password)>8:
        raise Exception("password is too long.")
    if not any(char.isdigit()for char in password):
            raise Exception("Password contain at least one digit.")
    if not any(char.isupper()for char in password):
            raise Exception("Password contain at least one uppercase.")
    if  not any(char in special_char for char in password):
            raise Exception("password contain at least special character.")
    print("password is valid.")
def validate_password():
    password = input("Enter password:")
    try:
        password_validation(password)
    except Exception as e:
        print(e)
        print("Invalid password.")
validate_password()