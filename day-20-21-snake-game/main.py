from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Anime Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.snake[0].distance(food) < 15:
        food.refresh()
        snake.add_segment()
        scoreboard.add_score()

    # Detect collision with wall
    if snake.snake[0].xcor() > 290 or snake.snake[0].xcor() < -290 or snake.snake[0].ycor() > 290 or snake.snake[0].ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    segments = snake.snake[1:]
    for seg in segments:
        if snake.snake[0].distance(seg) < 10:
            scoreboard.reset()
            snake.reset()





screen.exitonclick()
