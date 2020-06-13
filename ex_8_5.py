'''Modify the turtle walk program so that you have two turtles each with a random starting location. 
Keep the turtles moving until one of them leaves the screen.'''

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
        stillIn = False
    if turtleYa > topBound or turtleYa < bottomBound:
        stillIn = False
    if turtleXb > rightBound or turtleXb < leftBound:
        stillIn = False
    if turtleYb > topBound or turtleYb < bottomBound:
        stillIn = False

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