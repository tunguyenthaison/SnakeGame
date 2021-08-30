import time
from turtle import Screen, Turtle
from snake import *

screen = Screen()
SIZE = 20
WIDTH = 600
HEIGHT = 600
MOVE_DISTANCE = 20
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
count = 0
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.update()
    count += 1

screen.exitonclick()
