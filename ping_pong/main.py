import turtle

window = turtle.Screen()
window.title("Ping-Pong")
window.setup(width=0.5, height=0.5)
window.bgcolor("black")

border = turtle.Turtle()
border.speed(0)
border.color("green")

border.begin_fill()
border.goto(-250, 150)
border.goto(250, 150)
border.goto(250, -150)
border.goto(-250, -150)
border.goto(-250, 150)
border.end_fill()

border.goto(0, 150)
border.color('white')
border.setheading(270)
for i in range(25):
    if i % 2 == 0:
        border.forward(12)
    else:
        border.up()
        border.forward(12)
        border.down()

border.hideturtle()

rocket_a = turtle.Turtle()
rocket_a.color('white')
rocket_a.shape('square')
rocket_a.shapesize(stretch_wid=5, stretch_len=1)
rocket_a.penup()
rocket_a.goto(-230, 0)

rocket_b = turtle.Turtle()
rocket_b.color('white')
rocket_b.shape('square')
rocket_b.shapesize(stretch_wid=5, stretch_len=1)
rocket_b.penup()
rocket_b.goto(230, 0)


def move_up_a():
    y = rocket_a.ycor()
    rocket_a.sety(y + 5)


def move_down_a():
    y = rocket_a.ycor()
    rocket_a.sety(y - 5)

def move_up_b():
    y = rocket_b.ycor()
    rocket_b.sety(y + 5)


def move_down_b():
    y = rocket_b.ycor()
    rocket_b.sety(y - 5)

window.listen()
window.onkeypress(move_up_a, 'w')
window.onkeypress(move_down_a, 's')
window.onkeypress(move_up_b, 'e')
window.onkeypress(move_down_b, 'd')



window.mainloop()
