total_work=4
original_count=total_work
print("original_count value is ", original_count)

completed_count=0
work_num=1
while completed_count<total_work:
    print("work_num value is ", work_num)
    if work_num%2==0:
        print("work_num is even")
    else:
        print("work_num is odd")
    completed_count+=1
    work_num+=1

#print numbers 1-10 using while
num=1
while num<=10:
    print(num)
    num+=1

#print even numbers 2-20 using while
even_num=2
while even_num<=20:
    print(even_num)
    even_num+=1
    if even_num%2==0:
        print("even_num is even", even_num)
    else:
        print("even_num is odd", even_num)

#calculate + of numbers 1-10 

numbers=0
while numbers<=10:
    print("numbers value is ", numbers)
    numbers+=1

#ask user for a passwork(input) , the enter python123 logg, if no passwork is incorrect

password="python123" 
input_password=input("Enter the password:")
if input_password==password:
    print("password is correct")
else:
    print("password is incorrect")
