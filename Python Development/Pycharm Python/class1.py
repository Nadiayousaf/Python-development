'''a=1
print(a,id(a))
c={1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4}
print(c)'''



'''s=['1','2','3']
res=list(map(s))
print(s)

number=int(input("Enter the number:"))
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
    print("not weired"
else:
    print(exit)   
'''



def ATM_Machine():
 
    print("Wellcome to python bank ATM")
  
    def Account_creation():
         user_name=input("Enter the full name:")
         user_password=input("Enter the password:")
 
         encrypt_password=""
         for char in user_password:
            ascii_value=ord(char)
            shifted_value=ascii_value+5
            encrypted_char=chr(shifted_value)
            encrypt_password+=encrypted_char
    
         print(f'Encrypted_password:"{encrypt_password}')
         account_number=input("Enter account number:")
 
         user_recovery_pin=input("Enter recovery pin:")    
         if  user_recovery_pin.isdigit():
            print("user_recovery_pin",user_recovery_pin)
         else:
           print("none")
         
         account_holder_name=input("Enter acc_holder_name:")
         if account_holder_name and account_number:
           last_two_digit=account_number[-2:]
           login_id=account_holder_name + last_two_digit
           print(login_id)
         else:
          print("invalid account number")  
          return None    
        
         while True:
          user_transferable_account_numbers=input("Enter transferable_account_number:")
          if user_transferable_account_numbers.isdigit():
              print("Valid transferable account number:", user_transferable_account_numbers)
              break
          else:
            print("error prompt again")
          
         return login_id, encrypt_password, user_recovery_pin,user_transferable_account_numbers
     
    
    
    def Account_login(login_id, encrypt_password, user_recovery_pin):
      if login_id and encrypt_password():
           print("proceed to ATM menu")
      else:
            print("invalid login")
            print("1.choice 1")
            print("2.choice 2")
      choice=input("Enter  choice number=1/ choice number=2")
      if(choice==1):
             print("to Re_login")
             Account_login()
      elif (choice==2):
             print("forget password")
             recovery_pin=input("Enter  recovery pin:")
             Account_number=input("Enter Account_number:")
      while recovery_pin != user_recovery_pin:
             print(f'Encrypted password: {encrypt_password}')
             

      Account_login(login_id,encrypt_password,user_recovery_pin)  
      Account_creation() 
    
             

    def main():
       atm_user_data=None
       while True:
        print("\n--- Welcome to Python Bank ATM ---")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            atm_user_data=Account_creation()
        elif choice == "2":
            if atm_user_data:
                atm_user_data=Account_login()
            else:
                print("You need to create an account first.")
        elif choice == "3":
            print("Thank you for using Python Bank. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
       main()
    







'''login_id, encrypt_password, user_recovery_pin,user_transferable_account_numbers=Account_creation()
    
    if login_id and encrypt_password:        
     Account_login(login_id, encrypt_password, user_recovery_pin) '''  