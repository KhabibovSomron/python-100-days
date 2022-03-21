from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.refresh()
        self.left(90)

    def move_up(self):
        self.forward(20)

    def refresh(self):
        self.goto(0, -280)
