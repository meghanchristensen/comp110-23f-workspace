"""Making a golf scene using silly goofy turtle!"""

__author__ = "730659220"

from turtle import Turtle, colormode, done, Screen
import random
colormode(255)


def draw_golfball(ball: Turtle, x: float, y: float, width: float) -> None:
    """Draws the golf ball in the scene."""
    """8. try something fun, uses lines to create imperfect circle because on a golf ball there are individual ridges and flat sides to assist the ball in making contact with club face."""    
    ball.hideturtle()
    ball.penup()
    ball.goto(x, y)
    ball.setheading(0.0)
    ball.pendown()
    ball.color(255, 255, 255)
    
    ball.begin_fill()
    i: int = 0
    while (i < 37):
        ball.forward(width)
        ball.right(10)
        i = i + 1
    ball.end_fill()


def draw_grass(t: Turtle, x: float, y: float) -> None:
    """Fills in the base part of grass on image as well as the bright carolina blue sky."""
    screen = Screen()
    screen.bgcolor(130, 201, 244)
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.pencolor(53, 112, 35)
    t.fillcolor(53, 112, 35)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.forward(1000)
        t.right(90)
    t.end_fill()


def draw_tee(t: Turtle, x: float, y: float) -> None:
    """Builds first part of the golf tee, 7. Above and beyond breaks up complex functions (5 points total). Also 8. trying something fun, using random int to choose a color of golf tee!"""
    t.penup()
    t.hideturtle()
    t.goto(x, y)
    t.pendown()
    tee_color = random.randint(0, 2)
    if tee_color == 0:
        t.pencolor(249, 156, 249)
        t.fillcolor(249, 156, 249)
    elif tee_color == 1:
        t.pencolor(249, 156, 156)
        t.fillcolor(249, 156, 156)
    else:
        t.pencolor("red")
        t.fillcolor("red")
    t.begin_fill()
    for i in range(3):
        t.forward(50)
        t.right(120)
    t.end_fill()
    draw_tee_base(t, -3, -5)


def draw_tee_base(t: Turtle, x: float, y: float) -> None:
    """Draws base of golf tee, had to be split into two functions to disperse complexity."""
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(100)
    t.end_fill()


def main() -> None:
    """The entrypoint of my scence."""
    ball: Turtle = Turtle()
    ball.speed(0)
    draw_golfball(ball, 0, 140, 10)

    grass: Turtle = Turtle()
    grass.speed(0)
    draw_grass(grass, -500, -100)
    tee: Turtle = Turtle()
    draw_tee(tee, -20, 25)
    done()


if __name__ == "__main__":
    main() 