import turtle

window = turtle.Screen()
window.title("Ping-Pong")
window.setup(width=0.5, height=0.5)
window.bgcolor("black")

border = turtle.Turtle()
border.color("green")

border.begin_fill()
border.goto(-250, 150)
border.goto(250, 150)
border.goto(250, -150)
border.goto(-250, -150)
border.goto(-250, 150)
border.end_fill()

border.goto(0, 300)

window.mainloop()