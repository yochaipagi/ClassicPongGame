import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.screensize(canvwidth=800, canvheight=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
right_paddle = Paddle(310, 0)
left_paddle = Paddle(-310, 0)
ball = Ball()
score = Score()
screen.listen()

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


def exit_game():
    global game_is_on
    game_is_on = False


screen.onkey(exit_game, "Escape")

game_is_on = True
while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.xcor() > 290 and ball.distance(right_paddle) < 60) or (
            ball.xcor() < -290 and ball.distance(left_paddle) < 60):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_pos()
        score.add_score_left()

    if ball.xcor() < -380:
        ball.reset_pos()
        score.add_score_right()

screen.bye()
