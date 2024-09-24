import turtle

def draw_square(t, length):
    """Draws a square with the given side length."""
    for _ in range(4):
        t.forward(length)
        t.left(90)

def draw_circle(t, radius):
    """Draws a circle with the given radius."""
    t.circle(radius)

def draw_polygon(t, sides, length):
    """Draws a regular polygon with a given number of sides and side length."""
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)

t = turtle.Turtle()
t.speed(1)
#  t.hideturtle()

screen = turtle.Screen()
screen.bgcolor("darkblue")
screen.setup(width=600, height=600)

t.clear()
t.color("red")
t.shapesize(stretch_wid=5, stretch_len=5)
t.shape("arrow")

# Draw a square with a side length of 100

draw_square(t, 100)


draw_circle(t, 50)

draw_polygon(t, 6, 50)  # Hexagon
# Close the window when clicked

turtle.exitonclick()
