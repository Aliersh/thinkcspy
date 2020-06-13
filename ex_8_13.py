'''Write a general pixel mapper function that will take an image and a pixel mapping function as parameters. 
The pixel mapping function should perform a manipulation on a single pixel and return a new pixel.'''

# I couldn't do this exercise. Below the answer

import image

def pixelMapper(oldimage, rgbFunction):
    width = oldimage.getWidth()
    height = oldimage.getHeight()
    newim = image.EmptyImage(width, height)

    for row in range(height):
        for col in range(width):
            originalpixel = oldimage.getPixel(col, row)
            newpixel = rgbFunction(originalpixel)
            newim.setPixel(col, row, newpixel)

    return newim

def graypixel(oldpixel):
    intensitysum = oldpixel.getRed() + oldpixel.getGreen() + oldpixel.getBlue()
    aveRGB = intensitysum // 3
    newPixel = image.Pixel(aveRGB, aveRGB, aveRGB)
    return newPixel

win = image.ImageWin()
img = image.Image("luther.jpg")

newim = pixelMapper(img, graypixel)
newim.draw(win)

win.exitonclick()