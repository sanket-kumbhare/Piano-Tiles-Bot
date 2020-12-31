# Piano Tiles Bot

## Description
Simple Piano Tiles Bot made by using PyAutoGui Library. <br><br>
<img src="https://github.com/Sanket-Kumbhare/Piano-Tiles-Bot/blob/master/src/piano_tiles_gameplay.gif" width="600" />

## Working
- First we have to find out the pixel position of the tiles. This can be done by using running following command in python shell.
> import pyautogui <br>
> pyautogui.displayMousePosition()

This will show you the pixel position of mouse cursor. Point mouse at the center of each lane of tiles. And note down the x-coordinates and y-coordinate. We will keep the y-coordinate same for each lane.

- Check if the pixel color is black.
- If black click on the pixel.
- Do same for the rest of the lane.

## Libraries
* [PyAutoGui](https://pypi.org/project/PyAutoGUI/)

Game was running on browser [click here](https://www.crazygames.com/game/piano-tiles-2-online) to play Piano Tiles 2 online
