import time
import turtle
from turtle import Screen, Turtle

screen = Screen()
SIZE = 20
WIDTH = 600
HEIGHT = 600
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")

# TODO 0. Turn off animation using tracer
screen.tracer(0)

# TODO 1. Create a snake body.
all_segments = [] # save the snake with all_segments[0] = head of the snake
starting_position = [(0, 0), (-20, 0), (-40, 0)]
colors = ["red", "blue", "white"]
i = 2
for position in starting_position[::-1]:
    new_segment = Turtle(shape="square")
    new_segment.penup()
    new_segment.color(colors[i])
    new_segment.goto(position)
    all_segments.append(new_segment)
    i -= 1


# TODO 2. Move the snake forward
def move(snake):
    """
    Move the snake according to the movement of the head
    :param snake:
    :return:
    """
    head = snake[-1]
    pos = head.position()
    n = len(snake)
    for i in range(1, n):
        current_pos = snake[n-1-i].position()
        snake[n-1-i].goto(pos)
        pos = current_pos
    head.forward(SIZE)



def turn_left(snake):
    """
    make a left turn for the snake, no moving forward
    :param snake: all_segments
    :return: new position of the snake
    """
    move(snake[0:-1])
    head = all_segments[-1]
    head.left(90)
    head.forward(SIZE)
    screen.update()

# for _ in range(4):
#     move(all_segments)
#     screen.update()
#     time.sleep(0.1)

# range(start = 2, stop = 0, step = -1)

game_is_on = True
count = 0
while game_is_on:
    screen.update()
    move(all_segments)
    count += 1
    if count % 10 == 0:
        # turn_left(all_segments)
        all_segments[-1].left(90)
        count += 1
    time.sleep(0.2)
    if count == 40: # 10mloops
        game_is_on = False






# segment_1 = Turtle(shape="square")
# segment_1.color("white")
#
#
# segment_2 = Turtle(shape="square")
# segment_2.color("white")
# segment_2.setx(head.xcor() - 20)
#
#
# segment_3 = Turtle(shape="square")
# segment_3.color("white")
# segment_3.setx(segment_2.xcor() - 20)


screen.exitonclick()
