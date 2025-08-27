
def Atm_Machine():

 amount1=1000
 amount2=5000000
 pin=0
 at=0
 name=""
 amunt=0
 receipt=0
 ovral=0
 amntsnd=0
 last=0
 rsi=0
 print("Enter your card at terminal")
 print("card-Entered")
 print("Wellcome to the Western-Union Atm")
 print("please Enter your pin")
 pin=int(input())
 if pin==88:
     print("pin is correct")
     print("Select Your Operation:")
     print("press 1 for :Current_Account")
     print("Press 2 for:Savings_Account")
     print("Press 3 for:Business_Account")

     at=int(input())
     match at:
         case 1:
             print("You select:Current Account")
             print("Select Operations")
             print("Press 1 For:Amount With-drawl")
             print("Press 2 For:Amount_send")
             print("press 3 For:Balance_check")
             ovral=int(input())
             if ovral==1:
              print("How many Amount you with draw?")
              print("For 1000:press 1")
              print("For 500:press 2")
              print("For custom:press 3")

              if amunt==1:
                  print("yes:press 1")
                  print("No:press 2")
                  receipt=int(input())
                  if receipt==1:
                      print("Transaction Successful")
                      print("Take your receipt from R-Box")
                      print("Please take your card")
                      print(f"collect your{amount1} at terminal ")
                  elif receipt==2:
                      print("Transaction Successful")
                      print("Please take your card")
                      print(f"collect your{amount1}at terminal")
              elif amunt==2:
                  print("Do you want a receipt?")
                  print("Yes:Press 1")
                  print("No:Press 2")
                  receipt=int(input())
                  if receipt==1:
                      print("Transaction successful")
                      print("Take Your receipt from R-Box")
                      print("Please take your card")
                      print(f"collect your {amount2}at terminal")
                  elif receipt==2:
                      print("Transaction Successful")
                      print("Please take Your card")
                      print(f"collect your {amount2}at terminal")


              else:
                  print("Enter amount for with-drawl")
                  amunt=int(input())
                  if(amunt>=12000):
                      print("Transaction failed")
                      print("Amount Exceeds Limit")
                  elif(amunt<=10000):
                      print("Are you wanna receipt")
                      print("yes:press 1")
                      print("No:press 2")
                      receipt=int(input())
                      if receipt==1:
                          print("Transaction Successful")
                          print("Take your receipt from R-Box")
                          print("Please take your card")
                          print(f"collect your {amunt}at terminal")
                      elif receipt==2:
                          print("Transaction Successful")
                          print("Please take your card")
                          print(f"collect {amunt}at terminal")
             elif ovral==2:
                 print("Enter 4 digit Act Number of Receiver")
                 rsi=int(input())
                 print("Enter Amount")
                 amntsnd=int(input())
                 if(amntsnd<=100000):
                     print(f"Amount{amntsnd} transferred successfully to {rsi}")
                 elif(amntsnd>=100001):
                     print("Amount exceeds the limit")
                     print("Transaction Impossible")
             else:
                 print("current balance is: ($)5M-USD")
         case 2:
                    print("You select:Savings Account")
                    print("Select Operations")
                    print("press 1 for:Amount with-drawl")
                    print("press 2 for:Amount-send")
                    print("press 3 for:Balance-Check")
                    ovral = int(input())
                    if ovral == 1:
                       print("How many Amount you with drawl?")

                       print("For 1000:press 1")
                       print("For 500:press 2")
                       print("For custom:press 3")
                       if amunt == 1:
                         print("yes:press 1")
                         print("NO:press 2")
                         receipt = int(input())
                         if receipt == 1:
                              print("Transaction Successful")
                              print("Take your receipt from R-box")
                              print('Please take your card')
                              print(f"collect your{amount1} at terminal ")
                         elif (receipt == 2):
                                  print("Transaction Successful")
                                  print("Please take your card")
                                  print(f"collect your{amount1}at terminal")
                       elif amunt == 2:
                          print("Are you wanna receipt")
                          print("Yes:Press 1")
                          print("No:Press 2")
                          receipt = int(input())
                          if receipt == 1:
                            print("Transaction successful")
                            print("Take your receipt from R-Box")
                            print("Please take your card")
                            print(f"collect your {amount2}at terminal")
                          elif receipt == 2:
                                print("Transaction Successful")
                                print("Please take your card")
                                print(f"collect your{amount2}at terminal")
                       else:
                               print("Enter Amount for With drawl")
                               amunt = int(input())
                               if (amunt >= 12000):
                                 print("Transaction failed")
                                 print("Amount Exceeds Limit")
                               elif (amunt<=10000):
                                     print("Are you wanna receipt")
                                     print("yes:press 1")
                                     print("No:Press 2")
                                     receipt = int(input())
                                     if receipt == 1:
                                         print("Transaction Successful")
                                         print("Take your receipt from R-Box")
                                         print("Please take your card")
                                         print(f"collect your {amunt}at terminal")
                                     elif receipt == 2:
                                      print("Transaction Successful")
                                      print("Please take your card")
                                      print(f"collect your {amunt}at terminal")
                               else:
                                      print("Enter Amount for With drawl")
                                      amunt = int(input())
                                      if (amunt >= 12000):
                                              print("Transaction failed")
                                              print("Amount Exceeds Limit")
                                      elif (amunt <= 10000):
                                               print("Are you wanna receipt")
                                               print("yes:press 1")
                                               print("NO:Press 2")
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
                    elif ovral == 2:
                          print("Enter  4-digit Act number of receiver")
                          rsi = int(input())
                          print("Enter Amount")
                          amntsnd = int(input())
                          if (amntsnd <= 100000):
                                   print(f"Amount{amntsnd} transferred successfully to {rsi}")
                          elif (amntsnd >= 100001):
                                      print("Amount exceeds the limit")
                                      print("Transaction Impossible")
                    else:
                                    print("current balance is: ($)5M-USD")
         case 3:
              print("You select:Business Account")
              print("Select Operations")
              print("press 1 for:Amount with-drawl")
              print("press 2 for:Amount-send")
              print("press 3 for:Balance-Check")
              ovral = int(input())
              if ovral == 1:
                 print("How many Amount you with drawl?")

                 print("For 1000:press 1")
                 print("For 500:press 2")
                 print("For custom:press 3")
                 if amunt == 1:
                    print("yes:press 1")
                    print("NO:press 2")
                    receipt = int(input())
                    if receipt == 1:
                       print("Transaction Successful")
                       print("Take your receipt from R-box")
                       print('Please take your card')
                       print(f"collect your{amount1} at terminal ")
                    elif receipt == 2:
                      print("Transaction Successful")
                      print("Please take your card")
                      print(f"collect your{amount1}at terminal")
                 elif amunt == 2:
                    print("Do you want to receipt")
                    print("Yes:Press 1")
                    print("No:Press 2")
                    receipt = int(input())
                    if receipt == 1:
                      print("Transaction successful")
                      print("Take your receipt from R-Box")
                      print("Please take your card")
                      print(f"collect your {amount2}at terminal")
                    elif receipt == 2:
                     print("Transaction Successful")
                     print("Please take your card")
                     print(f"collect your{amount2}at terminal")
                 else:
                     print("Enter Amount for With drawl")
                     amunt = int(input())
                     if (amunt >= 12000):
                        print("Transaction failed")
                        print("Amount Exceeds Limit")
                     elif (amunt <= 10000):
                         print("Do you want to Receipt")
                         print("yes:press 1")
                         print("NO:Press 2")
                         if receipt == 1:
                           print("Transaction Successful")
                           print("Take your receipt from R-Box")
                           print("Please take your card")
                           print(f"collect your {amunt}at terminal")
                         elif receipt == 2:
                           print("Transaction Successful")
                           print("Please take your card")

                           print(f"collect {amunt}at terminal")
              elif ovral == 2:
                    print("Enter  4-digit Act number of Receiver")
                    rsi = int(input())
                    print("Enter Amount")
                    amntsnd = int(input())
                    if (amntsnd <= 100000):
                        print(f"Amount{amntsnd} transferred successfully to {rsi}")
                    elif (amntsnd >= 100001):
                        print("Amount exceeds the limit")
                        print("Transaction Impossible")
                    else:
                          print("current balance is: ($)5M-USD")

 elif (pin != 88):
     print("Pin is Invalid")
     print("Select any option:")
     print("press 1 for: Again Entering pin")
     print("press 2 for: for forget pin")
     last = int(input())
     match last:
         case 1:
             print("Enter the pin:")
             pin = int(input())
             if pin == 88:
                print("Pin is correct")
                print('Select operations')
                print("press 1 for:current Account")
                print("Press 2 for :Savings Account")
                print("Press 3 for:Business Account")
                at = int(input())
                match at:
                  case 1:
                    print("You select:Current Account")
                    print("Select Operations")
                    print("Press 1 For:Amount With-drawl")
                    print("Press 2 For:Amount_send")
                    print("press 3 For:Balance_check")
                    ovral = int(input())
                    if ovral == 1:
                      print("How many Amount you with draw?")
                      print("For 1000:press 1")
                      print("For 500:press 2")
                      print("For custom:press 3")
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
                        print("Do you want to  receipt")
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
                            if amunt >= 12000:
                               print("Transaction failed")
                               print("Amount Exceeds Limit")
                            elif amunt <= 10000:
                               print("Do you want to receipt")
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
                    elif ovral == 2:
                        print("Enter 4 digit Act Number of Receiver")
                        rsi = int(input())
                        print("Enter Amount")
                        amntsnd = int(input())
                        if amntsnd <= 100000:
                         print(f"Amount{amntsnd} transferred successfully to {rsi}")
                        elif (amntsnd >= 100001):
                           print("Amount exceeds the limit")
                           print("Transaction Impossible")
                        else:
                           print("current balance is: ($)5M-")
                    else:
                           print("pin is in-correct")
                  case 2:
                      print("Enter your username for viewing pin")
                      name = input("Enter the name:")
                      if name == "nadia":
                        print("pin is:88")
                      else:
                        print("user name is invalid")
         case 2:
             print("Enter user-name for pin recovery:")
             name=input("Enter name:")
             if name=="nadia":
                 print("Pin is:88")
             else:
                 print("User-name is invalid")





 else:
     print("Pin is correct")



Atm_Machine()