import time
from turtle import Screen, Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SIZE = 20
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.all_segments = []
        self.create_snake()
        self.head = self.all_segments[-1]
        self.length = 3

    def create_snake(self):
        for position in STARTING_POSITIONS[::-1]:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.all_segments.append(new_segment)

    def move(self):
        """
        Move the snake according to the movement of the head
        :param snake:
        :return:
        """
        head = self.head
        pos = head.position()
        n = self.length
        for i in range(1, n):
            current_pos = self.all_segments[n - 1 - i].position()
            self.all_segments[n - 1 - i].goto(pos)
            pos = current_pos
        self.head.forward(MOVE_DISTANCE)

    def get_head(self):
        return self.head

    def set_head(self, direction):
        if direction == "left":
            self.head.left(90)
        elif direction == "right":
            self.head.right(90)
