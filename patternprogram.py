print("Half Pyramid Pattern of Stars")
n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(i + 1):
        print("*", end="")
    print()

print("Numbers Pyramid Pattern")
n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(i + 1):
        print(j + 1, end=" ")
    print()

print("Square Pattern of Stars")
n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()



