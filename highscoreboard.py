from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Highscoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.highscore = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(0, -270)
        self.write(f"Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def update_highscore(self):
        self.clear()
        self.write(f"Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)