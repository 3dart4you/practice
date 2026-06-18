import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.pensize(2)
tim.speed(100)
turtle.colormode(255)

for _ in range(36):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.pencolor(r, g, b)
    tim.circle(100)
    tim.right(10)







screen = Screen()
screen.exitonclick()