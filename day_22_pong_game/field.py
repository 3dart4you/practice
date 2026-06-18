from turtle import Turtle

class Field(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pensize(10)
        self.hideturtle()
        self.shape("circle")
        self.draw_perimetr()
        self.draw_middle_line()

    def draw_perimetr(self):
        self.goto(-390,390)
        self.clear()
        coords = [(-390, -390), (390, -390), (390, 390), (-390, 390)]
        for coord in coords:
            self.goto(coord)

    def draw_middle_line(self):
        self.goto(0,390)
        self.right(90)
        self.pensize(5)
        while self.ycor() > -370:
            self.penup()
            self.forward(12)
            self.pendown()
            self.forward(12)
