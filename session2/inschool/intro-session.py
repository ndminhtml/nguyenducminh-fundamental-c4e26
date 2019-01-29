from turtle import *
a = 5
shape("turtle")
speed(1)

for i in range(20):
    a=a+10
    forward(a)
    left(90)
    forward(a)
    left(90)


mainloop()