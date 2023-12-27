from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_POSITIONS = [-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250]


class CarManager:
    def __init__(self):
        self.no_of_cars = 10
        self.cars = []
        self.generate_cars()
        self.difficulty = STARTING_MOVE_DISTANCE

    def generate_cars(self):
        for i in range(self.no_of_cars):
            self.create_car(random.randint(-250, 250), random.choice(Y_POSITIONS))

    def create_car(self, x, y):
        new_car = Turtle("square")
        new_car.setheading(270)
        new_car.color(random.choice(COLORS))
        new_car.shapesize(2, 1)
        new_car.penup()
        new_car.goto(x, y)
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            if car.xcor() > -330:
                car.setx(car.xcor() - self.difficulty)
            else:
                car.clearstamps()
                self.cars.remove(car)
                self.create_car(300, random.choice(Y_POSITIONS))

    def increase_difficulty(self):
        self.difficulty += MOVE_INCREMENT
