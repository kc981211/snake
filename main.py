from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)


bodies = []
x_axis = 0
y_axis = 0

for _ in range(0,3):
    new_body = Turtle(shape="square")
    new_body.penup()
    new_body.color("white")
    new_body.goto(x_axis, y_axis)
    x_axis -= 20
    bodies.append(new_body)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.5)

    # Moving the snake from the last body segment(the tail). The last segment will move to the coordinates of
    # the previous segment to create the movement. Then the first segment(the head) will move forward.
    # e.g. 3-->2, 2-->1, 1-->forward(20), then loop

    # range(start, end[*not inclusive], step)
    for i in range(len(bodies)-1, 0, -1):
        bodies[i].goto(bodies[i-1].position())

    bodies[0].forward(20)








screen.exitonclick()