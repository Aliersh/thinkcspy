'''Write a program to draw this. Assume the innermost square is 20 units per side, and each successive 
square is 20 units bigger, per side, than the one inside it.'''

import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

def movePoint(t,xc,yc):
    t.penup()
    t.goto(xc,yc)
    t.pendown()


wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("pink")

sz=20
x=0
y=0
for i in range(5):
    drawSquare(alex,sz)
    x-=10
    y-=10
    sz+=20
    movePoint(alex,x,y)

wn.exitonclick()