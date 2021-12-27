print("You are invited to Dinton's party, Please enter a few details so that we can plan for you")
# global variable that makes the while loop true, and executes whatever is in the loop
message='yes'
# global variables to store information that we input
name=''
gender=''
age=''
contact=''
gift=''
# A list going to store all the information entered
partyDetails=[]

# A function that enables a user to enter their details for the party
def registerForParty(name,gender,age,contact,gift):
    name=input("Please enter your name:")
    gender=input("Please enter your gender:")
    age=int(input("Please enter your age:"))
    contact=int(input("Please enter your contact:"))
    gift=input("Please enter your gift:")
    # A dictionary to store all the information input by the user
    regDetailsDictionary={
        'name':name,
        'gender':gender,
        'age':age,
        'contact':contact,
        'gift':gift,
    }
    # Adding all the information entered in the dictionary and adding it to a list
    partyDetails.append(regDetailsDictionary)
# A function to display the details of the registered guests
def seePartyDetails():
    print('Here are the names of the registered guests:')
    print('---------------------------------------------------------------')
    for i in partyDetails:
        print(i['name'])
        print(i['gender'])
        print(i['age'])
        print(i['contact'])
        print(i['gift'])
        print('------------------------\n------------------------\n------------------------')
    
while (message=='yes'):
    registerForParty(name, gender, age,contact,gift)
    message=input("Would you like to register another guest,Enter yes or no:")

else:
    seePartyDetails()


