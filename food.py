from turtle import Turtle
import random

WIDTH = 600
HEIGHT = 600
SIZE = 20
TOP_PADDING = 2 * SIZE


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-(WIDTH / 2) + SIZE, (HEIGHT / 2) - SIZE)
        random_y = random.randint(-(WIDTH / 2) + SIZE, (HEIGHT / 2) - 2*TOP_PADDING)
        self.goto(random_x, random_y)
