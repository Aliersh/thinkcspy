'''Write a function to convert the image to grayscale.'''

import image

img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,15)   # setDelay(0) turns off animation

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        newred = (p.getRed()+p.getGreen()+p.getBlue())/3
        newgreen = (p.getRed()+p.getGreen()+p.getBlue())/3
        newblue = (p.getRed()+p.getGreen()+p.getBlue())/3

        newpixel = image.Pixel(newred, newgreen, newblue)

        img.setPixel(col, row, newpixel)

img.draw(win)
win.exitonclick()