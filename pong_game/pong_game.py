from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
scoreboard=Scoreboard()
paddle=Turtle()
screen=Screen()
ball=Ball()
turtle=Turtle()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
rightpaddle=Paddle((370,0))
leftpaddle=Paddle((-370,0))
screen.listen()
screen.onkey(rightpaddle.up,"Up")
screen.onkey(rightpaddle.down,"Down")
screen.onkey(leftpaddle.up,"w")
screen.onkey(leftpaddle.down,"s")
continue_game=True
while continue_game:
    time.sleep(ball.moveon)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-270:
        ball.bounce_y()
    if (ball.distance(rightpaddle)<50 and ball.xcor()>340) or (ball.distance(leftpaddle)<50 and ball.xcor()<-340):
        ball.bounce_x()
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.left_point()
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.right_point()
    if scoreboard.left_score==9:
        turtle.color("green")
        turtle.penup()
        turtle.goto(-110,0)
        turtle.write("Left is winner!",font=("Arial",30,"normal"))
        continue_game=False
    if scoreboard.right_score==9:
        turtle.color("green")
        turtle.penup()
        turtle.goto(-110,0)
        turtle.write("Right is winner!",font=("Arial",30,"normal"))
        continue_game=False
screen.exitonclick()
