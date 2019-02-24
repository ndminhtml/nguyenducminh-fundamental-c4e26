from turtle import *
def draw_square(length, colors):
    color(colors)
    begin_fill()
    for i in range(4):
        left(90)
        forward(length)
    end_fill()

draw_square(100, "red")
mainloop()

