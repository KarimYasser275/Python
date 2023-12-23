from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

# initialize screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
# initialize snake
snake = Snake()
food = Food()
screen.listen()
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)

game_over = False
score = Scoreboard()
while not game_over:
    # screen.

    time.sleep(0.1)
    snake.move()
    screen.update()
    game_over = snake.collision()

    if snake.head.distance(food) < 15:
        print(len(snake.segments))
        snake.grow()
        food.create_new()
        score.update_score()
score.game_over()
screen.exitonclick()
