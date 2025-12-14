import board
import neopixel
import time

# The LED string is 10 LEDs, so consider it split into a left and right half.
# We will alternately flash different colors on left and right side. The red
# blue and white colors are defined in the list 'c'. The 'rgw' list has the
# pairings of left/right colors for each flashing iteration.

r=0
b=1
w=2
c = ((255, 0, 0), (0,0,255), (127,127,127))
rgw = ((r,b),(r,w),(b,r),(w,b),(b,r))

pixels = neopixel.NeoPixel(board.D18, 10, auto_write=False)


# Flash a few LEDs white to give the look of police lights.

for r in range(5):
    # Loop over our color pairs, doing two kinds of alternating flashing.
    for n in range(5):
        # First, flash three times quickly per left/right side.
        for f in range(3):
            lc = c[rgw[n][0]]
            for i in range(5):
                pixels[i] = lc
            pixels.show()
            time.sleep(0.05)
            pixels.fill((0,0,0))
            pixels.show()
            time.sleep(0.05)

        for f in range(3):
            rc = c[rgw[n][1]]
            for i in range(5,10):
                pixels[i] = rc
            pixels.show()
            time.sleep(0.05)
            pixels.fill((0,0,0))
            pixels.show()
            time.sleep(0.05)

        # Now simply flash a bit more slowly back and forth.
        for f in range(3):
            lc = c[rgw[n][0]]
            for i in range(5):
                pixels[i] = lc
            pixels.show()
            time.sleep(0.1)
            pixels.fill((0,0,0))
            rc = c[rgw[n][1]]
            for i in range(5,10):
                pixels[i] = rc
            pixels.show()
            time.sleep(0.1)
            pixels.fill((0,0,0))
            pixels.show()

pixels.fill((0,0,0))
pixels.show()

