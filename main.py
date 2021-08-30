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

# TODO 0. Turn off animation using tracer
screen.tracer(0)

# TODO 1. Create a snake body.
snake = Snake()

# TODO 2. Move the snake forward
game_is_on = True
count = 0
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    count += 1
    if count % 10 == 0:
        snake.set_head("left")
        count += 1
    if count == 80: # 10mloops
        game_is_on = False

screen.exitonclick()
