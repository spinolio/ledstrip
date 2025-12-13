import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 10, auto_write=False)

rgw = ((0,1),(0,2),(1,0),(2,1),(1,0))
c = ((255, 0, 0), (0,0,255), (127,127,127))

# Flash a few LEDs white to give the look of police lights.

for r in range(5):
    for n in range(5):
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

