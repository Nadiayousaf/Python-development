''''#Writes codes who write Ahsan . 
   #Question 1:

 #Write a Python program that:

Takes two inputs from the user.

The inputs can be either integers or strings that look like numbers (e.g., "4", "5.5").

The program should:

Convert both inputs to floats if they contain a dot (.), or to integers otherwise.

Then, add the two numbers.

If the result is an integer (e.g., 9.0), print "Result is an integer: 9".

If the result has a decimal (e.g., 9.5), print "Result is a float: 9.5".

If conversion fails, print "Invalid input".


#solution:
inp_a = input('Enter a: ')
inp_b = input('Enter b: ')

try:
    if '.' in inp_a or '.' in inp_b:
        inp_a = float(inp_a)
        inp_b = float(inp_b)
    else:
        inp_a = int(inp_a)
        inp_b = int(inp_b)

    Sum = inp_a + inp_b

    if Sum == int(Sum):
        print(f"Result is an integer: {int(Sum)}")
    else:
        print(f"Result is a float: {Sum}")

except ValueError:
    print("Invalid input")
 #Question2
def sum():
    inp_a = input('Enter a: ')
    inp_b = input('Enter b: ')
try:
    if '.' in inp_a or '.' in inp_b:
        inp_a = float(inp_a)
        inp_b = float(inp_b)
    else:
        inp_a = int(inp_a)
        inp_b = int(inp_b)

    Sum = inp_a + inp_b

    if Sum == int(Sum):
        print(f"Result is an integer: {int(Sum)}")
    else:
        print(f"Result is a float: {Sum}")

except ValueError:
    print("Invalid input")
    sum()

#Question 3
fruits=["Apple","Pineapple","Grapes"]
print(fruits[1])
#Question4
my_list=[1,2,3,4,5]
my_list.append(6)
print(my_list)
#Q 05
names=["Ali","sara","zain"]
names[1]="Fatima"
print(names)


#Q 06
names=["Ali","zain","sara"]
names.remove("zain")
print(names)
    
#Q7 Prompt the user to input two integers: num1 and num2.

Calculate the sum of num1 + num2.

Based on the value of this sum, trigger one of the following manual manipulation steps:

If the sum is exactly 10, prompt the user to re-enter num1, and recalculate the sum.

If the new sum is exactly 20, prompt the user to re-enter num2, and recalculate the sum again.

If the new sum is exactly 30, change both numbers manually by prompting new values for both.

if now again new sum is an even number, display: "Even Sum!"

If the sum is an odd number, display: "Odd Sum!"

If the sum is divisible by 3 and 4, say: "Divisible by both 3 and 4!"

If the sum is greater than 100, say: "That's a big number!"


#solution
number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))
sum=number1+number2
print(sum)
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
      if(result%2==0):
        print("Even number")
      else:
        print("odd number!")
        if result%3==0 and result%4==0:
          print("Divisible by both 3 and 4!")
          if (sum>100):
            print("Its a big number!")

        
        
    #  Use function 
#And check weather. Fun true then print

def calculate_sum():
   number1=int(input("Enter the first number:"))
   number2=int(input("Enter the second number:"))
   sum=number1+number2
   print(sum)
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
      if(result%2==0):
        print("Even number")
      else:
        print("odd number!")
        if result%3==0 and result%4==0:
          print("Divisible by both 3 and 4!")
          if (sum>100):
            print("Its a big number!")



#Try to take all inps as parameter , take inps when fun loads not on run time
def calculate_sum(num1,num2):
 number1=int(input("Enter the first number:"))
 number2=int(input("Enter the second number:"))
 sum=number1+number2
 print(sum)
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
      if(result%2==0):
        print("Even number")
      else:
        print("odd number!")
        if result%3==0 and result%4==0:
          print("Divisible by both 3 and 4!")
          if (sum>100):
            print("Its a big number!")
            
            print(f"number1:{num1}")
            print(f"number2:{num2}")
calculate_sum(2,4)


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

def Range():
  i=int(input("Enter the number:"))
  for i in range(i):
    print(i)
Range()


def Range():
  i=100
  for i in range(sorry):
    print(i)
Range()


def Range(*numbers):
  sum=0
  for i in range():
    sum=sum+i
    print(sum)
Range()




total_sum = 0
input_range = input('Enter Input Range: ')
def sum(number):
    for x in range(int(number)):
        print(f'Enter Number: {x+1}')
        val = int(input())
        total_sum = total_sum + val
sum(input_range)
print('Total Sum:', sum)



def delete():
    if ("people hurt you"):
        print(delete )
    elif("have real friends"):
        print("Safe")
    else:
        print(exit)
delete()



String='python'
for i in range(-1,len(String)-1,-1):
  print(String[i])'''
  

