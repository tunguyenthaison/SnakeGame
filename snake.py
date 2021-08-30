import time
from turtle import Screen, Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SIZE = 20
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.all_segments = []
        self.create_snake()
        # self.head = self.all_segments[-1]
        self.head = self.all_segments[0]
        self.length = 3

    def create_snake(self):
        # for position in STARTING_POSITIONS[::-1]:
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.all_segments.append(new_segment)

    def move(self):
        head = self.head
        n = self.length
        for i in range(n-1, 0, -1):
            current_pos = self.all_segments[i - 1].position()
            self.all_segments[i].goto(current_pos)
        self.head.forward(MOVE_DISTANCE)

    def get_head(self):
        return self.head

    def set_head(self, direction):
        if direction == "left":
            self.head.left(90)
        elif direction == "right":
            self.head.right(90)

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
            self.head.setheading(RIGHT)


