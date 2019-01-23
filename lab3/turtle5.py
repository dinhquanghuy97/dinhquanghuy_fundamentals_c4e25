from turtle import *
def draw_star(x, y, l): 
    penup()
    setpos(x,y)
    left(36)
    pendown()
    for i in range(5):
        forward(l)
        left(144)
draw_star(100,100,100)
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

mainloop()