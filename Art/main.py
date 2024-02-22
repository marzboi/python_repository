import colorgram
import turtle as t
from color import color_list
import random

extracted_colors = colorgram.extract('image.jpg', 30)
colors = []
for color in extracted_colors:
    r = color.rgb[0]
    g = color.rgb[1]
    b = color.rgb[2]
    colors.append((r, g, b))

# 20 ---50--- 20
# 10X10 circles

colors = color_list

t.colormode(255)
nav = t.Turtle()
screen = t.Screen()
x = -350
y = -350
nav.penup()
nav.setx(x)
nav.sety(y)
nav.pendown()
nav.hideturtle()


for _ in range(10):
    for _ in range(10):
        nav.dot(20, random.choice(colors))
        nav.penup()
        nav.forward(50)
    nav.setx(x)
    y += 50
    nav.sety(y)
    nav.pendown()

screen.exitonclick()
