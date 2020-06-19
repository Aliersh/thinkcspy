'''Modify the previous turtle walk program so that the turtle turns around when it hits the wall or when 
one turtle collides with another turtle (when the positions of the two turtles are closer than some small 
number).'''

import random
import turtle
from random import randint

def isInScreen(w,ta,tb):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleXa = ta.xcor()
    turtleYa = ta.ycor()
    turtleXb = tb.xcor()
    turtleYb = tb.ycor()

    stillIn = True
    if turtleXa > rightBound or turtleXa < leftBound:
        ta.right(180) # Hit the wall and turn around
        ta.forward(50)
    if turtleYa > topBound or turtleYa < bottomBound:
        ta.right(180)
        ta.forward(50)
    if turtleXb > rightBound or turtleXb < leftBound:
        tb.right(180)
        tb.forward(50)
    if turtleYb > topBound or turtleYb < bottomBound:
        tb.right(180)
        tb.forward(50)
    if (turtleXa - turtleXb) < 5 and (turtleYa - turtleYb) < 5: #Turn around if they are close
        ta.right(180)
        ta.forward(50)
        tb.right(180)
        tb.forward(50)

    return stillIn

t1 = turtle.Turtle()
t2 = turtle.Turtle()
wn = turtle.Screen()

t1.shape('turtle')
t2.shape('turtle')
t1.penup()
t2.penup()
t1.goto(randint(-100,0),randint(0,100))
t2.goto(randint(-100,0),randint(0,100))
t1.pendown()
t2.pendown()

while isInScreen(wn,t1,t2):
    coin = random.randrange(0, 2)
    if coin == 0:
        t1.left(random.randrange(1,360))
        t2.left(random.randrange(1,360))
    else:
        t1.right(random.randrange(1,360))
        t2.right(random.randrange(1,360))

    t1.forward(50)
    t2.forward(50)

wn.exitonclick()