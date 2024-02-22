import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.move, 'w')

loop_count = 1
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.move_cars()
    loop_count += 1

    if player.ycor() >= FINISH_LINE_Y:
        player.return_to_start()
        score.increase_score()
        car_manager.increase_level()

    if loop_count == 6:
        car_manager.create_car()
        loop_count = 1

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

screen.exitonclick()
