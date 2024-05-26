from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.color('black')
        self.hideturtle()
        self.goto(-290, 260)
        self.increase_level()

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f'Level: {self.level}', align='left', font=FONT)

    def game_over(self):
        self.home()
        self.write('GAME OVER', align='center', font=FONT)
