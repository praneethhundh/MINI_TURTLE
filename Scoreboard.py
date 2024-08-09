from turtle import Turtle
Align="center"
font=("Arial",20,"normal")
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("pink")
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        self.updates()
    def updates(self):
        self.write(f"Score:{self.score}",align=Align,font=font)
    def gameover(self):
        self.goto(0,0)
        self.write("gameover",align=Align,font=font)
    def increase_score(self):
        self.score+=1
        self.clear()
        self.updates()