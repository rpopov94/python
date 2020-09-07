import turtle
from random import choice, randint

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

FONT = ("Arial",44)
score_a = 0
score_b = 0
s1 = turtle.Turtle(visible=False)
s1.color('white')
s1.penup()
s1.setposition(-100,200)
# s1.shape('square')
# s1.shapesize(stretch_wid=1, stretch_len=5)
s1.write(score_a, font=FONT)

s2 = turtle.Turtle(visible=False)
s2.color('white')
s2.penup()
s2.setposition(100,200)
# s1.shape('square')
# s1.shapesize(stretch_wid=1, stretch_len=5)
s2.write(score_b, font=FONT)

def move_up_a():
    y = rocket_a.ycor() + 10
    if y > 100:
        y = 100
    rocket_a.sety(y)


def move_down_a():
    y = rocket_a.ycor() - 10
    if y < -100:
        y = -100
    rocket_a.sety(y)


def move_up_b():
    y = rocket_b.ycor() + 10
    if y > 100:
        y = 100
    rocket_b.sety(y)


def move_down_b():
    y = rocket_b.ycor() - 10
    if y < -100:
        y = -100
    rocket_b.sety(y)


ball = turtle.Turtle()
ball.shape('circle')
ball.color('red')
ball.speed(0)
ball.dx = 3
ball.dy = -3
ball.penup()

window.listen()
window.onkeypress(move_up_a, 'w')
window.onkeypress(move_down_a, 's')
window.onkeypress(move_up_b, 'e')
window.onkeypress(move_down_b, 'd')

while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 140:
        ball.dy = -ball.dy
    if ball.ycor() <= -140:
        ball.dy = -ball.dy
    if ball.xcor() >= 240:
        ball.dx = -ball.dx
    if ball.xcor() <= -240:
        ball.dx = -ball.dx
    if ball.xcor() >= 240:
        score_b += 1
        ball.goto(0, 0)
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])
    if ball.xcor() <= -240:
        score_a += 1
        ball.goto(0, 0)
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])

window.mainloop()
