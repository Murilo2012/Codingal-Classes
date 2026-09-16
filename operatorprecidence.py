V=4 
W=5
X=8
Y=2
Z=0
A=2
Z=(V+W)*X/Y
print("Value of operator precidence", Z)



Z=A*(X+Y)*Y
print("The new value of operator precidence", Z)
#0+2*(8+2)*2
#2*10*2
#20*2
#40 <-- Answer 

name="Elix"
age=0

if name=="Elix" or name=="John" and age>=2:
    print("You are allowed to enter")
else:
    print("Goodbye")    
# name= true ,  age= false
# + and -  = + ( You are allowed to enter)



if name=="Murilo" and age>=10 or name=="Elix" and age>=0:
    print("You are allowed to enter")
else:
    print("Goodbye")    
# Murilo=True, Age=False, Elix=True, Age=True    
# + and - and + and + = +( true) ( You are allowed to enter)


