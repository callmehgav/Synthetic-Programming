import time
import threading
from random import random
import numpy as np
from pynput.mouse import Button as pyB, Controller
from pynput.keyboard import Listener, KeyCode, Key, Controller as C
from time import sleep
from tkinter import *

everyMinute = 60
buttonLeftClick = pyB.left
buttonRightClick = pyB.right
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
                #@@@@@@@@@@@@@@@@@@@@@
                #randomAutoClickerWithButtonPress(self)
                #buttonPress(self)
                #clickPresetClickToolTipSpace(self)
                #quickRandomAutoClicker(self)
                #t5ArtifactBot(self)
                #t17ArtifactBot(self)
                #t100ArtifactBot(self)
                #t101ArtifactBot(self)
                #t102ArtifactBot(self)
                #t107ArtifactBot(self)
                #t114ArtifactBot(self)
                #t115ArtifactBot(self)
                #t115ArtifactBotWTele(self)
                #t119ArtifactBotWTele(self)

                #t118ArtifactBot(self)

                #t114ArtifactBotWBoost(self)
                #dragonkinBot(self)
                fishingBot(self)

                #firemakingBot(self);
                #cookingBot(self)
                #agilityAutoClickerAndEat(self)
                #buryInv(self)
                #firemakingAutoClicker(self)                  #firemaking auto clicker
                #fletchingAutoClicker(self)                  #fletching auto clicker / crafting /herb
                #miningAutoClicker(self)                    #mining auto clicker / arch
                #miningAutoClickerWithDrop(self)                    #mining auto clicker
                #smithingAutoClicker(self)                  #smithing auto clicke
                #heatAndSmith(self)
def grabPresetOne(self):
    mouse.click(self.button)
    time.sleep(np.random.randint(3, 4))
    keyboard.press('1')
    keyboard.release('1')
    time.sleep(np.random.randint(1, 2))

def firemakingBot(self):
    grabPresetOne(self)
    #move mouse back to fire pit
    moveMouse(returnInt(607, 640),returnInt(466, 480))
    time.sleep(np.random.randint(2, 4))
    mouse.click(self.button)
    time.sleep(returnInt(45, 60))

    #move mouse to bank
    moveMouse(returnInt(773, 785),returnInt(469, 489))
    time.sleep(returnInt(1, 2))

def cookingBot(self):
    grabPresetOne(self)
    #move mouse back to fire pit
    moveMouse(returnInt(614, 640),returnInt(463, 470))
    time.sleep(np.random.randint(3, 4))
    mouse.click(self.button)
    time.sleep(np.random.randint(3, 4))
    # select space
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    time.sleep(returnInt(45, 60))

    #move mouse to bank
    moveMouse(returnInt(778, 784),returnInt(471, 482))
    time.sleep(returnInt(3, 4))


def actionBarE():
    # select item
    keyboard.press('e')
    keyboard.release('e')
    # wait a sec
    time.sleep(1)
    # select space
    keyboard.press(Key.space)
    keyboard.release(Key.space)

def tenPercentChanceOfE():
    # 10% chance of storing ore
    randPercent = np.random.randint(1, 101)
    if randPercent > 80:
        #rint('e clicked')
        keyboard.press('e')
        keyboard.release('e')

def quickRandomAutoClicker(self):
    mouse.click(self.button)
    delay = np.random.randint(5,15)
    #tenPercentChanceOfE()
    time.sleep(delay)

def returnInt (minInt, maxInt):
    return np.random.randint(minInt, maxInt)

def moveMouse(x,y):
    mouse.position = (x, y)
