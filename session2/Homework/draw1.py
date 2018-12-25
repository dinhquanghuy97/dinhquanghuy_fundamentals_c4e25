from turtle import*
shape ("turtle")
color("red")
for k in range(4):
    for i in range(2):
        left(60)
        forward(100)
    left(60)
    for j in range(2):
        left(60)
        forward(100)
    right(30)
mainloop()