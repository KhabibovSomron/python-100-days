from turtle import Screen
from player import Player
import time
from car import Car
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = Car()
scoreboard = ScoreBoard()

is_game_on = True
screen.listen()
screen.onkey(key="Up", fun=player.move_up)

while is_game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            is_game_on = False
            scoreboard.game_over()

    # Detect crossing
    if player.ycor() > 270:
        player.refresh()
        car_manager.car_speed_up()
        scoreboard.level_up()


screen.exitonclick()
