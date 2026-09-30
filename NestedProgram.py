print("Pick your vehicle") 
print("1. Car") 
print("2. Bike") 


choice= int(input("Enter your choice (1, 2) : "))

if choice == 1:
    print("You have chosen Car")
elif choice == 2:
    print("You have chosen Bike")

hungry = input("Are you hungry? (yes/no): ")
if hungry == "yes":
    burguer = input("Which burguer do you want? (cheese, chicken, veggie): ")
    if burguer == "cheese":
        extra_cheese = input("Do you want extra cheese? (yes/no): ")
        if extra_cheese == "yes":
            print("You have chosen a cheese burger with extra cheese.")
        else:
            print("You have chosen a cheese burger without extra cheese.")
    elif burguer == "chicken":
        print("You have chosen a chicken burger.")
    elif burguer == "veggie":
        print("You have chosen a veggie burger.")
    else:
        print("Invalid choice.")
else:
    print("You are not hungry.")     

user_input = input("Did you finish your homework? (yes/no): ")       
if user_input =="yes":
    holiday = input("Is tomorrow a holiday? (yes/no): ")
    if holiday =="yes":
        print("Yay! Is time to sleep🍕") 
    else:
        print("Ok, time to study🍔 ")  
elif user_input =="no":
    checking = input("Is the teacher checking the homework tomorrow? (yes/no): ")
    if checking =="yes":
        print("Do the homework now!")
    else:
        print("You can do the homework later.")
else:
    print("Print yes or no please")


checkplay = input("Do you want to play a game? (yes/no): ")
if checkplay == "yes":
    gamechoice = input("Which game do you want to play? (Futbol or kriket):")
    if gamechoice == "Futbol":
        print(" You have chosen to play Futbol")
    elif gamechoice == "kriket":
        print("You have chosen to play kriket")
    else: 
        print("Please say Futbol or kriket")
else:
    print("Ok, So go back to homework")



    
    