from turtle import Screen, Turtle
from player import Player
import time
from ball import Ball
from scoreboard import ScoreBoard

center_line = Turtle()


def draw_line():
    center_line.penup()
    y_pos = -300
    center_line.goto(0, y_pos)
    center_line.color("white")
    center_line.left(90)
    center_line.pensize(8)
    while y_pos <= 300:
        center_line.pendown()
        center_line.forward(40)
        center_line.penup()
        center_line.forward(40)
        y_pos += 80


screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=600)
screen.tracer(0)
screen.title("Pong")
draw_line()
left_player = Player(-480)
right_player = Player(470)
ball = Ball()

left_score = ScoreBoard(-70)
right_score = ScoreBoard(70)


is_game_on = True
screen.listen()
screen.onkey(key="w", fun=left_player.move_up)
screen.onkey(key="s", fun=left_player.move_down)
screen.onkey(key="Up", fun=right_player.move_up)
screen.onkey(key="Down", fun=right_player.move_down)

while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision with players
    if ball.distance(right_player) < 50 and ball.xcor() > 440 or ball.distance(left_player) < 50 and ball.xcor() < -450:
        ball.bounce_player()

    # Detect if the balls goes out

    if ball.xcor() > 490:
        ball.refresh()
        left_score.inc()

    if ball.xcor() < -490:
        ball.refresh()
        right_score.inc()

screen.exitonclick()
