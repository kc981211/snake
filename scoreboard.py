from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def gameover(self):
        self.setposition(0, 0)
        self.write("Game over.", align=ALIGNMENT, font=FONT)


    def update_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()


