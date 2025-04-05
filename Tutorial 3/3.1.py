import turtle

star = turtle.Turtle()

star.speed(1)

def draw_star(turtle, size):
    angle = 144
    for _ in range(5):
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.right(72 - angle)
  
draw_star(star, 100)

turtle.done()
