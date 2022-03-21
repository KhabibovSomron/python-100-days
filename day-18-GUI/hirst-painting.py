import colorgram
from turtle import Turtle, Screen, colormode
from random import choice
colors = colorgram.extract('hirst.jpg', 30)

rgb_colors = []
for item in colors:
    new_color = (item.rgb.r, item.rgb.g, item.rgb.b)
    rgb_colors.append(new_color)

timmy = Turtle()
colormode(255)


def draw_dots():
    for _ in range(10):
        timmy.dot(20, choice(rgb_colors))
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()


positionX = -200
positionY = -200
for _ in range(10):
    timmy.penup()
    timmy.setposition(positionX, positionY)
    timmy.pendown()
    draw_dots()
    positionY += 50

screen = Screen()
screen.exitonclick()
