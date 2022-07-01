import time
import pynput
from pynput.mouse import Button, Controller
import tkinter

mouse = Controller()

print("Current position" + str(mouse.position))

'''
(231.2734375, 442.0390625) - First Sleep Button
 
(466.0078125, 524.6015625) - OK, after Sleep Button
 
(221.9296875, 525.3359375)- Save Button

(592.48828125, 639.16796875)- STOP Button!
'''

while True:
    mouse.position = (231.2734375, 442.0390625)
    time.sleep(0.03)
    mouse.click(Button.left, 2)
    mouse.position = (466.0078125, 524.6015625)
    time.sleep(0.03)
    mouse.click(Button.left, 2)
    mouse.position = (221.9296875, 525.3359375)
    time.sleep(0.03)
    mouse.click(Button.left, 2)
    mouse.position = (592.48828125, 642.16796875)
    time.sleep(0.9)
