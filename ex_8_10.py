'''Sepia Tone images are those brownish colored images that may remind you of times past. 
The formula for creating a sepia tone is as follows:

newR = (R × 0.393 + G × 0.769 + B × 0.189)
newG = (R × 0.349 + G × 0.686 + B × 0.168)
newB = (R × 0.272 + G × 0.534 + B × 0.131)

Write a function to convert an image to sepia tone. Hint: Remember that rgb values must be integers 
between 0 and 255.'''

import image

img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,15)   # setDelay(0) turns off animation

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)

        newred = (p.getRed() * 0.393) + (p.getGreen() * 0.769) + (p.getBlue() * 0.189)
        newgreen = (p.getRed() * 0.349) + (p.getGreen() * 0.686) + (p.getBlue() * 0.168)
        newblue = (p.getRed() * 0.272) + (p.getGreen() * 0.534) + (p.getBlue() * 0.131)

        newpixel = image.Pixel(newred, newgreen, newblue)

        img.setPixel(col, row, newpixel)

img.draw(win)
win.exitonclick()