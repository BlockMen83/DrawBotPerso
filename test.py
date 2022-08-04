from PIL import Image
import os
from functions import*
from pynput import mouse
from pynput.mouse import Button, Controller
import time
import requests

# I select the image i want to draw 
image_url = "https://upload.wikimedia.org/wikipedia/commons/9/9a/Gull_portrait_ca_usa.jpg"
img_data = requests.get(image_url).content
with open('Image.jpg', 'wb') as handler:
    handler.write(img_data)
img = Image.open("Image.jpg")
img.show()

# I ask the user the top left and bootom right of the final image
c = 0
point1 = 0
point2 = 0
print ("Enter the two points")
def on_click(x, y, button, pressed):
    global c
    global point1
    global point2
    if button == mouse.Button.left and pressed :
        c += 1
        if c == 1 :
            point1 = x,y
        elif c == 2 :
            point2 = x,y
            return False 
with mouse.Listener(
        on_click = on_click) as listener:
    listener.join()
print((point1),(point2))
width = abs(point1[0]-point2[0])
height = abs(point1[1]-point2[1])

# I resize the image so that she can fit into the blank space
if img.width > width :
    taille = width                       
    img.thumbnail((int(width/4),int(width/4)))

elif img.height > height :
    taille = height
    img.thumbnail((int(height/4),int(height/4)))

img.save("Image-resize.jpg", "JPEG")
imgr = Image.open("Image-resize.jpg")
imgr.show()

# I change each pixel colour to the closest one from the game pallet and I control the mouse to draw the image
mouse = Controller()
pointx = point1[0]
pointy = point1[1]
for x in range(imgr.width) :
    for y in range(imgr.height) :
        r, g, b = imgr.getpixel((x, y))
        c = coordinates(r,g,b)
        mouse.position = (c)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(0.01)
        mouse.position = (pointx,pointy)
        mouse.press(Button.left)
        mouse.release(Button.left)
        pointx += 4
        if pointx >= taille+point1[0] :
            pointx = point1[0]
            pointy += 4