##########################################################
# def ArtifactBotBlueprint(self):
#     mouse.click(self.button)
#     print("Clicked")
#     time.sleep(returnInt(8, 10))
#     # move mouse to pile
#     moveMouse(returnInt(593, 616),returnInt(369, 388))
#     time.sleep(returnInt(2, 4))
#     mouse.click(self.button)
#     print("Clicked")
#     time.sleep(returnInt(8, 10))
#     #READJUST
#     moveMouse(returnInt(712, 733),returnInt(495, 514))
#     time.sleep(returnInt(1, 2))
#     #click randomly for 2 min
#     t_end = time.time() + returnInt(55, 60) * returnInt(1, 2)
#     print("Wait time: " + str(t_end))
#     while time.time() < t_end:
#         time.sleep(returnInt(20, 25))
#         mouse.click(self.button)
#         print("Clicked in time loop")
#     #move mouse to bank
#     moveMouse(returnInt(835, 850),returnInt(660, 663))
#     time.sleep(returnInt(1, 2))


def t17ArtifactBot(self):
    mouse.click(self.button)
    print("Clicked")
    time.sleep(returnInt(2, 4))
    # move mouse to pile
    moveMouse(returnInt(784, 800),returnInt(370, 387))
    time.sleep(returnInt(1, 2))
    mouse.click(self.button)
    print("Clicked")
    time.sleep(returnInt(2, 4))
    #READJUST
    moveMouse(returnInt(704, 734),returnInt(426, 458))
    time.sleep(returnInt(1, 2))
    #click randomly for 2 min
    t_end = time.time() + returnInt(45, 60) * returnInt(1, 2)
    print("Wait time: " + str(t_end))
    while time.time() < t_end:
        time.sleep(returnInt(20, 25))
        mouse.click(self.button)
        print("Clicked in time loop")
    #move mouse to bank
    moveMouse(returnInt(580, 599),returnInt(543, 558))
    time.sleep(returnInt(1, 2))

def t100ArtifactBot(self):
    mouse.click(self.button)
    print("Clicked")
    time.sleep(returnInt(3, 5))
    # move mouse to pile
    moveMouse(returnInt(738, 767),returnInt(329, 354))
    time.sleep(returnInt(3, 5))
    mouse.click(self.button)
    print("Clicked")
    time.sleep(returnInt(2, 4))
    #READJUST
    moveMouse(returnInt(742, 766),returnInt(466, 488))
    time.sleep(returnInt(1, 2))
    #click randomly for 2 min
    t_end = time.time() + returnInt(45, 60) * returnInt(1, 2)
    print("Wait time: " + str(t_end))
    while time.time() < t_end:
        time.sleep(returnInt(20, 25))
        mouse.click(self.button)
        print("Clicked in time loop")
    #move mouse to bank
    moveMouse(returnInt(756, 786),returnInt(589, 606))
    time.sleep(returnInt(1, 2))

def t102ArtifactBot(self):
    mouse.click(self.button)
    print("Clicked")
    time.sleep(returnInt(3, 4))
    # move mouse to pile
    moveMouse(returnInt(844, 863),returnInt(535, 556))
    time.sleep(returnInt(2, 4))
    mouse.click(self.button)
    print("Clicked")
    time.sleep(returnInt(8, 10))
    #READJUST
    moveMouse(returnInt(740, 766),returnInt(465, 485))
    time.sleep(returnInt(1, 2))
    #click randomly for 2 min
    t_end = time.time() + returnInt(55, 60) * returnInt(1, 2)
    print("Wait time: " + str(t_end))
    while time.time() < t_end:
        time.sleep(returnInt(20, 25))
        mouse.click(self.button)
        print("Clicked in time loop")
    #move mouse to bank
    moveMouse(returnInt(596, 612),returnInt(427, 440))
    time.sleep(returnInt(1, 2))


def t101ArtifactBot(self):
    mouse.click(self.button)
    print("Clicked")
    time.sleep(returnInt(8, 10))
    # move mouse to pile
    moveMouse(returnInt(593, 616), returnInt(369, 388))
    time.sleep(returnInt(2, 4))
    mouse.click(self.button)
    print("Clicked")
    time.sleep(returnInt(8, 10))
    # READJUST
    moveMouse(returnInt(712, 733), returnInt(495, 514))
    time.sleep(returnInt(1, 2))
    # click randomly for 2 min
    t_end = time.time() + returnInt(55, 60) * returnInt(1, 2)
    print("Wait time: " + str(t_end))
    while time.time() < t_end:
        time.sleep(returnInt(20, 25))
        mouse.click(self.button)
        print("Clicked in time loop")
    # move mouse to bank
    moveMouse(returnInt(835, 850), returnInt(660, 663))
    time.sleep(returnInt(1, 2))

