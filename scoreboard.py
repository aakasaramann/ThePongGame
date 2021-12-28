from turtle import Turtle

PLAYER1_POSITION = (100, 225)
PLAYER2_POSITION = (-100, 225)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score1 = 0
        self.score2 = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(PLAYER1_POSITION)
        self.write(self.score1, align="center", font=("Courier", 50, "bold"))
        self.goto(PLAYER2_POSITION)
        self.write(self.score2, align="center", font=("Courier", 50, "bold"))

    def l_point(self):
        self.score2 += 1
        self.update_score()

    def r_point(self):
        self.score1 += 1
        self.update_score()

