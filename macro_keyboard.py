#####https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/main/adafruit_hid/keycode.py
#####https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/main/adafruit_hid/keyboard.py
#####https://www.youtube.com/watch?v=aEWptdD32iA&ab_channel=NovaspiritTech
####https://docs.circuitpython.org/en/latest/README.html#get-circuitpython



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

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

while True:
    if btn1.value:
        print("copy")
        keyboard.send(Keycode.CONTROL, Keycode.C)
    time.sleep(.05)
    keyboard.release_all
    
    if btn2.value:
        print("paste")
        keyboard.press(Keycode.CONTROL, Keycode.V)
        keyboard.release(Keycode.CONTROL, Keycode.V)
    time.sleep(.05)
      
    
    if btn3.value:
        print("cut")
        keyboard.send(Keycode.CONTROL, Keycode.X)
    time.sleep(.05)
    keyboard.release_all


    if btn4.value:
        print("undo")
        keyboard.send(Keycode.CONTROL, Keycode.Z)
    time.sleep(.05)
    keyboard.release_all