def prayFromTable(self):
    #go to threshold
    time.sleep(returnInt(1, 2))
    keyboard.press('t')
    time.sleep(returnInt(1, 2))
    keyboard.release('t')
    time.sleep(returnInt(2, 4))
    keyboard.press('t')
    time.sleep(returnInt(1, 2))
    keyboard.release('t')
    time.sleep(returnInt(1, 2))
    #move mouse to door square
    moveMouse(returnInt(1040, 1054), returnInt(519, 530))
    time.sleep(returnInt(1, 2))
    mouse.click(self.button)
    print("Clicked")
    time.sleep(returnInt(5, 7))

    #move to alter
    moveMouse(returnInt(1138, 1173), returnInt(526, 550))
    time.sleep(returnInt(1, 2))
    mouse.click(self.button)
    time.sleep(returnInt(6, 7))
    #move to barrier
    moveMouse(returnInt(270, 299), returnInt(445, 466))
    time.sleep(returnInt(1, 2))
    mouse.click(self.button)
    time.sleep(returnInt(7, 8))
    #move deposit box
    moveMouse(returnInt(1136, 1140), returnInt(56, 59))
    time.sleep(returnInt(1, 2))
    mouse.click(self.button)
    time.sleep(returnInt(10, 12))

def t107ArtifactBot(self):
    #click table
    mouse.click(self.button)
    print("Clicked")
    time.sleep(returnInt(2, 4))
    #confirm leave
    keyboard.press('1')
    keyboard.release('1')
    time.sleep(returnInt(3, 4))

    #25% chance to refill prayer
    if(returnInt(0,1001)> 750):
        prayFromTable(self)
    else:
        #move mouse to deposit box
        moveMouse(returnInt(1400, 1425), returnInt(663, 675))


        #keyboard.press('e')
        #keyboard.release('e')


        time.sleep(returnInt(2, 4))
        mouse.click(self.button)
        print("Clicked")
        #run there
        time.sleep(returnInt(11, 12))

    #move mouse to war table portal
    moveMouse(returnInt(35, 59), returnInt(246, 263))
    time.sleep(returnInt(2, 4))
    mouse.click(self.button)
    print("Clicked")
    #run back
    time.sleep(returnInt(11, 12))


    #move mouse to pile
    moveMouse(returnInt(843, 867), returnInt(267, 296))
    time.sleep(returnInt(2, 4))
    mouse.click(self.button)
    print("Clicked")
    #run to pile
    time.sleep(returnInt(4, 6))

    #readjust
    moveMouse(returnInt(707, 731), returnInt(432, 459))

    # click randomly for 2 min
    t_end = time.time() + returnInt(50, 70) * 2
    print("Wait time: " + str(t_end))
    while time.time() < t_end:
        time.sleep(returnInt(20, 25))
        mouse.click(self.button)
        print("Clicked in time loop")
    # move mouse to table
    moveMouse(returnInt(613, 648), returnInt(531, 557))
    time.sleep(returnInt(1, 2))

