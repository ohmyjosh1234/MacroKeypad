#Version 1.1.5

import time
import board
import digitalio
import pwmio
from adafruit_debouncer import Button
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Define Environment Variables
keyboard = Keyboard(usb_hid.devices)

ModVAR = ["ENTER"]
BTN_1_VAR = ["F13"]
BTN_2_VAR = ["F14"]
BTN_3_VAR = ["F15"]
BTN_4_VAR = ["F16"]
BTN_5_VAR = ["F17"]
BTN_6_VAR = ["F18"]
BTN_7_VAR = ["F19"]
BTN_8_VAR = ["F20"]
BTN_9_VAR = ["GUI", "L"]
BTN_10_VAR = ["F21"]
BTN_11_VAR = ["F22"]
BTN_12_VAR = ["F23"]

# Setup GPIO Keyboard Pins
btn1_pin_input = digitalio.DigitalInOut(board.GP1)
btn2_pin_input = digitalio.DigitalInOut(board.GP2)
btn3_pin_input = digitalio.DigitalInOut(board.GP3)
btn4_pin_input = digitalio.DigitalInOut(board.GP4)
btn5_pin_input = digitalio.DigitalInOut(board.GP5)
btn6_pin_input = digitalio.DigitalInOut(board.GP6)
btn7_pin_input = digitalio.DigitalInOut(board.GP7)
btn8_pin_input = digitalio.DigitalInOut(board.GP8)
btn9_pin_input = digitalio.DigitalInOut(board.GP9)
btn10_pin_input = digitalio.DigitalInOut(board.GP10)
btn11_pin_input = digitalio.DigitalInOut(board.GP11)
btn12_pin_input = digitalio.DigitalInOut(board.GP12)
btn_mod_pin_input = digitalio.DigitalInOut(board.GP17)

# Setup GPIO Keyboard Pins Direction
for btn in [btn1_pin_input, btn2_pin_input, btn3_pin_input, btn4_pin_input, btn5_pin_input, btn6_pin_input,
            btn7_pin_input, btn8_pin_input, btn9_pin_input, btn10_pin_input, btn11_pin_input, btn12_pin_input, btn_mod_pin_input]:
    btn.switch_to_input(pull=digitalio.Pull.UP)

# Define As A Button And Debounce
btn1_pin = Button(btn1_pin_input, value_when_pressed=False)
btn2_pin = Button(btn2_pin_input, value_when_pressed=False)
btn3_pin = Button(btn3_pin_input, value_when_pressed=False)
btn4_pin = Button(btn4_pin_input, value_when_pressed=False)
btn5_pin = Button(btn5_pin_input, value_when_pressed=False)
btn6_pin = Button(btn6_pin_input, value_when_pressed=False)
btn7_pin = Button(btn7_pin_input, value_when_pressed=False)
btn8_pin = Button(btn8_pin_input, value_when_pressed=False)
btn9_pin = Button(btn9_pin_input, value_when_pressed=False)
btn10_pin = Button(btn10_pin_input, value_when_pressed=False)
btn11_pin = Button(btn11_pin_input, value_when_pressed=False)
btn12_pin = Button(btn12_pin_input, value_when_pressed=False)
btn_mod_pin = Button(btn_mod_pin_input, value_when_pressed=False)

# Setup GPIO LED Pins
key_leds = [
    pwmio.PWMOut(board.GP14, frequency=5000, duty_cycle=0),
    digitalio.DigitalInOut(board.GP0),
    pwmio.PWMOut(board.GP16, frequency=5000, duty_cycle=0),
    pwmio.PWMOut(board.GP15, frequency=5000, duty_cycle=0),
    pwmio.PWMOut(board.GP18, frequency=5000, duty_cycle=0),
    pwmio.PWMOut(board.GP28, frequency=5000, duty_cycle=0),
    pwmio.PWMOut(board.GP19, frequency=5000, duty_cycle=0),
    pwmio.PWMOut(board.GP27, frequency=5000, duty_cycle=0),
    pwmio.PWMOut(board.GP20, frequency=5000, duty_cycle=0),
    pwmio.PWMOut(board.GP26, frequency=5000, duty_cycle=0),
    pwmio.PWMOut(board.GP21, frequency=5000, duty_cycle=0), 
    pwmio.PWMOut(board.GP22, frequency=5000, duty_cycle=0),
    pwmio.PWMOut(board.GP13, frequency=5000, duty_cycle=0),
    
]

