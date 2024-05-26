import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

NUMBER_OF_CARS = 12

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing')
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()

cars = []
for _ in range(NUMBER_OF_CARS):
    car = CarManager()
    cars.append(car)

screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in cars:
        car.move()
        # detect collision between car and player
        if car.distance(player) < 22:
            scoreboard.game_over()
            game_is_on = False

    if player.check_top_reached():
        scoreboard.increase_level()
        for car in cars:
            car.increase_speed()

screen.exitonclick()
