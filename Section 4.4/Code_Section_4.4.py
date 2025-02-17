import time
import board
import analogio
import digitalio
import usb_hid
from adafruit_apds9960.apds9960 import APDS9960
from adafruit_apds9960 import colorutility
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)

i2c = board.STEMMA_I2C()
apds = APDS9960(i2c)
apds.enable_color = True

while True:
    # wait for color data to be ready
    while not apds.color_data_ready:
        time.sleep(0.005)

    # get the colour and brightness data - r: Red colour; g: Green colour; b: Blue colour; c: Brightness
    r, g, b, c = apds.color_data

    kbd = Keyboard(usb_hid.devices)

    # Formula for detection of red color
    red = (r-g)/g
    # when ever red has a value greater than 3 : condition when red color is detected
    # Print * When RED color is detected
    if red > 3:
        kbd.press(Keycode.SHIFT, Keycode.EIGHT)
        print("RED")
        kbd.release(Keycode.SHIFT, Keycode.EIGHT)

    # In case of green color;we have the value of g variable greater than b and r variable
    # Enter Space When GREEN color is detected
    if g>r and g>b:
        kbd.press(Keycode.SPACE)

        print("GREEN")
        kbd.release(Keycode.SPACE)

    # # In case of blue color;we have the value of b variable greater than g and r variable
    # Enter Backspace When BLUE color is detected
    if b>r and b>g:
        kbd.press(Keycode.BACKSPACE)
        print("BLUE")
        kbd.release(Keycode.BACKSPACE)

    # Quit the program When it becomes dark
    # Its darkness condition when brightness variable - c falls below than 150
    if c < 150:

        print("DARK QUIT")
        break


    time.sleep(0.5)

#End of Code
