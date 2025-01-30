from turtle import Screen, Turtle
import time

FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.level = 1
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.hideturtle()
        self.turtle.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.turtle.clear()
        self.turtle.goto(0, 260)
        self.turtle.write(f"Level {self.level}", align='center', font=("Courier", 17, "bold"))

    def game_over(self):
        self.turtle.goto(0, 0)
        self.turtle.color('red')
        self.turtle.write("GAME OVER!", align='center', font=("Courier", 20, "bold"))

    def went_to_end(self):
        self.level += 1
        self.update_scoreboard()