'''def Calculate_Sum(a,b,c,d,user_input):
   Sum = a + b
   if Sum == 10:
        if Sum == 20:
            if Sum == 30:
                Sum1 = c + b
                Sum2 = c + d
            try:
              for x in range(user_input):        
                       print(f'Enter Number {x+1}')
                       inp = input()
                       SUM = SUM + int(inp)
                       print(f'Sum: {SUM}')
            Except ValueError:
            print("Invalid input!")
a = int(input('Enter Number 1: '))
if a < 0:
    print('A is lower then 0')
    a = int(input('ReEnter Number 1: '))
    b = int(input('Enter Number 2: '))
    c = int(input('Enter Number 3: '))
    d = int(input('Enter Number 4: '))
    user_input=int(input("Enter the number:"))
Calculate_Sum(a,b,c,d,user_input)'''


#MCQ maker app



'''def mcq1(statement1,options):
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
print(options)'''










'''
def generate_MCQ():
    Question1=input("Enter the MCQ1:")
    confirmation = input("Want To change Statement or Continue?")
    if confirmation == "1":
        Question = input("Enter the MCQ1 again: ")
    print("Now enter four options one by one")
    option_a=input("Option a:")
    option_b=input("Option b:")
    option_c=input("Option c:")
    option_d=input("Option d:")
    correct_answer = input("Enter the correct answer (a, b, c, or d): ")
    print("Question:",Question)
    print(f' A : {option_a}')  # Use f string
    print(("b"),option_b)
    print(("c"),option_c)
    print(("d"),option_d)
    options=input("Enter four options 'a','b','c','d' ")
    if (correct_answer==options):
       print("Valid input")
    else:
      print("invalid input")
      
generate_MCQ()'''



''''def generate_MCQ():
    Question=input("Enter the MCQ:")
    print("Now enter four options one by one")
    option_a=input("Option a:")
    option_b=input("Option b:")
    option_c=input("Option c:")
    option_d=input("Option d:")
    options=input("Enter the option 'a','b','c','d'")
    correct_answer = input("Enter the correct answer (a, b, c, or d): ")
    return Question,option_a,option_b,option_c,option_d,correct_answer
def quiz(Question,option_a,option_b,option_c,option_d):
    print("Question:",Question)
    print(f' A : {option_a}')  # Use f string
    print(f' B : {option_b}')   
    print(f' C : {option_c}') 
    print(f' D: {option_d}') 
    print(f' correct_answer : {correct_answer}')
Question1,option_a,option_b,option_c,option_d,correct_answer=generate_MCQ()
Question2,option_a,option_b,option_c,option_d,correct_answer=generate_MCQ()
print("MCQ1")
quiz(Question1,option_a,option_b,option_c,option_d)
print("MCQ2")
quiz(Question2,option_a,option_b,option_c,option_d)
'''


'''incorrect_answer=[]
correct_answer=[]
user_answer= ('a','b','d','d')
answers=('a','b','c','d')
correct=0
if answers==user_answer:
    correct+=1
    incorrect_answer=answers-correct
    print(f"correct answer:{correct_answer}")
else:
    print(f"Incorrect answer:{incorrect_answer}")  '''
    
    
    
    
'''correct_answers=('a','b','c','d')
user_answer=input("Enter the option:")
correct=0
incorrect=0
for i in range(len(correct_answer)):
 if user_answer[i]==correct_answer[i]:
  correct+=1
  incorrect=user_answer-correct
print(f"correct:{correct}")
print(f"incorrect:{incorrect}")'''









