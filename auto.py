import pyautogui
from PIL import Image, ImageGrab
import time



def OnCollision(image):
    color = 100
    data = image.load()
    for i in range(150, 360):
        for j in range(390, 470):
            if data[i, j] > color:
                pyautogui.keyDown("Up")
                return(True)
    
    for k in range(160, 360):
        for l in range(270, 388):
            if data[k, l] > color:
                pyautogui.keyDown("Down")
                return(True)

    return(False)

def TakeScreenshot():
    image = ImageGrab.grab().convert('L')
    return image

if __name__ == "__main__":
    time.sleep(5)
    while True:
        image = TakeScreenshot()
        OnCollision(image)
            
                    

    image.show()
    time.sleep(10)