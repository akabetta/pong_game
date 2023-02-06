from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("grey")
        self.penup()
        self.hideturtle()
        self.left_score=0
        self.right_score=0
        self.update_score()
    def update_score(self):
        self.clear()
        self.goto(-110,220)
        self.write(self.left_score,font=("Courier",45,"normal"))
        self.goto(90,220)
        self.write(self.right_score,font=("Courier",45,"normal"))
    def left_point(self):
        self.left_score+=1
        self.update_score()
    def right_point(self):
        self.right_score+=1
        self.update_score()


