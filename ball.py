from turtle import Turtle

STARTING_POSITION = (0, 0)
DEFAULT_X_MOVE = 10
DEFAULT_Y_MOVE = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(STARTING_POSITION)
        self.x_move = DEFAULT_X_MOVE
        self.y_move = DEFAULT_Y_MOVE
        self.move_speed = 0.1

    def move(self, change_direction=0):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.75

    def reset_position(self):
        self.goto(STARTING_POSITION)
        self.paddle_bounce()
        self.move_speed = 0.1


