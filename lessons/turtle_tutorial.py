"""Practicing with turtle, so silly and goofy!"""

from turtle import Turtle, colormode, done
colormode(255)


leo: Turtle = Turtle()
leo.speed(50)
leo.hideturtle()
leo.penup()
leo.goto(-250,-200)
leo.pendown()
leo.color(247, 125, 209)

leo.begin_fill()
i: int = 0
while (i<3):
    leo.forward(500)
    leo.left(120)
    i = i + 1
leo.end_fill()


bob: Turtle = Turtle()
bob.penup()
bob.goto(-250,-200)
bob.pendown()
bob.color(164, 89, 135)

bob.begin_fill()
while (i<3):
    bob.forward(500)
    bob.left(120)
    i = i + 1
bob.end_fill



def grass_blades(t: Turtle, x: float, y: float) -> None:
    """Adds adds more complex details to grass. 7. Above and beyond breaks up complex functions (5 points total)."""
    t.penup()
    t.goto(x,y)
    t.pencolor(53, 112, 35)
    t.fillcolor(53, 112, 35)
    i: int = 0
    while i < 40:
        t.forward(500)
        t.left(120)
        i = i + 1
    t.pendown()