# Set GP0 as output
key_leds[1].direction = digitalio.Direction.OUTPUT

# Function to send multiple keycodes
def send_keys(keycodes):
    key_list = [getattr(Keycode, key) for key in keycodes]
    keyboard.send(*key_list)

# Function to quickly light up and fade out an LED
def fade_led(led):
    if isinstance(led, pwmio.PWMOut):
        # Turn LED on quickly
        led.duty_cycle = 65535
        time.sleep(0.05)  # Short delay to keep the LED on at full brightness
        # Gradually fade out the LED
        for i in range(65535, 0, -5000):
            led.duty_cycle = i
            time.sleep(0.01)

def flash_led(led):
    if isinstance(led, digitalio.DigitalInOut):
    
        led.value = True
        time.sleep(0.1)
        led.value = False  

def power_on_animation():
    for led in key_leds:
        if isinstance(led, pwmio.PWMOut):
           
            for i in range(0, 65535, 5000):
                led.duty_cycle = i
                time.sleep(0.02)
            time.sleep(0.1)  
        elif isinstance(led, digitalio.DigitalInOut):
            # Turn on non-PWM LED (GP0) and then turn it off
            led.value = True
            time.sleep(0.2)
            led.value = False 

    # Fade out all PWM LEDs at the end of the animation
    for led in key_leds:
        if isinstance(led, pwmio.PWMOut):
            for i in range(65535, 0, -5000):
                led.duty_cycle = i
                time.sleep(0.02)




power_on_animation()






while True:
    btn1_pin.update()
    btn2_pin.update()
    btn3_pin.update()
    btn4_pin.update()
    btn5_pin.update()
    btn6_pin.update()
    btn7_pin.update()
    btn8_pin.update()
    btn9_pin.update()
    btn10_pin.update()
    btn11_pin.update()
    btn12_pin.update()
    btn_mod_pin.update()

    if btn1_pin.pressed:
        print("b1 pressed")
        send_keys(BTN_1_VAR)
        fade_led(key_leds[0])
        
    if btn2_pin.pressed:
        print("b2 pressed")
        send_keys(BTN_2_VAR)
        flash_led(key_leds[1])  # Use flash_led for GP0
        
    if btn3_pin.pressed:
        print("b3 pressed")
        send_keys(BTN_3_VAR)
        fade_led(key_leds[2])
        
    if btn4_pin.pressed:
        print("b4 pressed")
        send_keys(BTN_4_VAR)
        fade_led(key_leds[3])
        
    if btn5_pin.pressed:
        print("b5 pressed")
        send_keys(BTN_5_VAR)
        fade_led(key_leds[4])
        
    if btn6_pin.pressed:
        print("b6 pressed")
        send_keys(BTN_6_VAR)
        fade_led(key_leds[5])
        
    if btn7_pin.pressed:
        print("b7 pressed")
        send_keys(BTN_7_VAR)
        fade_led(key_leds[6])
        
    if btn8_pin.pressed:
        print("b8 pressed")
        send_keys(BTN_8_VAR)
        fade_led(key_leds[7])
        
    if btn9_pin.pressed:
        print("b9 pressed")
        send_keys(BTN_9_VAR)
        fade_led(key_leds[8])
        
    if btn10_pin.pressed:
        print("b10 pressed")
        send_keys(BTN_10_VAR)
        fade_led(key_leds[9])
        
    if btn11_pin.pressed:
        print("b11 pressed")
        send_keys(BTN_11_VAR)
        fade_led(key_leds[10])
        
    if btn12_pin.pressed:
        print("b12 pressed")
        send_keys(BTN_12_VAR)
        fade_led(key_leds[11])
        
    if btn_mod_pin.pressed:
        print("BTN_MOD_13 pressed")
        send_keys(ModVAR)
        fade_led(key_leds[12])

