
def Atm_Machine():

 amount1=1000
 amount2=5000000
 pin=88
 at=0
 name=""
 amunt=0
 receipt=0
 ovral=0
 amntsnd=0
 last=0
 rsi=0
 def Account_Creation():
     print("Enter your card at terminal")
     print("card-Entered")
     print("Wellcome to the Western-Union Atm")
     def handle_pin():
       print("Enter pin:")
       entered_pin = int(input())
       if entered_pin ==pin:
           print("pin is correct")
           print("Select Your Operation:")
           print("press 1 for :Current_Account")
           print("Press 2 for:Savings_Account")
           print("Press 3 for:Business_Account")
           at=int(input())
           print("you Select:Current Account")
           def Account_Selection():

               print("Select Operations")
               print("Press 1 For:Amount With-drawl")
               print("Press 2 For:Amount_send")
               print("press 3 For:Balance_check")
               def With_drawl():

                   print("How many Amount you with draw?")
                   print("For 1000:press 1")
                   print("For 500:press 2")
                   print("For custom:press 3")
                 def receipt():
                   amunt=int(input())
                   if amunt == 1:
                       print("yes:press 1")
                       print("No:press 2")
                       receipt = int(input())
                       if receipt == 1:
                           print("Transaction Successful")
                           print("Take your receipt from R-Box")
                           print("Please take your card")
                           print(f"collect your{amount1} at terminal ")
                       elif receipt == 2:
                           print("Transaction Successful")
                           print("Please take your card")
                           print(f"collect your{amount1}at terminal")
                   elif amunt == 2:
                       print("Do you want a receipt?")
                       print("Yes:Press 1")
                       print("No:Press 2")
                       receipt = int(input())
                       if receipt == 1:
                           print("Transaction successful")
                           print("Take Your receipt from R-Box")
                           print("Please take your card")
                           print(f"collect your {amount2}at terminal")
                       elif receipt == 2:
                           print("Transaction Successful")
                           print("Please take Your card")
                           print(f"collect your {amount2}at terminal")


                   else:
                       print("Enter amount for with-drawl")
                       amunt = int(input())
                       if (amunt >= 12000):
                           print("Transaction failed")
                           print("Amount Exceeds Limit")
                       elif (amunt <= 10000):
                           print("Are you wanna receipt")
                           print("yes:press 1")
                           print("No:press 2")
                           receipt = int(input())
                           if receipt == 1:
                               print("Transaction Successful")
                               print("Take your receipt from R-Box")
                               print("Please take your card")
                               print(f"collect your {amunt}at terminal")
                           elif receipt == 2:
                               print("Transaction Successful")
                               print("Please take your card")
                               print(f"collect {amunt}at terminal")
                 def amount_send():
                   print("Enter 4 digit Act Number of Receiver")
                   rsi = int(input())
                   print("Enter Amount")
                   amntsnd = int(input())
                   if (amntsnd <= 100000):
                       print(f"Amount{amntsnd} transferred successfully to {rsi}")
                   elif (amntsnd >= 100001):
                       print("Amount exceeds the limit")
                       print("Transaction Impossible")
                 def show_balance():
                   print("current balance is: ($)5M-USD")

       elif  entered_pin!=pin:
           print("pin is in-correct")
           print("Select any option:")
           print("press 1 for: Again Entering pin")
           print("press 2 for: for forget pin")
           option=int(input())
           if option==1:
               handle_pin()
           elif option==2:
               print("Enter your username for viewing pin")
               name = input("Enter the name:")
               if name == "nadia":
                   print("pin is:88")
               else:
                   print("user name is invalid")
       else:
           print("Enter user-name for pin recovery:")
           name = input("Enter name:")
           if name == "nadia":
               print("Pin is:88")
               print("Account Created Successfully")
           else:
               print("User name is invalid")

         Account_Selection()
     handle_pin()
 Account_Creation()
Atm_Machine()