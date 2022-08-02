from PIL import Image
import os
from functions import*
from pynput import mouse
from pynput.mouse import Button, Controller
import time
import requests

# I select the image i want to draw 
image_url = "https://cdn.futura-sciences.com/buildsv6/images/wide1920/6/5/2/652a7adb1b_98148_01-intro-773.jpg"
img_data = requests.get(image_url).content
with open('Image.jpg', 'wb') as handler:
    handler.write(img_data)
img = Image.open("Image.jpg")
img.show()

# I ask the user the top left and bootom right of the final image
c = 0
point1 = 0
point2 = 0

def on_click(x, y, button, pressed):
    global c
    global point1
    global point2
    if button == mouse.Button.left and pressed :
        c += 1
        if c == 1 :
            point1 = x,y
        elif c == 2 :
            point2 ==x,y 

        else : 
            return False

with mouse.Listener(
        on_click = on_click) as listener:
    listener.join()

width = abs(point1[0]-point2[0])
height = abs(point1[1]-point2[1])

# I resize the image so that she can fit into the blank space
if img.width > width :                       
    img.thumbnail((width,width))
if img.height > height :
    img.thumbnail((height,height))
img.save("Image-resize.jpg", "JPEG")
imgr = Image.open("Image-resize.jpg")
imgr.show()

# I change each pixel colour to the closest one from the game pallet
mouse = Controller()

for x in range(imgr.width) :
    for y in range(imgr.height) :
        r, g, b = imgr.getpixel((x, y))
        c = coordinates(r,g,b)