def t114ArtifactBot(self):
    #click table
    mouse.click(self.button)
    print("Clicked")
    time.sleep(returnInt(6, 7))
    #confirm leave
    keyboard.press('1')
    keyboard.release('1')
    time.sleep(returnInt(3, 4))

    #25% chance to refill prayer
    if(returnInt(0,1001)> 750):
        prayFromTable(self)
    else:
        #move mouse to deposit box
        moveMouse(returnInt(1400, 1425), returnInt(663, 675))
        time.sleep(returnInt(2, 4))
        mouse.click(self.button)
        print("Clicked")
        #run there
        time.sleep(returnInt(11, 12))

    #move mouse to war table portal
    moveMouse(returnInt(35, 59), returnInt(250, 263))
    time.sleep(returnInt(2, 4))
    mouse.click(self.button)
    print("Clicked")
    #run back
    time.sleep(returnInt(11, 12))


    #move mouse to pile
    time.sleep(returnInt(1, 2))
    moveMouse(returnInt(764, 792), returnInt(707, 729))

    time.sleep(returnInt(1, 2))
    mouse.click(self.button)
    print("Clicked")
    #run to pile
    time.sleep(returnInt(5, 7))

    #readjust
    moveMouse(returnInt(743, 765), returnInt(462, 488))

    # click randomly for 2 min
    t_end = time.time() + returnInt(50, 70) * 2
    print("Wait time: " + str(t_end))
    while time.time() < t_end:
        time.sleep(returnInt(5, 20))
        mouse.click(self.button)
        print("Clicked in time loop")
    # move mouse to table
    moveMouse(returnInt(688, 727), returnInt(115, 141))
    time.sleep(returnInt(1, 2))

def t118ArtifactBot(self):
    #click table
    mouse.click(self.button)
    print("Clicked")
    time.sleep(returnInt(1 ,2))
    #confirm leave
    keyboard.press('1')
    keyboard.release('1')
    time.sleep(returnInt(3, 4))

    #25% chance to refill prayer
    if(returnInt(0,1001)> 750):
        prayFromTable(self)
    else:
        #move mouse to deposit box
        moveMouse(returnInt(1400, 1425), returnInt(663, 675))
        time.sleep(returnInt(2, 4))
        mouse.click(self.button)
        print("Clicked")
        #run there
        time.sleep(returnInt(11, 12))

    #move mouse to war table portal
    moveMouse(returnInt(14, 44), returnInt(186, 206))
    time.sleep(returnInt(2, 4))
    mouse.click(self.button)
    print("Clicked")
    #run back
    time.sleep(returnInt(11, 12))


    #move mouse to pile
    time.sleep(returnInt(1, 2))
    moveMouse(returnInt(681, 694), returnInt(471, 487))

    time.sleep(returnInt(1, 2))
    mouse.click(self.button)
    print("Clicked")
    #run to pile
    time.sleep(returnInt(1,2))

    #readjust
    #moveMouse(returnInt(743, 765), returnInt(462, 488))

    # click randomly for 2 min
    t_end = time.time() + returnInt(50, 55) * 2
    print("Wait time: " + str(t_end))
    while time.time() < t_end:
        time.sleep(returnInt(5, 20))
        mouse.click(self.button)
        print("Clicked in time loop")
    # move mouse to table
    moveMouse(returnInt(705, 722), returnInt(422, 435))
    time.sleep(returnInt(1, 2))

def capeBoost(self):
    #move mouse to cape spot
    moveMouse(returnInt(195, 211),returnInt(873, 888))
    time.sleep(returnInt(1,2))
    #right click
    mouse.click(self.button.right)
    time.sleep(returnInt(1,2))
    #move mouse to boost then click
    moveMouse(returnInt(50, 296),returnInt(835, 848))
    time.sleep(returnInt(1,2))
    mouse.click(self.button)



