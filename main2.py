from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from highscoreboard import Highscoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
highscoreboard = Highscoreboard()
screen.listen()


def highscore_update():
    if scoreboard.score > highscoreboard.highscore:
        highscoreboard.highscore = scoreboard.score
        highscoreboard.update_highscore()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # print(snake.head.heading())
    print(snake.head.pos())
    # print(snake.heading)

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        snake.extend()

    # detect collision with wall
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        game_on = False
        scoreboard.gameover()
        highscore_update()


    # detect collision with tail
    # if head collides with any segment of the body:
    for body in snake.bodies[1:]:
        if snake.head.distance(body) < 10:
            game_on = False
            scoreboard.gameover()
            highscore_update()

screen.exitonclick()
