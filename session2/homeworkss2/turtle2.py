from turtle import *


shape("turtle")
speed(0)

color('blue')
begin_fill()
left(60)
forward(100)
right(120)
forward(100)
right(120)
forward(100)

color('red')
begin_fill()
right(90)
for i in range(4):
    forward(100)
    right(90)


color('blue')
begin_fill()
left(18)
for i in range(4):
    forward(100)
    right(72)

color('red')
begin_fill()
right(120)
for i in range(5):
    forward(100)
    left(60)

mainloop()