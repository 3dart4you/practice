from turtle import Turtle

class Score(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(x, y)
        self.color("white")
        self.penup()
        self.refresh()

    def refresh(self):
        self.write(f'{self.score}', align='center', font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.refresh()