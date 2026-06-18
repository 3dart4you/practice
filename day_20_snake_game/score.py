from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('high_score.txt') as file:
            self.high_score = int(file.read())
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Scire: {self.high_score}", False, "center", 10)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()