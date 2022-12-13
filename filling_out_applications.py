import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
####for using play/pause,etc__from adafruit_hid.consumer_control_code import ConsumerControlCode
####for using play/pause,etc__from adafruit_hid.consumer_control import ConsumerControl






btn1_pin = board.GP16
btn2_pin = board.GP17
btn3_pin = board.GP18
btn4_pin = board.GP19
btn5_pin = board.GP20
btn6_pin = board.GP21
btn7_pin = board.GP22


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


btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

btn7 = digitalio.DigitalInOut(btn7_pin)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.DOWN

while True:
    if btn1.value:
        print("first name")
        keyboard.send(Keycode.R)
        keyboard.send(Keycode.R)
        keyboard.send(Keycode.R)
        keyboard.send(Keycode.R)
        keyboard.send(Keycode.R)
        keyboard.send(Keycode.R)
        keyboard.send(Keycode.R)
        keyboard.send(Keycode.R)
    time.sleep(.05)
    keyboard.release_all
    
    if btn2.value:
        print("last name")
        keyboard.send(Keycode.F)
        keyboard.send(Keycode.R)
        keyboard.send(Keycode.I)
        keyboard.send(Keycode.N)
        keyboard.send(Keycode.G)
        keyboard.send(Keycode.E)
        keyboard.send(Keycode.R)
    time.sleep(.05)
      
    
    if btn3.value:
        print("email")
        keyboard.send(Keycode.R)
        keyboard.send(Keycode.R)
        keyboard.send(Keycode.R)
        keyboard.send(Keycode.R)
        keyboard.send(Keycode.R)
        keyboard.send(Keycode.R)
        keyboard.send(Keycode.R)
        keyboard.send(Keycode.R)
        keyboard.send(Keycode.R)
        keyboard.send(Keycode.SHIFT, Keycode.TWO)
        keyboard.send(Keycode.G)
        keyboard.send(Keycode.M)
        keyboard.send(Keycode.A)
        keyboard.send(Keycode.I)
        keyboard.send(Keycode.L)
        keyboard.send(Keycode.PERIOD)
        keyboard.send(Keycode.C)
        keyboard.send(Keycode.O)
        keyboard.send(Keycode.M)
    time.sleep(.05)
    keyboard.release_all
    
    if btn4.value:
        print("phone")
        keyboard.send(Keycode.EIGHT)
        keyboard.send(Keycode.EIGHT)
        keyboard.send(Keycode.EIGHT)
        keyboard.send(Keycode.EIGHT)
        keyboard.send(Keycode.EIGHT)
        keyboard.send(Keycode.EIGHT)
        keyboard.send(Keycode.EIGHT)
        keyboard.send(Keycode.SEVEN)
        keyboard.send(Keycode.SEVEN)
        keyboard.send(Keycode.SEVEN)
    time.sleep(.05)
    keyboard.release_all
    
    if btn5.value:
        print("street address")
        keyboard.send(Keycode.THREE)
        keyboard.send(Keycode.EIGHT)
        keyboard.send(Keycode.EIGHT)
        keyboard.send(Keycode.ONE)
        keyboard.send(Keycode.SPACE)
        keyboard.send(Keycode.S)
        keyboard.send(Keycode.E)
        keyboard.send(Keycode.EIGHT)
        keyboard.send(Keycode.EIGHT)
        keyboard.send(Keycode.EIGHT)
        keyboard.send(Keycode.EIGHT)
        keyboard.send(Keycode.EIGHT)
        keyboard.send(Keycode.A)
        keyboard.send(Keycode.V)
        keyboard.send(Keycode.E)
    time.sleep(.05)
    keyboard.release_all
    
    if btn6.value:
        print("city")
        keyboard.send(Keycode.D)
        keyboard.send(Keycode.D)
        keyboard.send(Keycode.D)
        keyboard.send(Keycode.D)
        keyboard.send(Keycode.D)
        keyboard.send(Keycode.D)
        keyboard.send(Keycode.D)
        keyboard.send(Keycode.D)
    time.sleep(.05)
    keyboard.release_all
    
    if btn7.value:
        print("copy")
        keyboard.send(Keycode.CONTROL, Keycode.C)
    time.sleep(.05)
    keyboard.release_all


