from turtle import *
def draw_square(l,c):
    color(c)
    for i in range(4):
        forward(l)
        left(90)
speed(0)   
draw_square(10,"red")
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
mainloop()
