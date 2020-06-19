'''Extend the star function to draw an n pointed star. (Hint: n must be an odd number greater or equal to 3).'''

import turtle

def drawnStar(t,sz,n):
    for i in range(n):
        t.forward(sz)
        t.right(180-180/n)

wn=turtle.Screen()
cami=turtle.Turtle()

drawnStar(cami,100,7)

wn.exitonclick()