import turtle


screen = turtle.Screen()
screen.bgcolor("white")


circle = turtle.Turtle()


circle.speed(1)


def draw_circle(turtle, radius):
    turtle.circle(radius)


draw_circle(circle, 50)


turtle.done()
