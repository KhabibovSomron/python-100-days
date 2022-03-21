from turtle import Turtle

FONT = ("Courier", 14, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.goto(-250, 270)
        self.write(f"Level: {self.level}", False, "center", FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, "center", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", FONT)
