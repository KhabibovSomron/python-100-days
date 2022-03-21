from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_data()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score {self.score}   High Score: {self.high_score}", False, align="center", font=("Arial", 14, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_data()

        self.score = 0
        self.update_scoreboard()

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", False, align="center", font=("Arial", 14, "normal"))

    def read_data(self):
        with open("data.txt") as file:
            content = int(file.read())
            return content

    def write_data(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))

