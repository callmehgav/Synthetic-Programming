import time
import threading
from random import random
import numpy as np
from pynput.mouse import Button as pyB, Controller
from pynput.keyboard import Listener, KeyCode, Key, Controller as C
from tkinter import *

#one swing
minDelay = 2.4
#4 swings and .1 seconds
maxDelay = 9.7
everyMinute = 60
buttonLeftClick = pyB.left
start_stop_key = KeyCode(char='=')
exit_key = KeyCode(char='+')


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        print("Started Clicking")
        self.running = True

    def stop_clicking(self):
        print("Stopped Clicking")
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                delay = np.random.randint(minDelay,maxDelay)
                #10% chance of storing ore
                randPercent = np.random.randint(1,101)
                if  randPercent>90:
                    print('e clicked')
                    keyboard.press('e')
                    keyboard.release('e')

                mouse.click(self.button)
                time.sleep(delay)

def click():
    cm = ClickMouse()
    if self.running == True:
        cm.stop_clicking()
    else:
        cm.start_clicking()

keyboard = C()
mouse = Controller()
click_thread = ClickMouse(1, buttonLeftClick)
click_thread.start()
"""
#Create new window object
window = Tk()
window.title ("Random auto clicker")
#Define 2 lables min and max delay
l1= Label(window, text = "Min Delay:").grid(row=0, column = 0)
l2= Label(window, text = "Max Delay:").grid(row=0, column = 2)

txtMinDelay = StringVar()
e1 = Entry(window,textvariable =txtMinDelay).grid(row=0,column = 1)
txtMaxDelay = StringVar()
e2 = Entry(window,textvariable =txtMaxDelay).grid(row=0,column = 3)

#define buttons
btnStartStop=Button(window,text = "Start/Stop", width = 12, command = click).grid(row=2,column=3)
btnQuit=Button(window,text = "Quit", width = 12, command = exit).grid(row=2,column=4)


window.mainloop()
"""
def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
