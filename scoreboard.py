from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Verdana", 15, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        self.color("White")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"score: {self.score}", move=False
                   , align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.color("red")
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def turtle_score(self,size):
        self.clear()
        if size == "small":
            self.score += 1
        else:
            self.score += 3

        self.update_scoreboard()

