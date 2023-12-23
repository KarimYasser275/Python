from turtle import Turtle
import  random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle", )
        self.penup()
        self.color("yellow")
        self.shapesize(stretch_wid= 0.5, stretch_len= 0.5)
        self.create_new()

    def create_new(self):
        self.randomX = random.randint(-280, 280)
        self.randomY = random.randint(-280, 280)

        self.goto(x=self.randomX, y=self.randomY)

