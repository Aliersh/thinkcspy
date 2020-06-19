'''The two spirals in this picture differ only by the turn angle. Draw both.'''

import turtle

# First pattern
def drawSpiral(t,ct,sz):
    for i in range(ct):
        t.forward(sz)
        t.left(90)
        sz+=1
        t.forward(sz)
        

wn=turtle.Screen()
wn.bgcolor("lightgreen")

cami=turtle.Turtle()
cami.color("blue")

drawSpiral(cami,40,10)

wn.exitonclick()

# Second pattern
def drawSpiral(t,ct,sz):
    for i in range(ct):
        t.forward(sz)
        t.left(89)
        sz+=1
        t.forward(sz)
        

wn=turtle.Screen()
wn.bgcolor("lightgreen")

cami=turtle.Turtle()
cami.color("blue")

drawSpiral(cami,40,10)

wn.exitonclick()