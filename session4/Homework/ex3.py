loop = True
while loop:
    print("Answer the following algebra question:")
    print("If x = 8, then what is the value of 4(x + 3)?")
    ans = [35,36,40,44]
    for index, num in enumerate(ans):
        print(index+1,num,sep=". ")
    a = input("Your choice: ")   
    if a == "3":
        print("Bingo")
        loop = False
    else:
        print(":(")
        loop = True