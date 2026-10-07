for i in range(5):
    print("Iteration,", i)

for i in range(1, 6):
    print("iteration,", i)

#Hello how are you 10 times

for i in range(10):
    print("Hello how are you?")

n=int(input("enter the number whose sum you want to find"))

sum=0

for i in range(1,n+1):

      sum=sum+i

      print("the value of sum is ",sum)


m=int(input("enter the number whose multiplication table you want to find"))

multiplication=1
for i in range(1,m+1):
    multiplication=multiplication*i
print("the value of multiplication is ",multiplication)


name=input("please enter your own name")

name2=("")

for i in name:

  name2=i+name2


print("the orignal name is",name)

print("after reversed the name is",name2)