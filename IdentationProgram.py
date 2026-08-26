age=2 

if age>=18:
    print("You can vote")

homework_done=True

if homework_done:
    print("You can go out and play")
else:
    print("Go and study")

money=50
if money>=30:
    print("You can buy a toy")
else:
    print("You cannot buy a toy")

marks=75
if marks>=75:
    print("You have a good grade")
else:
    print("You need to study more")

color="green"
if color=="green":
    print("Yes, good catch")
else:
    print("No, try again")

name="Murilo"
if name=="Murilo":
    print("Hey Murilo")
else:
    print("Try again")

name=input("Enter your name: ")
if name=="Murilo":
    print("Hey Murilo")
else:
    print("Try again")

temperatura=int(input("Enter today's temperature in celsius: "))

if temperatura <20: 
    outfit="jacket"
    print("It's cold today")
    print("Wear a", outfit)
else:
    outfit="t-shirt"
    print("It's warm today")

    print("Wear a", outfit)


has_pudles=input("Are there puddles on the ground? (yes/no): ")

if has_pudles=="yes":
    shoes="boots"
    print("The ground is wet")
    print("Wear", shoes)
else:
    shoes="sneakers"
    print("The ground is dry")
    print("Wear a ", shoes)