n=int(input("Enter the number:"))
square=map(lambda x:x**n,[1,2,3])
cube=map(lambda x:x**n,[1,2,3])

print(square)
print(cube)




########################################################################################################################
# --------------------------------------: 🌀 Python Generators — Summary Notes :-----------------------------------------
# What is a Generator?
# its an special type of function that remembers its state and yield vals one at a time using yield keyword.
# A generator returns values one by one, not all at once like return.
# Instead of return, we use the yield keyword.
# yield pauses the function and remembers its state between calls, each next resumes where it was paused

# def test_return():
#     return [1, 2, 3]
# print(test_return())  # 1 2 3


def get_gen_vals():
    yield 1
    yield 2
    yield 3

gen = get_gen_vals()

for x in gen:
    print(x)
#
# # OR:-
#
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

# OR---:
print(list(gen)) # [1,2,3]

# OR---:
print(tuple(gen)) # [1,2,3]



# --------------------: Generator Expression

# tuple(x for x in range(10))    # ✅ Tuple from generator

gen = (x*x for x in range(3)) # ✅ Generator Expression
print(gen) # <generator object <genexpr> at 0x739a9790bb90>
for x in gen:
    print(x) # 0   1   4



#-----------

gen = (x* x for x in range(5) if x % 2 == 0)
print(f'List: {list(gen)}') # [0, 4, 16]
print(f'Tuple: {tuple(gen)}') # (0, 4, 16)
print(f'Next: {next(gen)}') # 0
print(f'Next: {next(gen)}') # 4
print(f'Next: {next(gen)}') # 16
print(f'Next: {next(gen)}') # StopIteration Error



# ----------------------: Genrator : generating even nums upto 10:


def GenEven():
    number = 0
    while number <= 10:
        yield number
        number += 2

obj = GenEven()

print(f'Val 1 : {next(obj)}') # 0
print(f'Val 2 : {next(obj)}') # 2
print(f'Val 3 : {next(obj)}') # 4
print(f'Val 4 : {next(obj)}') # 6
print(f'Val 5 : {next(obj)}') # 8
print(f'Val 6 : {next(obj)}') # 10
print(f'Val 7 : {next(obj)}') # StopIteration error occurs when generator is exhausted.

## OR: --
List_obj = list(obj)


## OR: --

for index , value in enumerate(obj):
    print(f'Val {index} : {value}')


#############-------######################--------::::::::::::::
#############-------######################--------::::::::::::::: Lambda
#############-------######################--------::::::::::::::

# lambda is an small anonymus fuction , takes any no.of arguments , only have 1 expression(+,-,*,/)
#:  you can reuse a lambda function by assigning it to a variable

x = lambda a : a+10
Y = lambda a,b : a+b

print(x(5))
print(Y(5,5))
print(x(25))


var = []
lam = lambda x: x.strip()
var.append(lam(' ahsan   '))
print(var) # ['ahsan']

#############-------######################--------::::::::::::::
#############-------######################--------::::::::::::::: Scope
#############-------######################--------::::::::::::::
# variable is only available inside the region where it is created , this is scope bcz variable belongs to the
# local scope of that function.
# mean if varibale or function is created inside an function , then trying to acess them outside the parent
# function , we will not get them , and error occurs.
# fun cant be gloablized using global keyword... but vars can be ...

# ----------------: Local Scope
#
def fun():
    A = 200
    if "1" == "1":
        def Fun2():
            print(A) # 200
        Fun2()
fun()

print(A) # error through hoga , thats scope
Fun2()   # error through hoga , thats scope


# ----------------: Global Scope
# variable created in  main body of   code is a global variable and belongs to the global scope and is
# available from within any scope, global and local.
# For example , constructor m jo self.Variable banate han , wo global scope ka hota , jider mrzi use krlo.

x = 300
def Fun():
    print(x)
Fun()

# ----------------: Global Keyword
# If you need to create a global variable that can be used inside,outside the functions , use Global keyword
# syntax: global Variable_Name
#               Variable Value
def Fun():
    global x
    x = 100
    print(x)