def t115ArtifactBot(self):
    #click hole
    mouse.click(self.button)
    print("Clicked")
    time.sleep(returnInt(7, 8))
    #move mouse to lift then click
    moveMouse(returnInt(457, 510),returnInt(570, 606))
    time.sleep(returnInt(1,2))
    mouse.click(self.button)
    time.sleep(returnInt(9,10))

    #move mouse to bank then click
    moveMouse(returnInt(661, 680),returnInt(831, 840))
    time.sleep(returnInt(1,2))
    mouse.click(self.button)
    time.sleep(returnInt(11,12))

    #grab preset 2
    keyboard.press('3')
    keyboard.release('3')
    time.sleep(returnInt(1,2))

    #move mouse to lift then click
    moveMouse(returnInt(637, 664),returnInt(122, 135))
    time.sleep(returnInt(1,2))
    mouse.click(self.button)
    time.sleep(returnInt(11,12))

    #Go to location 1
    keyboard.press('1')
    keyboard.release('1')
    time.sleep(returnInt(3,4))

    #move mouse to hole then click
    moveMouse(returnInt(860, 870),returnInt(321, 333))
    time.sleep(returnInt(1,2))
    mouse.click(self.button)
    time.sleep(returnInt(9,10))

    #move mouse to pile then click
    moveMouse(returnInt(551, 567),returnInt(235, 250))
    time.sleep(returnInt(1,2))
    mouse.click(self.button)
    time.sleep(returnInt(7, 8))

    #readjust to pile then click
    moveMouse(returnInt(709, 727),returnInt(432, 449))
    time.sleep(returnInt(1,2))
    mouse.click(self.button)

    #loop for a good sec (2min 24 sec)
    t_end = time.time() + returnInt(65, 75) * 2
    print("Wait time: " + str(t_end))
    while time.time() < t_end:
        #drop soil
        for x in range(5):
            keyboard.press('m')
            keyboard.release('m')
        time.sleep(returnInt(5, 20))
        mouse.click(self.button)
        print("Clicked in time loop")

    # move mouse to hole
    moveMouse(returnInt(883, 902), returnInt(723, 729))
    time.sleep(returnInt(1, 2))


def t115ArtifactBotWTele(self):
    #click teleport keybind
    keyboard.press(Key.shift)
    keyboard.press('p')
    keyboard.release('p')
    keyboard.release(Key.shift)
    time.sleep(returnInt(1,2))

    # click 6 (Warforge tele)
    keyboard.press('6')
    keyboard.release('6')
    time.sleep(returnInt(3,5))

    #move mouse to bank then click
    moveMouse(returnInt(813, 824),returnInt(376, 383))
    time.sleep(returnInt(1,2))
    mouse.click(self.button)
    time.sleep(returnInt(4,5))

    #bank all
    keyboard.press('3')
    keyboard.release('3')
    time.sleep(returnInt(1,2))

    #move mouse to lift then click
    moveMouse(returnInt(637, 664),returnInt(122, 135))
    time.sleep(returnInt(1,2))
    mouse.click(self.button)
    time.sleep(returnInt(11,12))

    #Go to location 1
    keyboard.press('1')
    keyboard.release('1')
    time.sleep(returnInt(3,4))

    #move mouse to hole then click
    moveMouse(returnInt(860, 870),returnInt(321, 333))
    time.sleep(returnInt(1,2))
    mouse.click(self.button)
    time.sleep(returnInt(9,10))

    #move mouse to pile then click
    moveMouse(returnInt(551, 567),returnInt(235, 250))
    time.sleep(returnInt(1,2))
    mouse.click(self.button)
    time.sleep(returnInt(7, 8))

    #readjust to pile then click
    moveMouse(returnInt(709, 727),returnInt(432, 449))
    time.sleep(returnInt(1,2))
    mouse.click(self.button)

    #loop for a good sec (2min 24 sec)
    t_end = time.time() + returnInt(60, 65) * 2
    print("Wait time: " + str(t_end))
    while time.time() < t_end:
        #drop soil
        for x in range(returnInt(5, 10)):
            keyboard.press('p')
            keyboard.release('p')
        time.sleep(returnInt(5, 20))
        mouse.click(self.button)
        print("Clicked in time loop")

    # move mouse to hole
    #moveMouse(returnInt(883, 902), returnInt(723, 729))
    #Click to remove interface in case where loot was grabbed
    mouse.click(self.button)

    time.sleep(returnInt(1, 2))


