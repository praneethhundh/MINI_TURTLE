from turtle import Turtle

# Define initial snake positions and movement constants
posi = [(0, 0), (-20, 0), (-40, 0)]
move_dist = 20
Down = 270
Up = 90
Left = 180
Right = 0

class Snake:
    def __init__(self):
        self.segs = []
        self.create_snake()
        self.head = self.segs[0]

    def create_snake(self):
        for p in posi:
           self.addsnake(p)
    def extend(self):
        self.addsnake(self.segs[-1].position())
    def addsnake(self,posi):
        new = Turtle(shape="square")
        new.color("white")
        new.penup()
        new.goto(posi)
        self.segs.append(new)
    def move(self):
        for segi in range(len(self.segs) - 1, 0, -1):
            newx = self.segs[segi - 1].xcor()
            newy = self.segs[segi - 1].ycor()
            self.segs[segi].goto(newx, newy)
        self.head.forward(move_dist)

    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(Up)

    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)

    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(Left)

    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(Right)