Fun()
print(x)


# can change the value of any variable by specifying it global at other place , global value will be
# used then at every place.
x = 50
def fun():
    global x
    x= 20
fun()
print(x)

#-----> Not possible :- , same function ma global declare ho and ussay pehlay use kiya ho var , is not sllowed.
A = 100
print(A)
def Fun():
    print(A) # SyntaxError: name 'A' is used prior to global declaration
    global A
    A = 200

Fun()
print(A)

# -------> Non_Local <-------: The nonlocal keyword makes the variable belong to the outer , nearest enclosing
# function (but not makes global).
# variable should also be present in outer fun.
# nonlocal keyword is used in inner nested function, effecting immediate enclosing function...
# only diff b/w global and non_local is , by global it changes for everyplace but non_local does same thing for nearest enclosing fun and only works in nested fun.

x = 10
print(f'No Effect: {x}') # 10

def outer():
    x = 10
    print(f'X in outer: {x}') # 10 , bcz effect takes place after inner fun calling...

    def inner():
        nonlocal x
        x = 20
        print(f'X in inner: {x}') # 20
    inner()

    print(f'X in outer: {x}') # 20

outer()

print(f'No Effect: {x}') # 10

# #----------------------------------------------------------------> Is_Instance() <------------------------------------
#
# isinstance() is used to check that object belongs to which class or data type
# Syntax: isinstance(object , classinfo)
# object : var or value to check
# classinfo : data type or class , to compare against
# Returns True if object matches type otherwise false.
#
# -Example:-
x = 10
print(isinstance(x, int))   # True
print(isinstance(x, float)) # False
print(isinstance(x, str))   # False

# --> Checking againt tuple:
print(isinstance(x , (float , str) ))   # false
print(isinstance(x , (float , str , int) ))   # true , any 1 true will print true


# -----> Why Use isinstance() Instead of type()?
#
# Handles Inheritance: isinstance() considers subclasses, while type() does not.
# Flexible: Allows checking against multiple types at once using a tuple.
#
# -- Example:-

class Animal:
    pass

class Dog(Animal):
    pass

object = Dog()

print(isinstance( object , Animal  ))  # True
print(isinstance(object,Dog))        #   True
print(type(object)) # <class '_main_.Dog'>
print(type(object) == Dog )          #    True
print(type(object) == Animal)        #   False  ,inherit bi ha phr bi false , so dont use it.
#
#
# ------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------->  Map & Strip <----------------------------------------------------
#
# Map & Strip Function:---
# map function is used to apply a function to a iterable list or tuple and returns a map object , which is a iteratable.--> map(function, iterable)
# strip removes any white spaces beginning or end of string.
# Example1:
#
s = ['1','2','3']
res = map(int,s)
print(res) #  <map object at 0x7b030f8fae90>
# loop
for x in res:
    print(x)  #   1    2     3
# list
map_list = list(res)
print(map_list) # [1, 2, 3]
#
# tuple
data = ['1','2']
res = map(int, data)
print(tuple(res))  # (1, 2)
#
#
#- Next
data = ['1','2']
res = map(int, data)
print(next(res))
print(next(res))
print(next(res)) # StopIteration






# Example2:
def fun(a, b):
    return a + b
res = map(fun, (1, 2, 3), (1, 2, 3))
print(tuple(res))  # (2, 4, 6)
#
# Exp-3:-
data = [1,2,3]
res = list(map(lambda r: r*2 , data))
print(res)
#
#
# -Exp-4:-

fruits = ['apple','peach']
print(list(map(lambda r: r.title(), fruits)))  # ['Apple', 'Peach']

# Exp-4:-
#
s = ['heloo ', '  python']
res = list(map(str.strip , s))
print(res) # ['heloo', 'python']
#

data = [' a ','  b ']
res = list(map(lambda r: r.strip(), data))



# ------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------->  Filter  <----------------------------------------------------

