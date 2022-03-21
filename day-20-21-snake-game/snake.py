from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        x_pos = 0
        for _ in range(3):
            snake_piece = Turtle(shape="square")
            snake_piece.color("white")
            snake_piece.penup()
            self.snake.append(snake_piece)
            snake_piece.goto(x=x_pos, y=0)
            x_pos -= 20

    def move(self):
        for seg in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg - 1].xcor()
            new_y = self.snake[seg - 1].ycor()
            self.snake[seg].goto(new_x, new_y)
        self.snake[0].forward(20)

    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)

    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)

    def left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)

    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)

    def add_segment(self):
        new_seg = Turtle(shape="square")
        new_seg.penup()
        new_seg.color("white")
        x_pos = self.snake[len(self.snake) - 1].xcor()
        y_pos = self.snake[len(self.snake) - 1].ycor()
        new_seg.goto(x_pos, y_pos)
        self.snake.append(new_seg)

    def reset(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()

