def Atm_Machine():
    user_name = input("Enter the name:")
    user_password = input("Enter the password")
    encrypt_password = ""
    for char in user_password:
     ascii_value = ord(char)
     shifted_value = ascii_value + 5
     encrypted_char = chr(shifted_value)
     encrypt_password+=encrypted_char
     print("Encrypted password:{encrypt_password}")

    recovery_pin= input("Enter the pin:")
    enter_pin=input("Enter the pin:")
    if enter_pin==recovery_pin:
        print("correct_password")
    else:
        print("incorrect_password")


    try:
        initial_balance = float(input("Enter the balance:"))
        if initial_balance> 0:
            print("Valid input")
            print("balance:",initial_balance)
            raise ValueError(print("Invalid input"))
        else:
            print("Incorrect_input")
    except Exception as e:
        print(e)

    transferable_account_number=input("Enter transferable account number:")
    try:
        if  transferable_account_number.isdigit():
         print("valid_input")
        raise ValueError(print("prompt again"))

    except Exception as e:
        print(e)

    acc_holder_name=input("Enter the account holder name:")
    if acc_holder_name.isdigit():
        last_two_digits=acc_holder_name[-2:]
        login_id=acc_holder_name + last_two_digits
        print("login id:",login_id)

        





Atm_Machine()