from pynput import mouse
import json

colour_list = []
def on_click(x, y, button, pressed):
    if button == mouse.Button.right and pressed :
        print(str(x)+","+str(y))
        colour_list.append({"x" : x,"y" : y })
        if len(colour_list) > 21 :
            return False
        

with mouse.Listener(
        on_click = on_click) as listener:
    listener.join()

print(colour_list)
jsonFile = open("data.json", "w")
jsonFile.close()
jsonString = json.dumps(colour_list)
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()