def t119ArtifactBotWTele(self):
    #click teleport keybind
    keyboard.press(Key.shift)
    keyboard.press('p')
    keyboard.release('p')
    keyboard.release(Key.shift)
    time.sleep(returnInt(1,2))

    # click 6 (Warforge tele)
    keyboard.press('6')
    keyboard.release('6')
    time.sleep(returnInt(3,5))

    #move mouse to bank then click
    moveMouse(returnInt(813, 824),returnInt(376, 383))
    time.sleep(returnInt(1,2))
    mouse.click(self.button)
    time.sleep(returnInt(4,5))

    #bank all
    keyboard.press('3')
    keyboard.release('3')
    time.sleep(returnInt(1,2))

    #move mouse to lift then click
    moveMouse(returnInt(637, 664),returnInt(122, 135))
    time.sleep(returnInt(1,2))
    mouse.click(self.button)
    time.sleep(returnInt(11,12))

    #Go to location 3
    keyboard.press('3')
    keyboard.release('3')
    time.sleep(returnInt(3,4))

    #move mouse to door then click
    moveMouse(returnInt(692, 746),returnInt(517, 537))
    time.sleep(returnInt(1,2))
    mouse.click(self.button)
    time.sleep(returnInt(3,4))

    #move mouse to pile then click
    moveMouse(returnInt(806, 826),returnInt(499, 519))
    time.sleep(returnInt(1,2))
    mouse.click(self.button)
    time.sleep(returnInt(2,3))

    #readjust to pile then click
    moveMouse(returnInt(744, 752),returnInt(465, 487))
    time.sleep(returnInt(1,2))
    mouse.click(self.button)

    #loop for a good sec (2min 24 sec)
    t_end = time.time() + returnInt(60, 65) * 2
    print("Wait time: " + str(t_end))
    while time.time() < t_end:
        #drop soil
        for x in range(returnInt(5, 10)):
            keyboard.press('p')
            keyboard.release('p')
        time.sleep(returnInt(5, 20))
        mouse.click(self.button)
        print("Clicked in time loop")

    #Click to remove interface in case where loot was grabbed
    mouse.click(self.button)

    time.sleep(returnInt(1, 2))


def dragonkinBot(self):
    mouse.click(self.button)
    print("Clicked")
    time.sleep(returnInt(4,7))
    #move mouse to pile
    moveMouse(returnInt(875, 905),returnInt(400, 420))
    time.sleep(returnInt(1, 2))
    mouse.click(self.button)
    print("Clicked")
    #READJUST
    moveMouse(returnInt(735, 775),returnInt(474, 500))
    time.sleep(returnInt(1, 2))
    #click randomly for 2 min
    t_end = time.time() + returnInt(45, 60) * returnInt(1, 2)
    print("Wait time: " + str(t_end))
    while time.time() < t_end:
        time.sleep(returnInt(10, 15))
        mouse.click(self.button)
        print("Clicked in time loop")
    #move mouse to bank
    moveMouse(returnInt(566, 598),returnInt(556, 573))
    time.sleep(returnInt(1, 2))

def t5ArtifactBot(self):
    # click bank
    mouse.click(self.button)
    print("Clicked")
    # 7 to 9 second wait randomly
    time.sleep(returnInt(10, 11))
    keyboard.press('3')
    keyboard.release('3')
    print("Pressed 3")
    time.sleep(returnInt(1, 2))
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    print("Pressed escape")
    time.sleep(returnInt(1, 2))
    #move mouse back to pile
    moveMouse(returnInt(1095, 1130),returnInt(700, 735))
    time.sleep(returnInt(1, 2))
    mouse.click(self.button)
    time.sleep(returnInt(10, 11))
    moveMouse(returnInt(700, 740),returnInt(495, 530))
    time.sleep(returnInt(1, 2))
    mouse.click(self.button)
    #click randomly for 2 min
    t_end = time.time() + returnInt(45,60) * returnInt(1,2)
    print("Wait time: " + str(t_end))
    while time.time() < t_end:
        time.sleep(returnInt(10,15))
        mouse.click(self.button)
        print("Clicked in time loop")
        tenPercentChanceOfE()

    moveMouse(returnInt(155, 181),returnInt(137, 150),)
    time.sleep(returnInt(1, 2))

