#phoneNumber=256782058447
pin=88888
amount=2000000
charge=1000
def transaction():
  verifyPinCode=int(input("please enter your pin:"))
  if verifyPinCode == pin:
    answer=int(input("would you like to \"Send Money?\" Enter 1\nWould you like to \"Withdraw Money?\" Enter 2\nWould you like to \"View your Balance?\" Enter 3\nPlease enter your selection here:"))
    if answer == 1:
      numberToSendMoney=input("Please enter the phone number you are sending money:")
      amountToSend=int(input("Enter amount to send:"))
      if (amountToSend + charge) <= amount:
        balance= amount-(amountToSend + charge)
        reason=input("Please enter the reason for sending the money:")
        print("You are going to send UGX{0} at a charge of UGX{1}".format(amountToSend,charge))
        verifyPin=int(input("please enter your pin if you would like to continue with this transaction:"))
        if verifyPin == pin:
          print("you have sent UGX", amountToSend, "to", numberToSendMoney, "at a charge of UGX", charge, "and your balance is UGX",balance)
        else:
          print("Incorrect pin")
      else:
        print("You have insufficient funds to complete this transaction")
    elif answer == 2:
      amountToWithdraw=int(input("enter how much you would like to withdraw:"))
      
      
      if  (charge + amountToWithdraw) <= amount:
        
        balanceAfterWithdraw= amount-(charge + amountToWithdraw)
        print("You have withdrawn UGX",amountToWithdraw, "at a fee of UGX", charge,"and your balance is UGX",balanceAfterWithdraw)
      else:
        print("You have insufficient funds to complete this transaction")
    elif answer == 3:
      print("Your account balance is UGX",amount)
    else:
      print("Invalid option, the option entered doesn't exist")
  else:
    print("The pin entered is invalid")
transaction()
