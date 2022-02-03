from turtle import Turtle

POSITION=[(0,0),(-20,0),(-40,0)]

class Snake():
    
    def __init__(self):
        self.new_turtle = []
        self.create_snake()
        self.head = self.new_turtle[0]


    def create_snake(self):
        for i in POSITION:
            self.add_segments(i)


    def add_segments(self,position):  
        t = Turtle('square')
        t.color('green')
        t.penup()
        t.goto(position)
        self.new_turtle.append(t)


    def move(self):
        for i in range(len(self.new_turtle)-1,0,-1):
            new_x = self.new_turtle[i-1].xcor()
            new_y = self.new_turtle[i-1].ycor()
            self.new_turtle[i].goto(new_x,new_y)
        self.head.forward(15)


    def extend(self):
        self.add_segments(self.new_turtle[-1].position())
            

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)


    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)


    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)


    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)