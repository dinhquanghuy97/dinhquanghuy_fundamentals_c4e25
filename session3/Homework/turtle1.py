from turtle import *
shape("turtle")
speed(0)

color("red")    
for i in range(3):
    forward(100)
    left(120)

color("blue")
for j in range(4):
    forward(100)
    left(90)

color("dark red")
for k in range(5):
    forward(100)
    left(72)

color("yellow")
for l in range(6):
    forward(100)
    left(60)

color("light blue")
for m in range(7):
    forward(100)
    left(360/7)

mainloop()