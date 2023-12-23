from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=280)
        self.write(arg="Score : " + str(self.score), move=False, align='center', font=('Arial', 10, 'bold'))


    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg="Score : " + str(self.score), move=False, align='center', font=('Arial', 10, 'bold'))

    def game_over(self):
        self.clear()
        self.goto(0, 50)
        self.color("blue")
        self.write(arg="Game Over, Score : " + str(self.score), move=False, align='center', font=('Arial', 20, 'bold'))

