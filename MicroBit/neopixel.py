from microbit import *
from neopixel import NeoPixel
num_pixels = 8
foreground = [0x00, 0x00, 0xFF] # Hex color - red, green and blue
background = [0x10, 0x10, 0x10]
ring = NeoPixel(pin2, num_pixels)


while True:
    # blue dot circles around a white background (for PixelRing 24)
    for i in range(0, num_pixels):
    ring[i] = foreground # set pixel i to foreground
    ring.show() # actually display it
    sleep(50) # milliseconds
    ring[i] = background # set pixel to background before moving on
    ring.show()