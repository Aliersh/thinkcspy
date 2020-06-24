'''Write a non-fruitful function drawPoly(someturtle, somesides, somesize) which makes a turtle draw a 
regular polygon. When called with drawPoly(tess, 8, 50), it will draw a shape like this:'''

import turtle

def drawPoly(someturtle,somesides,somesize):
    for i in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(360/somesides)

wn=turtle.Screen()
wn.bgcolor("lightgreen")

tess=turtle.Turtle()
tess.color("pink")

drawPoly(tess,8,50)

wn.exitonclick()