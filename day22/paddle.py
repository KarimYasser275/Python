from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color("white")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_len= 3.5, stretch_wid= 1)
        self.position = position
        self.goto(self.position, 0)
        self.score = 0

    def move_up(self):
        if self.ycor() < 260:
            self.setheading(90)
            self.forward(30)

    def move_down(self):
        if self.ycor() > -260:
            self.setheading(270)
            self.forward(30)