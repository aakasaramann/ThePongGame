from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("The Pong Game")


r_paddle = Paddle(1)
l_paddle = Paddle(2)

ball = Ball()

scoreboard = Scoreboard()
speed = 0

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

change_direction = 0
screen_is_on = True
while screen_is_on:
    screen.update()
    ball.move(change_direction)
    time.sleep(ball.move_speed)

    # Detect collision with wall and bounce
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.wall_bounce()

    # Detect collision with paddle
    if (ball.xcor() > 320 or ball.xcor() < -320) and (ball.distance(l_paddle) < 50 or ball.distance(r_paddle) < 50):
        ball.paddle_bounce()

    # Detect if r_paddle missed the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect if l_paddle missed the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
