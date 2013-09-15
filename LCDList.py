#!/usr/bin/python
"""
Created by Foamyguy

To use: Edit the entries in the actionList.
The first column are the names that appear
on the LCD screen. The second column are the
names of python files that you want to run
when the user selects that item in the list.

This is free and unencumbered software released into the public domain.
See the UNLICENCE File for more details.
"""

actionList = [("Have fun", "have_fun.py"),
              ("Help People", "help_people.py"),
              ("Teach People", "teach_people.py"),
              ("Always Learn", "always_learn.py"),
              ("Turn Off", "turn_off.py")]

from time import sleep
import os
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

lcd = Adafruit_CharLCDPlate(busnum = 1)
currentIndex = 0
currentChoice = 0
       
def drawScreen():
    lcd.clear()
    lcd.backlight(lcd.ON)
    lcd.message(">%s\n %s" % (actionList[currentIndex % len(actionList)][0], actionList[(currentIndex+1) % len(actionList)][0]))




              
drawScreen()

while True:

    if lcd.buttonPressed(lcd.RIGHT):
        currentIndex += 1
        curChoice = currentIndex % len(actionList)
        print "curChoice = %s" % curChoice
        
        drawScreen()
        sleep(.5)
    if lcd.buttonPressed(lcd.LEFT):
        currentIndex -= 1
        curChoice = currentIndex % len(actionList)
        print "curChoice = %s" % curChoice
        drawScreen()
        sleep(.5)
    if lcd.buttonPressed(lcd.SELECT):
        curChoice = currentIndex % len(actionList)
        print "curChoice = %s" % curChoice
        os.system("python /home/pi/AutoLCD/%s" % actionList[curChoice][1])
        drawScreen()

    