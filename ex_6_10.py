'''Extend your program above. Draw five stars, but between each, pick up the pen, move forward by 
350 units, turn right by 144, put the pen down, and draw the next star. You’ll get something like this 
(note that you will need to move to the left before drawing your first star in order to fit everything 
in the window):'''

import turtle

def drawStar(t,sz):
    for i in range (5):
        for i in range(5):
            t.forward(sz)
            t.right(144)
        t.penup()
        t.right(144)
        t.forward(350)
        t.pendown()


wn=turtle.Screen()
cami=turtle.Turtle()

cami.penup()
cami.goto(100,0)
cami.pendown()
drawStar(cami,50)

wn.exitonclick()