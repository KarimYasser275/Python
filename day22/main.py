from turtle import Screen, Turtle
from paddle import Paddle
import time
from pong_ball import Ball



screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
net = Turtle()
net.hideturtle()
net.penup()
net.goto(0,300)
net.pendown()
net.pencolor("white")
net.goto(0,-300)
ball = Ball()
player1 = Paddle(-380)
player2 = Paddle(380)


screen.title("Pong")
game_over = False

screen.listen()
screen.onkeypress(fun=player1.move_up, key="w")
screen.onkeypress(fun=player1.move_down, key="s")
screen.onkeypress(fun=player2.move_up, key="Up")
screen.onkeypress(fun=player2.move_down, key="Down")
while not game_over:
    ball.move()
    screen.update()
    time.sleep(0.01)
    if not ball.in_progress:
        if (ball.distance(player1) < 30 and ball.xcor() < -365)\
                or (ball.distance(player2) < 30 and ball.xcor() > 365):
            ball.bounce()
        elif ball.ycor() < -280 or ball.ycor() > 280:
            ball.wall_bounce()
        elif ball.xcor() < -395:
            ball.generate()
            player1.score += 1
        elif ball.xcor() > 395:
            ball.generate()
            player2.score += 1


screen.exitonclick()