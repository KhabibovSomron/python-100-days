from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x_pos, 230)
        self.write(self.score, False, "center", ("Arial", 50, "normal"))

    def inc(self):
        self.score += 1
        self.clear()
        self.write(self.score, False, "center", ("Arial", 50, "normal"))
