'''Write a non-fruitful function to draw a five pointed star, where the length of each side is 100 units.'''

import turtle

def drawStar(t,sz):
    for i in range(5):
        t.forward(sz)
        t.right(180-180/5)

wn=turtle.Screen()
cami=turtle.Turtle()

drawStar(cami,100)

wn.exitonclick()