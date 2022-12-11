##########https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/main/adafruit_hid/keycode.py
#####https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/main/adafruit_hid/keyboard.py
#####https://www.youtube.com/watch?v=aEWptdD32iA&ab_channel=NovaspiritTech
####https://docs.circuitpython.org/en/latest/README.html#get-circuitpython

###This works as of 11pm when you are using Edge with Bing.  F-Off if you think google has a superior product in Chromeum browsers and search engine
###I think this works if we have any sort of a state change on the Pico Pin



import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
####for using play/pause,etc__from adafruit_hid.consumer_control_code import ConsumerControlCode
####for using play/pause,etc__from adafruit_hid.consumer_control import ConsumerControl






btn1_pin = board.GP15
btn2_pin = board.GP16
btn3_pin = board.GP17
btn4_pin = board.GP18

keyboard = Keyboard(usb_hid.devices)

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

"""
btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN
"""
while True:
    if btn1.value:
        print("Rick Rolled")
        keyboard.send(Keycode.CONTROL, Keycode.T)
        keyboard.send(Keycode.R)
        keyboard.send(Keycode.I)
        keyboard.send(Keycode.C)
        keyboard.send(Keycode.K)
        keyboard.send(Keycode.SPACE)
        keyboard.send(Keycode.R)
        keyboard.send(Keycode.O)
        keyboard.send(Keycode.L)
        keyboard.send(Keycode.L)
        keyboard.send(Keycode.E)
        keyboard.send(Keycode.D)
        keyboard.send(Keycode.SPACE)
        keyboard.send(Keycode.V)
        keyboard.send(Keycode.I)
        keyboard.send(Keycode.D)
        keyboard.send(Keycode.ENTER)
        time.sleep(1)
        keyboard.send(Keycode.TAB)
        keyboard.send(Keycode.TAB)
        keyboard.send(Keycode.TAB)
        keyboard.send(Keycode.ENTER)
        keyboard.release_all
    time.sleep(.05)



















