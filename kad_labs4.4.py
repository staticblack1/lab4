import turtle
import random


def draw_pumpkin(t, x, y, radius):
    """Draws a pumpkin (orange circle) at the given (x, y) location with a green stem."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    draw_stem(x, y+2*radius, radius//7, radius//1)
    draw_eye(t, x-radius//2, y + radius, radius//2)
    draw_eye(t, x + radius //3, y + radius , radius//2)
    draw_nose(t,x, y + radius //1.5, radius // 6, radius // 5)
    draw_mouth(t,x- radius //4, y + radius //3, 50)

def draw_stem(x, y, width, height):
    t.penup()
    t.setpos(x, y)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def draw_eye(t, x, y, size):
    """Draws one triangular eye at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    print(f"{size}")
    draw_polygon(t, 3, size)
    t.end_fill()


def draw_polygon(t, side, length):
    angle = 360 / side
    for _ in range(side):
        t.forward(length)
        t.left(angle)
        t.fillcolor("black")
    t.end_fill()

def draw_mouth(t, x, y, width):
    """Draws a jagged mouth using a series of connected lines."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.right(60)
    for _ in range(5):  # Create a simple zigzag mouth
        t.forward(width // 5)
        t.left(120)
        t.forward(width // 5)
        t.right(120)
    t.end_fill()
    t.left(60)

def draw_nose(t,x, y, width, height):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.fillcolor("green")
        t.begin_fill()
        for _ in range(2):
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)
        t.end_fill()

def draw_star(t, x, y, size):
    """Draws a star at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)  # 144 degrees is the angle to form a star
    t.end_fill()

def draw_multiple_stars(t, num_stars, screen_width, screen_height, max_size,pumpkin_y):
    """Draws multiple stars at random positions with random sizes."""
    for _ in range(num_stars):
        x = random.randint(-screen_width // 2, screen_width // 2)  # Random x position
        y = random.randint(pumpkin_y + screen_height // 4, screen_height // 2)  # Only above pumpkin
        size = random.randint(10, max_size)  # Random size for the star
        draw_star(t, x, y, size)




t = turtle.Turtle()
t.speed(5)
t.hideturtle()

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)

t.clear()
t.color("red")
t.shapesize(stretch_wid=5, stretch_len=5)
t.shape("arrow")

draw_pumpkin(t, 200,-100, 80)
draw_pumpkin(t, -200,-100, 80)
draw_star(t,10, 50, 50)
draw_multiple_stars(t,25,500,500,50,50)









turtle.exitonclick()