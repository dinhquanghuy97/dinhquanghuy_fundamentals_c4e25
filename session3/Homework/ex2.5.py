sheep = [5,7,300,90,24,50,75]
print("Hello, my name is Huy and these are my flock\n",sheep)
print("Now my biggest sheep has size",max(sheep),"let's shear it")
sheep[sheep.index(max(sheep))] = 8
print("After shearing, here is my flock\n",sheep)
m = int(input("Enter number of month: "))
for j in range(m):
    for i in range (len(sheep)):
        sheep[i] += 50
    print("Month",j+1)
    print("Now here is my flock\n",sheep)
    sheep[sheep.index(max(sheep))] = 8
    print("After shearing, here is my flock\n",sheep)
print("My flock has size total: ",sum(sheep))
money = sum(sheep)*2
print("I would get: ",money,"$")