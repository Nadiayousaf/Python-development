

  
        
  #basic calculator (functions,loops,user input,try and except exception handling ,conditions)
    #Basic project
    
    
    
def add (x,y):
 return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
   if y==0:
    return("Error division by zero.")

    return(x/y)
def calculator():
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    
    while True:
        choice=input("Enter the choice(1/2/3/4/5):")
        if choice=='5':
            print("exiting the calculator")
            break
        if choice in[1,2,3,4]:
            try:
                num1=float(input("Enter the first number:"))
                num2=float(input("Enter the seccond number:"))
            except ValueError:
                print("invalid input data")
                continue
            
            
            
        if choice=='1':
          print(f"{num1}+{num2}=add{num1,num2}")
        elif choice=='2':
          print(f"{num1}-{num2}=subtrat{num1,num2}")
        elif choice=='3':
          print(f"{num1}*{num2}=mltiply{num1,num2}")
        elif choice=='4':
         print(f"{num1}/{num2}=divide{num1,num2}")
    else:
                print("maths error")
          
if_name_=="_main_":
calculator()




      
    
                
                