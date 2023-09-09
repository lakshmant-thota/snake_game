from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Verdana", 15, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.color("White")
        self.penup()
        self.goto(-100, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}           High Score: {self.high_score}", move=False
                   , align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.update_scoreboard()
    def turtle_score(self,size):
        self.clear()
        if size == "small":
            self.score += 1
        else:
            self.score += 3

        self.update_scoreboard()

