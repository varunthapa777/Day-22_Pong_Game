from turtle import Turtle


class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("White")
        self.pensize(9)
        self.draw_line()

    def draw_line(self):
        self.penup()
        self.setpos(0, 300)
        self.setheading(270)

        while self.ycor() > -300:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(60)

