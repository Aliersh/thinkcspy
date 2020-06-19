'''Write a non-fruitful function drawEquitriangle(someturtle, somesize) which calls drawPoly from the 
previous question to have its turtle draw a equilateral triangle.'''

import turtle

def drawPoly(someturtle,somesides,somesize):
    for i in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(360/somesides)

def drawEquitriangle(someturtle,somesize):
    drawPoly(someturtle,3,somesize)

wn=turtle.Screen()
wn.bgcolor("lightgreen")

tess=turtle.Turtle()
tess.color("pink")

drawEquitriangle(tess,50)

wn.exitonclick()