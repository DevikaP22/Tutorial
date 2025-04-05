import turtle

pentagon = turtle.Turtle()

pentagon.speed(1)

def draw_pentagon(turtle, size):
    angle = 72
    for _ in range(5):
        turtle.forward(size)
        turtle.right(angle)


draw_pentagon(pentagon, 100)


turtle.done()
