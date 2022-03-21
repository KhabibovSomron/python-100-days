from turtle import Turtle


class Player(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.goto(x_pos, 0)
        self.left(90)
        self.shapesize(stretch_wid=1, stretch_len=5)

    def move_up(self):
        if self.ycor() < 240:
            self.forward(20)

    def move_down(self):
        if self.ycor() > -240:
            self.backward(20)




