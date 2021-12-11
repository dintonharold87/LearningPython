def withDrawingMoney():
    name="Dinton Harold Ainemukama"
    pin=1997
    balance=2000000
    nameEntered =input("Please enter your name:")
    if nameEntered == name:
        pinEntered=int(input("Please enter your pin:"))
        if pinEntered == pin:
            print("your account balance is ",balance,"UGX")
            amountToWithdraw=int(input("How much would you like to withdraw:"))
            if amountToWithdraw > balance:
                print("You have insufficient funds to complete the transaction")
            else:
                print("Transaction successful")
                remainingBalance= balance - amountToWithdraw
                print("Your account balance is now ",remainingBalance,"UGX")
                balance = remainingBalance
        else:
            print("Incorrect pin,Please try again")
    else:
        print("please enter a correct user name")
withDrawingMoney()