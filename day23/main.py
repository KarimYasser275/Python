import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player1 = Player()
car = CarManager()

screen.listen()
screen.onkeypress(fun=player1.move_up, key="Up")
screen.onkeypress(fun=player1.move_right, key="Right")
screen.onkeypress(fun=player1.move_left, key="Left")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move_cars()
    print(car.cars)
    if player1.ycor() >= 295:
        player1.reset_player()
        car.increase_difficulty()
        car.generate_cars()
