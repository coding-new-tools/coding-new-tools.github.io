# CircuitPlaygroundExpress_NeoPixel

import time

import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
pixels.fill((0, 0, 0))
pixels.show()

# define some colors (R,G,B) / (255,255,255)
RED = 0x100000  # (0x10, 0, 0) also works
YELLOW = (0x10, 0x10, 0)
GREEN = (0, 0x10, 0)
AQUA = (0, 0x10, 0x10)
BLUE = (0, 0, 0x10)
PURPLE = (0x10, 0, 0x10)
BLACK = (0, 0, 0)
CUSTOM_COLOR=(100,100,0)

while True:
    pixels[2]=BLUE
    time.sleep(1)
    pixels[2]=BLACK
    time.sleep(1)
