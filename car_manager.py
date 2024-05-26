from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.move_distance = STARTING_MOVE_DISTANCE
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(180)
        self.create_car()

    def create_car(self):
        self.color(choice(COLORS))
        x_pos = randint(320, 920)
        y_pos = randint(-24, 24) * 10
        self.goto(x_pos, y_pos)

    def move(self):
        self.forward(self.move_distance)
        # when moved out on the left, restart from right
        if self.xcor() < -320:
            self.goto(320, self.ycor())

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
