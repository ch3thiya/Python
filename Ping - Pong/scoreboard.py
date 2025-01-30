from turtle import Turtle

alignment = 'center'
font = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"{self.left_score}  {self.right_score}", align=alignment, font=font)

    def increase_left_score(self):
        self.left_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_right_score(self):
        self.right_score += 1
        self.clear()
        self.update_scoreboard()
