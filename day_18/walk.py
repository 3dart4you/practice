import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.pensize(7)
turtle.colormode(255)

def right():
    tim.right(90)
    tim.forward(20)

def left():
    tim.left(90)
    tim.forward(20)

def forward():
    tim.forward(20)

t_angle = [right, left, forward]


for _ in range(100):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.pencolor(r, g, b)
    random.choice(t_angle)()







screen = Screen()
screen.exitonclick()