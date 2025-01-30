from turtle import Turtle
import time
y_location = [(0, 0), (0, -5), (0, -10), (0, -15)]
move_distance = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in y_location:
            self.add_segment(position)

    def add_segment(self, position):
        t = Turtle('square')
        t.shapesize(1, 1)
        t.penup()
        t.color('white')
        t.goto(position)
        t.left(90)
        self.segments.append(t)

    def reset(self):
        for seg in self.segments:
            seg.goto(500, 500)
        self.segments.clear()
        self.create_snake()
        time.sleep(1)
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def check_collision_with_wall(self):
        if (self.head.xcor() > 280 or self.head.xcor() < -280 or
                self.head.ycor() > 250 or self.head.ycor() < -280):
            return True
        return False

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)
