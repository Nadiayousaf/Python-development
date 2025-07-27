
#Basic Calculator project

'''def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")


    while True:
        choice = input("Enter choice (1/2/3/4/53): ")

        if choice == '5':
            print("Exiting the calculator.")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid choice! Please select a valid operation.")'''

#second project
#Text Analyzer

'''def count_vowels(user_input):
    vowels="AEIOUaeiou"
    count=0
    for char in user_input:
        if char in vowels:
            count += 1
    return count

def count_consonents(user_input):
    vowels="AEIOUaeiou"
    count=0
    for char in user_input:
        if char .isalpha()and char not in vowels:
            count+=1
    return count

def is_digit(user_input):
    count = 0
    for char in user_input:
        if char.isdigit():
            count += 1
    return count

def count_specific_word(user_input,specific_word):
 count = 0
 target_word='is'
 words = user_input.split()
 for word in words:
  if word == target_word:
            count += 1
 return count

specific_word=input("Enter the String:")
user_input=input("Enter the string")
count=count_specific_word(user_input,specific_word)
#user input handling for text for dyanamic text analysis
def main():
    user_input=input("Enter text for analysis:")
    specific_word=input("Enter the string:")
    print("Text analysis result")
    print(f"The number of vowels in the string is:{count_vowels(user_input)}")
    print(f"The number of consonents in the string is:'{count_consonents(user_input)}")
    print(f"Digit count: {is_digit(user_input)}")
    print(f"The '{specific_word}'appears in {count}times")
if __name__ == "__main__":
    main()'''


#third project
#Password strength checker

'''def password_strength_checker():
 password=input("Enter the string:")
 strength='weak'
 has=False
 has_lower=False
 has_digit=False
 has_special_character=False
 if len(password)<8:
        strength='weak'
 elif(len(password)>=8):
        strength='Strong'
 else:
        strength='Moderate'

 for  char in password:
    if char .isupper():
        has_upper=True
    elif(char.islower()):
        has_lower=True
    elif(char.isdigit()):
        has_digit=True
    elif(char in("@,#,!,$,^,&,*,<,>,")):
        has_special_char=True 
    common_patterns='ABCD','1234567','password'
    if password in common_patterns:
            strength='Weak'
    elif password not in common_patterns:
            strength="strong"
            
            print(f'password Strength{strength}')
password_strength_checker()'''



def ATM_Machine():
    print("Welcome to Python Bank ATM")

    def Account_creation():
        user_name = input("Enter the full name: ")
        user_password = input("Enter the password: ")

        encrypt_password = ""
        for char in user_password:
            ascii_value = ord(char)
            shifted_value = ascii_value + 5
            encrypted_char = chr(shifted_value)
            encrypt_password += encrypted_char

        print(f'Encrypted password: "{encrypt_password}"')
        account_number = input("Enter account number: ")

        user_recovery_pin = input("Enter recovery pin: ")
        if user_recovery_pin.isdigit():
            print("User  recovery pin:", user_recovery_pin)
        else:
            print("Invalid recovery pin")

        account_holder_name = input("Enter account holder name: ")
        if account_holder_name and account_number:
            last_two_digit = account_number[-2:]
            login_id = account_holder_name + last_two_digit
            print("Login ID:", login_id)
        else:
            print("Invalid account number")
            return None

        user_transferable_account_numbers = input("Enter transferable account number: ")
        if user_transferable_account_numbers.isdigit():
            print("Transferable account number:", user_transferable_account_numbers)
        else:
            print("Error: Please enter a valid account number")

        return login_id, encrypt_password, user_recovery_pin

    def Account_login(login_id, encrypt_password, user_recovery_pin):
        if login_id and encrypt_password:
            print("Proceed to ATM menu")
        else:
            print("Invalid login")
            print("1. Re-login")
            print("2. Forget password")
            choice = input("Enter choice number (1 or 2): ")
            if choice == '1':
                print("Re-login")
                Account_login(login_id, encrypt_password, user_recovery_pin)
            elif choice == '2':
                recovery_pin = input("Enter recovery pin: ")
                account_number = input("Enter account number: ")
                if recovery_pin == user_recovery_pin:
                    print(f'Encrypted password: {encrypt_password}')
                else:
                    print("Invalid recovery pin")

    login_id, encrypt_password, user_recovery_pin=Account_creation()

    if login_id and encrypt_password:
     Account_login(login_id, encrypt_password, user_recovery_pin)

ATM_Machine()
        
        
    
        
        
    
        


