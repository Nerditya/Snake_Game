from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.write(f"Score: {self.score}",  align="center", font=('Arial', 20, 'normal'))

    def increasescore(self):
        self.score += 1

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Arial', 20, 'normal'))
