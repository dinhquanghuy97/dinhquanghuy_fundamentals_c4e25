sheep = [5,7,300,90,24,50,75]
print("Hello, my name is Huy and these are my flock\n",sheep)
print("Now my biggest sheep has size",max(sheep),"let's shear it")
sheep[sheep.index(max(sheep))] = 8
print("After shearing, here is my flock\n",sheep)
for i in range (len(sheep)):
    sheep[i] += 50
print("One month has passed, now here is my flock\n",sheep)