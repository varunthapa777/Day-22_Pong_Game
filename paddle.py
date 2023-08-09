from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("black")
        self.penup()
        self.setpos(position)

    def move_up(self):
        if self.ycor() < 240:
            new_ycor = self.ycor() + 20
            self.sety(new_ycor)

    def move_down(self):
        if self.ycor() > -240:
            new_ycor = self.ycor() - 20
            self.sety(new_ycor)
