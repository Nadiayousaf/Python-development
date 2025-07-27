def Atm_machine():
    print("Welcome to Atm Machine")

    def Account_creation():
       user_name = input("Enter full name:")
       user_password = input("Enter password:")

       encrypt_password=""
       for char in user_password:
         ascii_value=ord(char)
         shifted_value=ascii_value+5
         encrypt_char=chr(shifted_value)
         encrypt_password+=encrypt_char
       print(f"Encrypted password:,{encrypt_password}")

       account_number = input("Enter account number:")

       recovery_pin=int(input("Enter recovery_pin:"))
       if recovery_pin==encrypt_password:
            print("valid input")
       else:
            print("Invalid input")

       try:
          initial_balance=float(input("Enter the balance:"))
          if initial_balance >0:
             print("balance",initial_balance)
          else:
             raise ValueError("balance must be greater than 0")
       except Exception as e:
             print("error",e)


       user_transferable_account_number=input("Enter transferable_account_number:")
       try:
          if user_transferable_account_number.isdigit():
            print("user_transferable_account_number:",user_transferable_account_number)
          raise ValueError("Account number must be digits only")
       except Exception as e:
            print("prompt again",e)

       account_holder_name=input("Enter account_holder_name:")
       if  not account_holder_name.isdigit() and account_number:
          last_two_digits=account_number[-2:]
          login_id=account_holder_name+last_two_digits
          print("login_id:",login_id)
          print("Account created Successfully")
       else:
          print("Invalid account number")


       return login_id, encrypt_password, recovery_pin


    def Account_login(login_id, encrypt_password, user_recovery_pin):
         while True:
            print("\n---login portal---")

            if login_id and  encrypt_password:
               print(" login successful,..Proceed to ATM menu")
               break
            else:
                print("Invalid login")
                print("1. Re-login")
                print("2. Forget password")
                choice = input("Enter choice number (1 or 2): ")
                if choice == '1':
                   print("Re-login")

                elif choice == '2':
                   recovery_pin = input("Enter recovery pin: ")
                   account_number = input("Enter account number: ")
                   if recovery_pin == user_recovery_pin:
                     print(f'Encrypted password: {encrypt_password}')
                   else:
                     print("Invalid recovery pin")
                else:
                     print("Try again")
    login_id, encrypt_password, user_recovery_pin = Account_creation()
    if login_id and encrypt_password:
     Account_login(login_id, encrypt_password, user_recovery_pin)
    else:
        print(" Account creation failed. Cannot proceed to login.")
    Account_creation()

Atm_machine()