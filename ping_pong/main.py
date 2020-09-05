import turtle

window = turtle.Screen()
window.title("Ping-Pong")
window.setup(width=0.5, height=0.5)
window.bgcolor("black")

border = turtle.Turtle()
border.speed(5)
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
for i in range(12):
    if i%2 == 0:
        border.forward(12)
    else:
        border.up()
        border.forward(12)
        border.down()

window.mainloop()