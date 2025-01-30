import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def draw_line(turtle, start_x, start_y):
    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()
    for _ in range(35):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')
screen.title('Turtle Crossroads')

turtle = Turtle()
turtle.hideturtle()
turtle.color('white')
turtle.left(180)
draw_line(turtle, 290, 200)
draw_line(turtle, 290, -210)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.movef, 'w')
screen.onkey(player.moveb, 's')
screen.onkey(player.moveright, 'd')
screen.onkey(player.moveleft, 'a')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 210:
        player.go_to_start()
        car_manager.level_up()
        car_manager.create_cars()
        scoreboard.went_to_end()

screen.exitonclick()
