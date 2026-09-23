V=4
W=5
X=8
Y=2
Z=0

Z=(V+W)*X/Y
print("Value of operator precidence", Z)

name="Murilo"
age=0

if name=="Murilo" and age>=10 or name=="Elix" and age>=0:
    print("You are allowed to enter")
else:
    print("Goodbye")


print("Enter a number(Numerator)")
numerator=int(input())
print("Enter a number(Denominator)")
denominator=int(input())

if numerator%denominator==0:
    print("The number is divisible")
else:
    print("The number is not divisible")