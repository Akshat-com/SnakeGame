from turtle import Turtle
import random as rn

colours = ["cyan", "magenta", "lime", "gold", "silver", "red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "gray", "white"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = rn.randint(-250, +250)
        random_y = rn.randint(-250, +250)
        self.goto(random_x, random_y)
        self.color(colours[rn.randint(0, len(colours)-1)])