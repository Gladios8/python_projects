from turtle import Turtle
FONT = ("courier",20 )

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.teleport(0,270)
        self.current_score()
        self.speed("fastest")


    def add_score(self):
        self.score += 1
        self.clear()
        self.teleport(0,270)
        self.current_score()

    def gameover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center" ,font=FONT)


    def current_score(self):
        self.write(f"Score = {self.score}", align="center",font=FONT)







