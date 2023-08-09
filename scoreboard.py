from turtle import Turtle

STYLE = ("courier", 70, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("yellow")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.setpos(-110, 200)
        self.write(f"{self.l_score}", move=False, align="center", font=STYLE)
        self.setpos(110, 200)
        self.write(f"{self.r_score}", move=False, align="center", font=STYLE)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def winner(self, player):
        self.clear()
        self.setpos(0, -10)
        self.pencolor("pink")
        self.write(f"{player} WINS!", move=False, align="center", font=("Arial", 30, "bold"))

