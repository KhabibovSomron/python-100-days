from turtle import Turtle, Screen, colormode
from random import randint, choice

timmy = Turtle()
timmy.shape("classic")
timmy.color("red")
colormode(255)


def draw(angle):
    degree = 360 / angle
    timmy.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    for _ in range(angle):
        timmy.right(degree)
        timmy.forward(100)


def random_walk():
    timmy.pensize(15)
    timmy.speed("fastest")
    degrees = [0, 90, 180, 270]
    for _ in range(200):
        timmy.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        timmy.setheading(choice(degrees))
        timmy.forward(30)


def draw_spirograph():
    timmy.pensize(1)
    timmy.speed("fastest")
    for _ in range(0, 360, 6):
        timmy.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        timmy.circle(100)
        timmy.left(6)


random_walk()

screen = Screen()
screen.exitonclick()
