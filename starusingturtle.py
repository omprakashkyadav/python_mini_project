import turtle

star = turtle.Turtle()
star.getscreen().bgcolor("#994444")

star.penup()
star.goto((-200, 100))
star.pendown()

def starturtle(turtle, size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            starturtle(turtle, size/3)
            turtle.left(216)
        turtle.end_fill()

starturtle(star, 360)

turtle.done()