# Filter method filters any sequence with the help of an function that tests each element to be true or not.
# The filter() function in Python filters elements from an iterable (like a list) based on a function.
# Syntax: filter(function, sequence)
# returns filter object: <filter object at 0x00000183FD39ACB0> without list.
# Point: filter does not transform items, only keep items where function returns True,
# filter return orignal element not result,
#

#-----------------
def EVEN(n):
    return n % 2 == 0

res = filter(EVEN, [1,2,3,4,5,6])

print(f'{next(res)}') # 2
print(f'{next(res)}') # 4
print(f'{next(res)}') # 6
print(f'{next(res)}') # StopIteration




# whether sums equals 3:
def fun(n):
    return n + 2 == 3

res = filter(fun , [1,2,3])
print(list(res)) # [1]

# whether sum equals 0
res = list(filter( lambda r: r + 2 == 0 , [1,2,3,-2] ))
print(res) # [-2]


# sum items simply:
def eve(n):
    return n + 2

res = filter(eve, [1, 2, 3])
print(list(res)) # [1,2,3]
#  bcz 1+2 = True , possible , 2+1 = True again possible , all three items pass the filter so returning true , filter just checks weather result is true or not.



# Fitler to check even nums...:-
def fun(n):
    return n % 2 == 0
res = filter(fun , [1,2,3,4,5,6])
print(list(res)) # [2, 4, 6]



# ------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------->  Eval()  <----------------------------------------------------


# Eval Function takes the  argument and evaluates it as python code and runs it.

# Syntax: eval(expression, globals=None, locals=None)
# expression = string is passed and evaluates as python expression.
# globals = dict to specify available global method,vars.
# locals =  Another dictionary to specify the available local methods and variables.


expr = 'x*(x+1)*(x+2)'
x = 5
res = eval(expr)
print(res) # 210


def Fun():
    expr = 'x*(x+1)*(x+2)'
    x = 5
    Result = eval(expr, globals=None, locals=None)
    print(Result) # 210
Fun()


x= 5
R1 = x + 0
print(eval('not x is None')) # True
print(eval('x is None')) # False
print(eval('R1 == 5'))   # True
print(eval('R1 != 5'))   # False
print(eval('x%2==0'))    # False as 5 is odd not even


# Vulnerability issues with Python eval() Function
# We can get any function access by eval as eval will execute anything passed to it.
#
def secret_function():
    return '1234'

def Eval():
    result = eval( secret_function() )
    print(f'Result: {result}')

Eval()


# ----------------------------------------------------------------:  Making eval() safe  :------------------------------
#
# Setting {"_builtins_": None} inside eval() disables Python’s built-in functions and modules, preventing the execution of potentially dangerous code, also auto applied to our local funs.
#
# Here we make all builtin function access blocked:
res = eval("print('Ahsan')"  ,{"_builtins_": None}) # 'NoneType' object is not subscriptable
#
# Here we specified , what to allow:
res = eval("print('Ahsan')"  ,{"_builtins_": None,'print': print}) # Ahsan

#---
def sec_fun():
    print('SEC FUN')

res = eval('sec_fun()', {'_builtins_': None,'sec_fun': sec_fun}) # SEC FUN


#--- local + global funs can be placed inside an single dict, any var name can be chosen for dict and more then 1 fun can be called from given dict.

def sec_fun():
    print('SEC FUN')

local_dict = {'print':print , 'sec_fun': sec_fun}

res = eval('print("Print Used Here"),sec_fun()',{'_builtins_':None},local_dict) # Print Used Here  ---  # SEC FUN

#-- pass builtins : none in global or local.

def sec_fun():
    print('SEC FUN')

local_dict = {'sec_fun': sec_fun}

global_dict = {'print':print}

expression = 'print("Print Used Here"),sec_fun()'

res = eval(expression,{'_builtins_':None},local_dict,global_dict) # TypeError: eval expected at most 3 arguments, got 4


#---  So pass builtins none inside global or local.

globals_dict = {
    '_builtins_': None,
    'print': print,
}


