from turtle import Turtle
import random
BALL_SPEED = 3

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.setheading(random.randint(150, 210))
        self.generate()
        self.in_progress = False
        self.ball_speed = BALL_SPEED
    def move(self):
        self.forward(self.ball_speed)

    def generate(self):
        self.goto(0, 0)
        self.ball_speed = BALL_SPEED
    def bounce(self):
        self.in_progress = True
        if 0 <= self.heading() < 90:
            temp = 90 - self.heading()
            self.setheading(90 + temp)

        elif 90 <= self.heading() < 180:
            temp = 180 - self.heading()
            self.setheading(90 - temp)

        elif 180 <= self.heading() < 270:
            temp = 270 - self.heading()
            self.setheading(270 + temp)
        else:
            temp = 360 - self.heading()
            self.setheading(270 - temp)

        self.ball_speed += 0.25
        self.in_progress = False

    def wall_bounce(self):
        self.in_progress = True
        if 0 <= self.heading() < 90:
            temp = self.heading()
            self.setheading(360 - temp)

        elif 90 <= self.heading() < 180:
            temp = self.heading()
            self.setheading(360 - temp)

        elif 180 <= self.heading() < 270:
            temp = 270 - self.heading()
            self.setheading(90 + temp)
        else:
            temp = self.heading()
            self.setheading(360 - temp)

        self.in_progress = False
