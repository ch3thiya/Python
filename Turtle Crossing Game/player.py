from turtle import Turtle

STARTING_POSITION = (0, -250)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.penup()
        self.left(90)
        self.go_to_start()

    def movef(self):
        self.forward(MOVE_DISTANCE)

    def moveb(self):
        self.backward(MOVE_DISTANCE)

    def moveright(self):
        self.speed('slowest')
        self.setx(self.xcor() + 10)

    def moveleft(self):
        self.speed('slowest')
        self.setx(self.xcor() - 10)

    def go_to_start(self):
        self.goto(STARTING_POSITION)



