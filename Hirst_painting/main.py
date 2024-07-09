# ##my try
# import colorgram
#
# color_extract = []
# colors = colorgram.extract("hirstpaint.jpeg", 30)
#
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_extract.append(new_color)
#
# print(color_extract)

import turtle
from turtle import Turtle
from turtle import Screen
import random


def teleport(x, y):
    tim.penup()
    tim.setpos(x, y)
    tim.pendown()


tim = Turtle()
tim.shape('turtle')
tim.speed(0)
screen = Screen()

color = [(239, 229, 212), (63, 28, 7), (87, 95, 112), (243, 217, 234), (166, 83, 30), (219, 159, 82), (211, 224, 233), (140, 156, 180), (88, 108, 96), (211, 161, 13), (225, 236, 230), (236, 217, 81), (206, 6, 24), (18, 20, 53), (142, 160, 151), (22, 38, 27), (240, 65, 43), (79, 107, 202), (33, 45, 132), (182, 15, 6), (225, 51, 80), (216, 217, 8), (209, 138, 168), (51, 32, 37), (175, 47, 64), (235, 167, 203), (102, 78, 10), (113, 136, 122), (45, 75, 59), (235, 171, 161)]
# switch = True
# lines = 0
# x = 0
# y = -250
# z = -200
#
#
# def moving():
#     screen.colormode(255)
#     tim.pencolor(random.choice(color))
#     tim.dot(20)
#     tim.forward(10)
#     tim.up()
#     tim.forward(10)
#     tim.down()

#
# while switch is True:
#     teleport(y, z)
#     moving()
#     moving()
#     moving()
#     moving()
#     moving()
#     moving()
#     moving()
#     moving()
#     lines += 1
#     if lines > 1:
#         z += 50
#         moving()
#         moving()
#     if z > 250:
#         switch = False


##Angela option

screen.colormode(255)
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots +1):
    tim.dot(20, random.choice(color))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

















tim.shape("turtle")
turtle.exitonclick()