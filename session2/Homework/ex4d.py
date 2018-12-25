n = int(input("enter a number: "))
for i in range(n):
    if i % 2 == 0:
        print("x", end=" ")
    else:
        print("*", end=" ")