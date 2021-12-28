from turtle import Turtle

PLAYER1_POSITION = (350, 0)
PLAYER2_POSITION = (-350, 0)


class Paddle(Turtle):
    def __init__(self, player_num):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        if player_num == 1:
            self.goto(PLAYER1_POSITION)
        if player_num == 2:
            self.goto(PLAYER2_POSITION)
        self.color("white")

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



