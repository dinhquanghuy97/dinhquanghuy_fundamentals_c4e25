shop = ["T-shirt","Sweater"]
loop = True
while loop:
    n = input("Welcome to our shop, what do you want(C,R,U,D)? if you want exit please enter X: ")
    if n == "R" or n == "r":
        print("Our item: ",shop)
        
    elif n == "c" or n == "C":
        shop.append(input("Enter new item: "))
        print("Our item: ",shop)
    
    elif n == "u" or n == "U":
        m = int(input("Update position: "))
        while m > (len(shop)-1):
            print("Wrong")
            m = int(input("Update position: "))
            loop = True
        shop[m] = input("New item: ")
        print(shop)

    elif n == "d" or n == "D":
        d = int(input("Delete position: "))
        while d > len(shop):
            print("Wrong")
            d = int(input("Delete position: "))
            loop = True
        shop.pop(d)
        print(shop)

    elif n == "x" or n == "X":
        print("Bye bye, see you again.")
        loop = False

    else:
        print("Wrong input")
        loop = True