#
# Why Safe_Dict?
# as our own local methods got blocked due to using builtins:None , so we pass an safe_dict in that we will speicify funs which can be evaluated and using one at a time as expression.
# can make it safe by using an dictionary and passing variable , functions that should be accessed inside it and calling any by passing in expr.
#
# Exp-0:-
#
def Evaluate_Fun():
    safe_dict = {'x':5}
    expression = "x*5"
    response = eval(expression, {'_builtins_':None }, safe_dict)
    print(response) #
Evaluate_Fun()


# ---- Exp1:
#
def testing_eval():
    data = [1,2,3]
    res = list(filter(lambda r:r%2==0 , data))
    print(f'Even Result: {res}')

response = eval('testing_eval()',{'_builtins_':None, 'testing_eval':testing_eval})



# ---Exp-2:-

def secret_function():
    return "Secret Key 911"

def evaluate_fun():
    safe_dict = {"x": 5, "secret_function": secret_function}   # Added function
    expr = "secret_function()"  # Now eval can find it

    result = eval(expr, {"_builtins_": None}, safe_dict)
    print(f"Result: {result}")

evaluate_fun()

# - Exp-3:- not included in safe dict then error.------>

def secret_function():
    return "Secret Key 911"

def evaluate_fun():
    safe_dict = {"x": 5}
    expr = "secret_function()"

    result = eval(expr, {"_builtins_": None}, safe_dict)
    print(f"Result: {result}")

evaluate_fun()   # NoneType' object is not subscriptable : as sec_fun not added in dict.


# ------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------->  Any()  <----------------------------------------------------


# Python Any Function returns true if any of the iterables are true as 1,true or other ,
# returns false if false or 0 or empty string or list,dict,set,tuple. in dict it check keys not vals.
#
# -------------------------------- Exp-1:-
testing_any = any([0,True,0])
print(testing_any)   # True

testing_any = any([False]) # False
testing_any = any([]) # False
testing_any = any( ()  ) # False

string_test = 'Hy' # True
string_test = '' # False

# ------------------------------- Exp-2:-

List = [1,2,3,4,5]

res = any(item > 2 for item in List)
print(f'Res: {res}') # True

# this function gives same result as built-in any() function
def Customr_Any():
    for x in List:
        return True
    return False
print(Customr_Any()) # True


# ------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------->  All()  <----------------------------------------------------
# The Python all() function returns true if all  items of  iterable (List, Dictionary, Tuple, set, etc.) are True
# otherwise it returns False. It also returns True if the iterable object is empty.
#
# Why To Use?
# Sometimes working on some code if we want to ensure that user has not entered a False value then we use the all() function.

# testing_all = [4,5,1]
# print(all(testing_all)) # True

# testing_all = []
# print(all(testing_all)) # True , on empty but not on false

# testing_all = [False]
# print(all(testing_all)) # False

# testing_all = [4,5,33]
# print(all(x > 5 for x in testing_all)) # False , as all are not greater then 0
# print(all(x > 0 for x in testing_all)) # True , as all are greater then 0
# print(all(x%2==0  for x in testing_all)) # False
# print(all({0: 22 , 1: 22})) # False


# s = '000'
# print(all(s)) # True


# --------------------------------------- Split -------------------------------------#


# Split Method splits the string into list , we can specify the separator but default separator is whitespace
# max split : optional ,specifies how many splits we want , default val -1 mean all.its index val.


# Default Separator
String = 'Ahsan Khan'
Split = String.split()
print(Split) # ['Ahsan', 'Khan']

# ------

String = 'hello, my name is Peter, I am 26 years old'
Split =  String.split(' ',2)
print(Split) # ['hello,', 'my', 'name is Peter, I am 26 years old']  2 means index , that why 3 occurs.

# --------------------------------------- Join -------------------------------------#

# Join takes the elements in iterable form and joins them in 1 list using any thing inside '' called separator and returns values as strings.
# takes the keys as default in dictionary.
# Note: If the key of the string is not a string, it raises the TypeError exception.---> Dict
#
Tuple = ('john','peter')
x = ''.join(Tuple)
print(x) # johnpeter


Dict = {'name': 'Pak' , 'Country': 'Pacific'}
x = ''.join(Dict)
print(x) # nameCountry


