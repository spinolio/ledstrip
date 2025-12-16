# Set the LEDs to random colors. This script is mostly about testing different
# ways of making the colors seem nice and saturated. Just setting RGB all to
# some random values makes for a lot pastels.

import board
import neopixel
import time
import random

pixels = neopixel.NeoPixel(board.D18, 10, auto_write=False)
time.sleep(1)

pixels.fill([0,0,0])

# This list represents the other two colors of RGB when one color
# is chosen. 0=R, 1=G, 2=B, so for index 0, the other two indices
# are 1 and 2. This makes for less if/then/else code below.
dim = [(1,2), (0,2), (0,1)]

while True:
    a=[0, 0, 0]

    # Select a random LED
    n=random.randrange(0,10)

    # Randomly select the primary color
    c = random.randrange(0,3)
    a[c] = random.randrange(0,32)

    # Select only one of the ramaining two colors. The third LED will
    # be left dark for more color saturation.
    s = random.randrange(0,2)
    a[dim[c][s]] = random.randrange(0,16)
    a[dim[c][(s+1)%2]] = 0

    pixels[n] = a
    pixels.show()
    time.sleep(0.1)

