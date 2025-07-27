user_password=input("Enter the password:")
encrypt_password=""
for char in user_password:
         ascii_value=ord(char)
         shifted_value=ascii_value+5
         encrypted_char=chr(shifted_value)
         print(f'Encrypted_password:"{encrypt_password}')
    
def check_is_digit():
    user_recovery_pin=input("Enter recovery pin:")    
    if  user_recovery_pin.isdigit():
        print("user_recovery_pin",user_recovery_pin)
    else:
         print("none")
         
         
         
    initial_balance=float(input("Enter the balance:"))
    if initial_balance>=0:
        print("valid input")
        print(initial_balance)
    else:
        print("error")
        print("Repeat process")
         
    user_transferable_account_numbers=input("Enter transferable_account_number:")
    if user_transferable_account_numbers.isdigit():
         print(user_transferable_account_numbers)
    else:
        print("error prompt again")
        
        
    account_holder_name=input("Enter acc_holder_name:")
    if account_holder_name and account_number:
        last_two_digit=account_number[-2:]
        login_id=account_holder_name + last_two_digit
        print(login_id)
    else:
         print("invalid account number")
   #Display the Encrypted password for login step
    print(f'Encrypted_password:"{encrypt_password}')
     
         
    
check_is_digit()
        

     

def Account_login():
    
         
     
bank_account_number=input("Enter the bank_account_number:")
pin=input("Enter the pin:")
recovery_pin=input("Enter the recovery_pin:")
    
try:
      while pin==recovery_pin:
          raise ValueError('Pin & Recovery PIN can not same')
except Exception as e:
         print(e)
    
    
    
    
    
    
    
 
      account_number=input("Enter Account number:")
      account_pin=input("Enter the pin")  
      if account_number==bank_account_number and account_pin==pin:
          print("login successfully")
     
    
      else:
        print('details are not correct')
        print('1.choice==1')
        print('2.choice==2')
        
        choice=input("Enter  choice number=1/ choice number=2")
        if(choice==1):
          print("enter details again")
          Account_login()
        elif choice==2:
          print("forget password")
          recovery_pin=input("Enter the recovery pin:")
          while recovery_pin!=pin:
           print('reset the password')
          
        else:
            print("Input error")
            new_password=input("Enter new password:")
            print(f'THE Reset password is:{new_password}')
            
     account_type=input("choose savings/current:")
     print(account_type)
     
     Account_login()
        
    
  