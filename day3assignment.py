phoneNumber=256782058447
pin=88888
amount=2000000
charge=1000
def transaction():
  verifyNumber=int(input("please enter your phone number:"))
  if verifyNumber == phoneNumber:
    answer=int(input("would you like to \"Send Money?\" Enter 1\nWould you like to \"Withdraw Money?\" Enter 2\nWould you like to \"View your Balance?\" Enter 3\nPlease enter your selection here:"))
    if answer == 1:
      numberToSendMoney=input("Please enter the phone number you are sending money:")
      amountToSend=int(input("Enter amount to send:"))
      if (amountToSend + charge) <= amount:
        balance= amount-(amountToSend + charge)
        reason=input("Please enter the reason for sending the money:")
        verifyPin=int(input("please enter your pin:"))
        if verifyPin == pin:
          print("you have sent UGX", amountToSend, "to", numberToSendMoney, "at a charge of UGX", charge, "and your balance is UGX",balance)
        else:
          print("Incorrect pin")
      else:
        print("You have insufficient funds to complete this transaction")
    elif answer == 2:
      amountToWithdraw=int(input("enter how much you would like to withdraw:"))
      balanceAfterWithdraw=amount-(charge + amountToWithdraw)
      if  (charge + amountToWithdraw) <= amount:
        print("You have withdrawn UGX",amountToWithdraw, "at a fee of UGX", charge,"and your balance is UGX",balanceAfterWithdraw)
      else:
        print("You have insufficient funds to complete this transaction")
    elif answer == 3:
      print("Your account balance is UGX",amount)
    else:
      print("Invalid option, the option entered doesn't exist")
  else:
    print("The phone number entered is invalid")
transaction()
