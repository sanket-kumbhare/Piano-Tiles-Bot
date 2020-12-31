import pyautogui

"""
For finding out the pixel position run the following code in python shell 
and note down the mouse position

import pyautogui
pyautogui.displayMousePosition()

"""

# Tile1 Pixel Postion: X: 820  Y:  380
# Tile2 Pixel Postion: X: 880  Y:  380
# Tile3 Pixel Postion: X: 940  Y:  380
# Tile4 Pixel Postion: X: 1000 Y:  380

# If pixel color is black then click on the pixel

try:
    while True:

        if pyautogui.pixel(710, 380)[0] == 0:
            pyautogui.click(710, 380)

        if pyautogui.pixel(875, 380)[0] == 0:
            pyautogui.click(875, 380)

        if pyautogui.pixel(1035, 380)[0] == 0:
            pyautogui.click(1035, 380)

        if pyautogui.pixel(1200, 380)[0] == 0:
            pyautogui.click(1200, 380)

except KeyboardInterrupt:
    pass
