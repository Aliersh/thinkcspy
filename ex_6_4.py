'''Draw this pretty pattern.'''

import turtle

def drawSquares(t,sz,ct):
    for i in range(ct):
        t.forward(sz/2)
        t.left(90)
        t.forward(sz/2)
        t.left(90)
        t.forward(sz)
        t.left(90)
        t.forward(sz)
        t.left(90)
        t.forward(sz)
        t.left(90)
        t.forward(sz/2)
        t.left(90)
        t.forward(sz/2)
        t.left(180)
        t.left(360/ct)
   
wn=turtle.Screen()
wn.bgcolor("lightgreen")

cami=turtle.Turtle()
cami.color("blue")

drawSquares(cami,80,5)

wn.exitonclick()

#It's not the same pattern that the exercises