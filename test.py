from pynput import mouse,keyboard
import clipboard

def on_click(x, y, button, pressed):
    if button == mouse.Button.right and pressed :
        print(str(x)+","+str(y))
        clipboard.copy(str(x)+","+str(y))

with mouse.Listener(
        on_click = on_click) as listener:
    listener.join()





