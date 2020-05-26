import time
import threading
from random import random
import numpy as np
from pynput.mouse import Button as pyB, Controller
from pynput.keyboard import Listener, KeyCode, Key, Controller as C
from tkinter import *

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
                firemakingAutoClicker(self)                  #firemaking auto clicker
                #fletchingAutoClicker(self)                  #fletching auto clicker
                #miningAutoClicker()                    #mining auto clicker
                #smithingAutoClicker()                  #smithing auto clicker

def fletchingAutoClicker(self):
    #click bank
    mouse.click(self.button)
    #wait a second
    time.sleep(1)
    #grab preset one
    keyboard.press('1')
    keyboard.release('1')
    #wait a second
    time.sleep(1)
    #select fletching toolbind
    keyboard.press('1')
    keyboard.release('1')
    #wait a sec
    time.sleep(1)
    #select space
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    #wait a random delay
    delay = np.random.randint(30 , 45)
    time.sleep(delay)

def firemakingAutoClicker(self):
    #click bank
    mouse.click(self.button)
    #wait 3-6 seconds to run to and open bank
    time.sleep(np.random.randint(3,6))
    #grab preset one
    keyboard.press('1')
    keyboard.release('1')
    #wait a second
    time.sleep(2)
    #select fletching toolbind
    keyboard.press('1')
    keyboard.release('1')
    #wait a sec11
    time.sleep(np.random.randint(1,2))
    #click add to bonfire
    mouse.click(self.button)
    #wait a random delay
    delay = np.random.randint(60,90)
    time.sleep(delay)


def miningAutoClicker(self):
    # one swing
    minDelay = 2.4
    # 4 swings and .1 seconds
    maxDelay = 9.7
    delay = np.random.randint(minDelay, maxDelay)
    # 10% chance of storing ore
    randPercent = np.random.randint(1, 101)
    if randPercent > 80:
        print('e clicked')
        keyboard.press('e')
        keyboard.release('e')

    time.sleep(1)
    mouse.click(self.button)
    time.sleep(delay)

def smithingAutoClicker(self):
    # 28ish bars
    minDelay = 30
    # 58ish bars
    maxDelay = 60
    # random time intween
    delay = np.random.randint(minDelay, maxDelay)
    # Click
    mouse.click(self.button)
    # wait a sec then click then space
    time.sleep(1)
    mouse.click(self.button)
    time.sleep(1)
    print('space=  clicked')
    keyboard.press(Key.space)
    keyboard.release(Key.space)

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
