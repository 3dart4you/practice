from turtle import Turtle

class Player(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape('square')
        self.shapesize(0.6, 4)
        self.right(90)
        self.goto(x, y)

    def move_up(self):
        if self.ycor() < 340:
            self.heading()
            self.setheading(90)
            self.forward(10)

    def move_down(self):
        if self.ycor() > -340:
            self.heading()
            self.setheading(270)
            self.forward(10)