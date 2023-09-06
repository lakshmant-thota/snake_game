from turtle import Turtle
from snake import Snake
import random
# one glitch is we can have the food at the location of the snake
# so need to take care of the location of the food

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.small_food()
        self.speed("fastest")
        self.refresh()

    def big_food(self):
        self.color("cyan")
        self.shapesize(stretch_len=1, stretch_wid=1)

    def small_food(self):
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)

    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        # for seg in snake.segments:
        #     if seg.position()[0] == random_x and seg.position()[1] == random_y:
        #         self.refresh()
        self.goto(random_x, random_y)
