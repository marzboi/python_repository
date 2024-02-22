from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def create_car(self):
        car = Turtle()
        car.penup()
        car.color(random.choice(COLORS))
        car.shape('square')
        car.shapesize(1, 2)
        car.goto(310, random.randint(-250, 250))
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            new_x = car.xcor() - self.speed
            car.goto(new_x, car.ycor())

    def increase_level(self):
        self.speed += MOVE_INCREMENT

    def increase_level(self):
        self.speed += MOVE_INCREMENT
