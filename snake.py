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
        self.head = self.all_segments[0]
        self.length = len(self.all_segments)

    def create_snake(self):
        # for position in STARTING_POSITIONS[::-1]:
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        # new_segment.speed(3)
        new_segment.color("black")
        new_segment.goto(position)
        new_segment.turtlesize(outline=1)
        new_segment.fillcolor("#D4C783")
        self.all_segments.append(new_segment)

    def extend(self):
        self.add_segment(self.all_segments[-1].position())

    def move(self):
        head = self.head
        n = len(self.all_segments)
        for i in range(n - 1, 0, -1):
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

    def reset(self):
        for seg in self.all_segments:
            seg.hideturtle()
        self.all_segments.clear()
        self.create_snake()
        self.head = self.all_segments[0]
        self.length = len(self.all_segments)
