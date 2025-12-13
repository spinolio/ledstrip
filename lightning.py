import board
import neopixel
import time

# Array to hold which LEDs to flash.

z = [0,1,0,1,0,0,1,0,0,0]

pixels = neopixel.NeoPixel(board.D18, 10, auto_write=False)

# Set the strip to red

pixels.fill((31, 0, 0))
pixels.show()
time.sleep(1)

# Flash a few LEDs white to give the look of lightning.

for n in range(20):
    for i in range(3):
        # Set specific LEDs to white
        for j in range(10):
            if z[j] == 1:
                pixels[j] = (31,31,31)
        pixels.show()
        time.sleep(0.05)

        # Set white LEDs back to red
        for j in range(10):
            if z[j] == 1:
                pixels[j] = (31, 0, 0)
        pixels.show()
        time.sleep(0.05)

    time.sleep(4)
pixels.fill((0,0,0))
pixels.show()