def fishingBot(self):
    #click bank
    mouse.click(self.button)
    print("Clicked")
    #7 to 9 second wait randomly
    time.sleep(returnInt(11, 12))

    #click inventory button (same spot or "3" make random)
    keyboard.press('3')
    keyboard.release('3')
    print("Pressed 3")
    time.sleep(returnInt(1, 2))

    #move mouse to swarm (left)
    moveMouse(returnInt(227, 250),returnInt(445, 465))
    print("Moved")
    time.sleep(returnInt(1, 2))
    #click
    mouse.click(self.button)
    print("Clicked")
    #7 to 9 second wait randomly
    time.sleep(returnInt(10, 11))

    #adjust mouse to swarm (new spot)
    moveMouse(returnInt(737, 773), returnInt(481, 503))
    print("Moved")
    #click randomly for 6 min
    t_end = time.time() + returnInt(55,60) * returnInt(3,4)
    print("Wait time: " + str(t_end))
    while time.time() < t_end:
        time.sleep(returnInt(10, 30))
        mouse.click(self.button)
        print("Clicked in time loop")

    #move mouse to bank
    moveMouse(returnInt(1131,1163),returnInt(409,435))
    print("Moved")

    time.sleep(returnInt(1, 2))

def agilityAutoClickerAndEat(self):
    mouse.click(self.button)
    delay = np.random.randint(2  , 4)
    time.sleep(delay)
    keyboard.press('e')
    keyboard.release('e')

def clickPresetClickToolTipSpace(self):
    #grab preset
    grabPresetOne(self)
    actionBarE()
    time.sleep(np.random.randint(15,25))

def buttonPress(self):
    time.sleep( 1)
    keyboard.press('m')
    keyboard.release('m')

def randomAutoClickerWithButtonPress(self):
    keyboard.press('e')
    keyboard.release('e')
    time.sleep( np.random.randint(1,4))
    mouse.click(self.button)
    #keyboard.press(Key.space)
    #keyboard.release(Key.space)
    time.sleep( np.random.randint(15,35))

def fletchingAutoClicker(self):
    grabPresetOne(self)
    actionBarE()
    #wait a random delay
    delay = np.random.randint(12,20)
    time.sleep(delay)

def firemakingAutoClicker(self):
    grabPresetOne(self)
    actionBarE()
    time.sleep(np.random.randint(1,4))
    mouse.click(self.button)
    #wait a random delay
    delay = np.random.randint(60,90)
    time.sleep(delay)

def minMaxDelay():
    # one swing
    minDelay = 2.4
    # 4 swings and .1 seconds
    maxDelay = 9.7
    sleep(np.random.randint(minDelay, maxDelay))

def buryInv(self):
    grabPresetOne(self)
    for x in range(1,28):
        keyboard.press('e')
        keyboard.release('e')
        sleep(0.6)


def miningAutoClicker(self):
    tenPercentChanceOfE()
    time.sleep(1)
    mouse.click(self.button)
    minMaxDelay()


def miningAutoClickerWithDrop(self):
    minMaxDelay()
    # 10% chance of storing ore
    randPercent = np.random.randint(1, 101)
    if randPercent > 80:
        for x in range(np.random.randint(15, 26)):
            keyboard.press('e')
            keyboard.release('e')
            sleep(0.05)

    time.sleep(1)
    mouse.click(self.button)
    minMaxDelay()

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
    time.sleep(2)
    #mouse.click(self.button)
    #time.sleep(1)
    print('space=  clicked')
    keyboard.press(Key.space)
    keyboard.release(Key.space)

    time.sleep(delay)

def heatAndSmith(self):
    #click kiln
    mouse.click(self.button)
    #wait a sec
    time.sleep(np.random.randint(4, 5))

    #move mouse to anvil
    moveMouse(returnInt(377, 428),returnInt(410, 459))
    time.sleep(np.random.randint(1,2))
    # Click
    mouse.click(self.button)

    #wait
    # random time intween
    delay = np.random.randint(20, 30)
    # wait a sec then click then space
    #mouse.click(self.button)
    #time.sleep(1)

    time.sleep(delay)

    #MOVE MOUST TO FORGE
    moveMouse(returnInt(711, 728),returnInt(227, 245))

    time.sleep(np.random.randint(1,2))

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
