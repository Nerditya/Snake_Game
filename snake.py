from turtle import Turtle, Screen, xcor

Starting_positions = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):

        self.segments = []
        self.create_snake()

        self.head = self.segments[0]

    def create_snake(self):
        for pos in Starting_positions:
            seg = Turtle("square")
            seg.color("white")
            seg.penup()
            seg.goto(pos)
            self.segments.append(seg)

    def move(self):
        length = len(self.segments)
        for s in range(length - 1, 0, -1):
            to_be_x = (self.segments[s - 1]).xcor()
            to_be_y = (self.segments[s - 1]).ycor()
            (self.segments[s]).goto(to_be_x, to_be_y)

        self.head.forward(20)

    def left(self):
        if self.head.heading() == 0:
            pass
        else:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() == 180:
            pass
        else:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() == 270:
            pass
        else:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90:
            pass
        else:
            self.head.setheading(270)

    def increasesize(self):
        seg = Turtle("square")
        seg.color("white")
        seg.penup()
        last = self.segments[len(self.segments) - 1]
        seg.goto(last.position())
        self.segments.append(seg)
