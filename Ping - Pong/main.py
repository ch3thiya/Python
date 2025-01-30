from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

s = Screen()
t = Turtle()
s.setup(width=800, height=600)
s.bgcolor('black')
s.title('Pong')
s.tracer(0)

t.color('white')
t.penup()
t.goto(0, -300)
t.pendown()
t.hideturtle()
t.left(90)
for _ in range(30):
    t.forward(20)
    t.penup()
    t.forward(20)
    t.pendown()


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

s.listen()
s.onkey(r_paddle.go_up, "Up")
s.onkey(r_paddle.go_down, "Down")
s.onkey(l_paddle.go_up, "w")
s.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()
    if ball.ycor() > 255 or ball.ycor() < -275:
        ball.bounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.paddle_hit()
    if ball.xcor() > 390:
        scoreboard.increase_left_score()
        r_paddle.goto(350, 0)
        l_paddle.goto(-350, 0)
        ball.restart()
    if ball.xcor() < -390:
        scoreboard.increase_right_score()
        r_paddle.goto(350, 0)
        l_paddle.goto(-350, 0)
        ball.restart()

s.exitonclick()
