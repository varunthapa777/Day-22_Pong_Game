import time
import turtle as t
from turtle import Screen
from ball import Ball
from line import Line
from paddle import Paddle
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("AQUAMARINE")
screen.title("Pong")
screen.tracer(0)

ball = Ball((0, 0))
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard = ScoreBoard()
middle_line = Line()

l_name = screen.textinput("Players Registration", prompt="Enter left player name ")
r_name = screen.textinput("Players Registration", prompt="Enter right player name ")

screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.movespeed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    # Detect collision with r_paddle and l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect collision with the wall
    # for r_paddle
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()

    # for l_paddle
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()

    if scoreboard.l_score == 3:
        scoreboard.winner(l_name.upper())
        game_is_on = False

    elif scoreboard.r_score == 3:
        scoreboard.winner(r_name.upper())
        game_is_on = False


screen.exitonclick()
