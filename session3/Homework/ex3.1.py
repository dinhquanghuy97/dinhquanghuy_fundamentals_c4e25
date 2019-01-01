print("a n m o p h c i")
a = input("Guess the answer: ")
loop = True
while loop:
    if a == "champion":
        print("Congratulation!")
        loop = False
    else:
        print("Wrong answer, please try again")
        a = input("Guess the answer: ")
