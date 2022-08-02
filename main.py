from PIL import Image
import os
from functions import*
from pynput import mouse
import time

# I select the image i want to draw 
img = Image.open("Image3.jpg")

# I ask the user the top left and bootom right of the final image
c = 0
taille_x = 0
taille_y = 0

def on_click(x, y, button, pressed):
    global c
    global taille_x
    global taille_y
    if button == mouse.Button.left and pressed :
        c += 1
        if c < 3 :
            taille_x = abs(taille_x-x) 
            taille_y = abs(taille_y-y) 
        else : 
            return False

with mouse.Listener(
        on_click = on_click) as listener:
    listener.join()

# I resize the image so that she can fit into the blank space
if img.width > taille_x :                       
    img.thumbnail((taille_x,taille_x))
if img.height > taille_y :
    img.thumbnail((taille_y,taille_y))
img.save("Image-resize.jpg", "JPEG")
imgr = Image.open("Image-resize.jpg")
imgr.show()

# I change each pixel colour to the closest one from the game pallet
#for x in range(imgr.width) :
#    for y in range(imgr.height) :
#        r, g, b = imgr.getpixel((x, y))
#        c = new_colour(r,g,b)
#        imgr.putpixel( (x,y), (c%256,int(c/256)%256,int(c/256**2)))
