from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("lightblue")
        self.penup()
        self.shape("circle")
        self.shapesize(1)
        self.x = 5
        self.y = 3

    def reset_ball(self):
        self.goto(0, 0)

    def move(self):
        self.goto(self.xcor() + self.x, self.ycor() + self.y)

    def hit_x(self):
        if self.ycor() > 380 or self.ycor() < -380:
            self.y *= -1

    def hit_y(self, pl_x, pl_y):
        if abs(self.xcor() - pl_x) < 20 and abs(self.ycor() - pl_y) < 50:
            self.x *= -1