Dict = {'name': 'Pak' , 'Country': 'Pacific'}
x = ''.join(Dict.values())
print(x)


# -------------------------: Sorted :----------------------------------------
# sorted function takes iterable and  returns the sorted list of iterable object.
# strings are sorted alphabeticly and numbers numerically.we can not sort both abc,123 at a time.
# Returns an list of sorted vals. tuple dont have sort so we use sorted.
# Syntax:-----------            Sorted(iterable,key=key,reverse=True)


data = ('ab','ism','asn')
Sort = sorted(data,reverse=False)
print(Sort) # ['ab', 'asn', 'ism']

Sort = sorted(data,key=len)
print(Sort)   # ['24', '755', '1111', '43345']  : only for str not int.

# Exp-2--------------:
# List ke ander dictionary ko hum .get('') krKe access krte han.

Bikes = [
    {'model':'Yamaha 100', 'price':200},
    {'model': 'Suzuki 110', 'price':450},
    {'model':'Honda 70', 'price':100}
]
Sort = sorted(Bikes , key=lambda x : x.get('price'))
print(Sort)


# -------------------------------: Zip :-------------------------------------------
# it takes any iterable object as input and 1st items of each iterable are paired together.
# returns zip object in tuple form and if input iterables are of unequal lenght then zip stops when shortest iterable is exhausted(completed).
# -------: zip(iterator1, iterator2, iterator3 ...)


list1 = [1,2,3]
list2= [4,5,6,7]
res = zip(list1, list2)
print(res)                                      # <zip object at 0x7cc3eca1e680>
print(list(res))                                # [(1, 4), (2, 5), (3, 6)]


#--------------------------------: Loop + List + tuple + Next , any one can be used on zip object , as all objects of any (generator,map,zip) have these operations.
data1 = ['a','b','c']
data2 = ['d','e','f']

#--List response
list_res = list(zip(data1, data2))
print(list_res) # [('a',), ('b',), ('c',)]

#--Tuple response
tuple_res = tuple(zip(data1, data2))
print(tuple_res) # (('a', 'd'), ('b', 'e'), ('c', 'f'))

#-- for loop
for x in zip(data1, data2):
    print(f'Tuple: {x}') # Tuple: ('a', 'd') , Tuple: ('b', 'e') , Tuple: ('c', 'f')

next_res = zip(data1, data2)
print(next(next_res)) # ('a', 'd')
print(next(next_res)) # ('b', 'e')
print(next(next_res)) # ('c', 'f')






#--- 1 iterable is allowed.
a = ['a','b','c']
res = list(zip(a))
print(res) # [('a',), ('b',), ('c',)]


A = ('asn','Mr')
B = ('khan','ism')
Zip = zip(A, B)
print(tuple(Zip)) # (('asn', 'khan'), ('Mr', 'ism'))


# Looping:--- Return greater element in each tuple.
l1 = [111,22,33]
l2 = [11,22,333]

for x in zip(l1, l2):
    print(max(x)) # returns 1 element form tuple which is greater.


#----- Dictionary zip

d = {'name': 'AA', 'age': 1900, 'grade': 'CC'}

res = zip(d)
print(list(res))  # [('name',), ('age',), ('grade',)]

res_keys = zip(d.keys())
print(list(res_keys))  # [('name',), ('age',), ('grade',)]

res_vals = zip(d.values())
print(list(res_vals))  # [('AA',), (1900,), ('CC',)]

res_items = zip(d.items())
print(list(res_items))  # [(('name', 'AA'),), (('age', 1900),), (('grade', 'CC'),)]




#--- Unzipping Zip: From Structure

ZIP_Data = [('a',1),('b',2)]
strings , integers = zip(*ZIP_Data)
print(strings) # ('a', 'b')
print(integers) # (1, 2)

# Unzipping Zip-Object

listy =['a','b','c']
listy2 = [1,2,3]
res = zip(listy, listy2)

strings , integers = zip(*res)
print(strings) # ('a', 'b', 'c')
print(integers) # (1, 2, 3)













    


























  
            

    
    





  