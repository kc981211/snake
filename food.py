from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.resizemode("user")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_cor = random.randrange(-260, 260, 20)
        y_cor = random.randrange(-260, 260, 20)
        self.goto(x_cor, y_cor)



