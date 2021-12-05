import turtle
import math

om = turtle.Turtle()
om.color("red", "yellow")
om.speed(10)

om.begin_fill()
for i in range(2000):
    om.forward(10)
    om.forward(math.sin(i/10)*25)
    om.left(20)

om.end_fill()

turtle.done()
