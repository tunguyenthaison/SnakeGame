import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
SIZE = 20
WIDTH = 600
HEIGHT = 600
MOVE_DISTANCE = 20
TOP_PADDING = 2 * SIZE

screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(2/(10 + scoreboard.score))
    snake.move()
    screen.update()

    # Detect collision
    if snake.head.distance(food) < 20:
        # print("Nom Nom Nom!")
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 - TOP_PADDING or \
            snake.head.ycor() < -280:
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()
        screen.update()
        # game_is_on = False

    # Detect collision with tail
    for segment in snake.all_segments[1::]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()
            screen.update()

screen.exitonclick()
