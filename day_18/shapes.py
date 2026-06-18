from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")

color = ["red", "green", "blue", "brown", "orange", "purple"]

def random_color():
    t_color = random.choice(color)
    color.remove(t_color)
    return t_color

def shape():
    angle = 360 / shape_sides
    return angle

def move_and_turn():
    for _ in range(shape_sides):
        tim.forward(100)
        tim.right(shape())

shape_sides = 3
while len(color) > 0:
    tim.color(random_color())
    shape()
    move_and_turn()
    shape_sides += 1


screen = Screen()
screen.exitonclick()