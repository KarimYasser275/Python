from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def collision(self):
        retval = False
        for seg in range(2, len(self.segments)-1,1):
            print(f'Head: {self.head.pos()}, current segment {seg}, position: {self.segments[seg].pos()}, '
                  f'distance between them = {self.head.distance(self.segments[seg])}')
            if self.head.distance(self.segments[seg]) <= 25:
                retval = True
                break
        return retval
    def move(self):
        if self.head.xcor() >= 300:
            self.head.setx(-300)

        elif self.head.ycor() >= 300:
            self.head.sety(-300)

        elif self.head.xcor() <= -300:
            self.head.setx(300)

        elif self.head.ycor() <= -300:
            self.head.sety(300)

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def grow(self):
        if self.tail.heading() == LEFT:
            new_segment = Turtle("square")
            new_segment.hideturtle()
            new_segment.setx(self.tail.xcor() + 20)
            new_segment.sety(self.tail.ycor())
            new_segment.color("white")
            new_segment.penup()
            new_segment.showturtle()
            self.segments.append(new_segment)

        elif self.tail.heading() == RIGHT:
            new_segment = Turtle("square")
            new_segment.hideturtle()
            new_segment.penup()
            new_segment.setx(self.tail.xcor() - 20)
            new_segment.sety(self.tail.ycor())
            new_segment.color("white")
            new_segment.showturtle()
            self.segments.append(new_segment)

        elif self.tail.heading() == UP:
            new_segment = Turtle("square")
            new_segment.hideturtle()
            new_segment.penup()
            new_segment.setx(self.tail.xcor())
            new_segment.sety(self.tail.ycor() - 20)
            new_segment.color("white")
            new_segment.showturtle()
            self.segments.append(new_segment)

        elif self.tail.heading() == DOWN:
            new_segment = Turtle("square")
            new_segment.hideturtle()
            new_segment.color("white")
            new_segment.penup()
            new_segment.setx(self.tail.xcor())
            new_segment.sety(self.tail.ycor() + 20)
            new_segment.showturtle()
            self.segments.append(new_segment)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
