import turtle as t

import random

t.colormode(255)

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")
tim.speed(0)
directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()


# for i in range(10000):
#     tim.forward(20)
#     tim.setheading(random.choice(directions))
#     tim.color(random_color())


# total_angle = 360
# starting_side = 3
# angle = total_angle / starting_side

# while angle <= total_angle:
#     for _ in range(starting_side):
#         tim.forward(30)
#         tim.right(angle)
#     starting_side += 1
#     angle = total_angle / starting_side
