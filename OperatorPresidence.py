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

murilo=90
fernando=50
eduardo=60

total=murilo+fernando+eduardo
print("The total of the three numbers is", total)

average=total/3
print("The average of the three numbers is", average)

if murilo>fernando and murilo>eduardo:
    print("Murilo has the highest score")
elif fernando>murilo and fernando>eduardo:
    print("Fernando has the highest score")
else:
    print("Eduardo has the highest score")     

#answer= Murilo has the highest score   

student1=60
student2=80
student3=70

total=student1+student2+student3
print("The total of the three students is", total)

average=total/3
print("The average of the three students is", average)

if total%3==0:
    print("The total is divisible by 3")
elif total%3==20:
    print("The total is not divisible by 3")    
else:
    print("The total is not divisible by 3")    

if student1>student2 and student1>student3:
    print("Student 1 has the highest score")
elif student2>student1 and student2>student3:
    print("Student 2 has the highest score")
else:
    print("Student 3 has the highest score")

#answer=student 2 has the highest score    

if student1<student2 and student1<student3:
    print("Student 1 has the lowest score")
elif student2<student1 and student2<student3:
    print("Student 2 has the lowest score")
else:
    print("Student 3 has the lowest score")
#answer=student 1 has the lowest score 




        