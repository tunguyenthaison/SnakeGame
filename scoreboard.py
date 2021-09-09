from turtle import Turtle
from typing import TextIO

WIDTH = 600
HEIGHT = 600
SIZE = 20
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")
TOP_PADDING = 2 * SIZE


def line():
    top_line = Turtle()
    top_line.hideturtle()
    top_line.penup()
    top_line.goto(-WIDTH // 2, HEIGHT // 2 - TOP_PADDING - 10)
    top_line.pencolor("white")
    top_line.pendown()
    for i in range(4):
        top_line.forward(150)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        line()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        with open("score.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.goto(0, HEIGHT // 2 - 1.5 * SIZE)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}   |    High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)



    def add_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score >= self.high_score:
            self.high_score = self.score
            with open("score.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
