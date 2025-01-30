from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


s = Screen()
s.setup(600, 600)
s.tracer(0)
s.bgcolor('black')
s.title('My Snake Game')


snake = Snake()
food = Food()
scoreboard = Scoreboard()

s.listen()
s.onkey(snake.up, 'w')
s.onkey(snake.down, 's')
s.onkey(snake.left, 'a')
s.onkey(snake.right, 'd')

game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.check_collision_with_wall():
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[3:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

s.exitonclick()
