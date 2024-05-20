from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.score_right = 0
        self.score_left = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_left, align="center", font= ("Ariel", 80, "normal"))
        self.goto(100, 200)
        self.write(self.score_right, align="center", font=("Ariel", 80, "normal"))


    def add_score_right(self):
        self.score_right += 1
        self.write_score()

    def add_score_left(self):
        self.score_left += 1
        self.write_score()