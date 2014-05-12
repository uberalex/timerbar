#!/usr/bin/python

# -*- coding: utf-8 -*-

""" Simple OSX Bar with Countdown Timer """

import os
import sys
import rumps # uses the rumps library from http://github.com/tito/rumps
import time

__author__ = "Alexander O'Connor <oconnoat@gmail.com>"
__copyright__ = "Copyright 2012, Alexander O'Connor <oconnoat@gmail.com>"
__credits__ = ["Alexander O'Connor <oconnoat@gmail.com>"]
__license__ = "Copyright"
__version__ = "1.4"
__email__ = "Alexander O'Connor <oconnoat@gmail.com>"
__status__ = "Release"

timeleft = 0
elapsed = 0
notify = False
start_time = 0


@rumps.timer(1)
def tick(sender):
    """ Called automatically every second """
    global elapsed
    global start_time
    global timeleft
    global notify
    global app

    elapsed = time.time() - start_time

    if timeleft > elapsed :
        app.title = "(%02d:%02d)" %  ((timeleft - elapsed) / 60, (timeleft - elapsed) % 60)

    if (timeleft - elapsed) < 1 and notify:
        app.title = "Done!"
        rumps.notification(title="Countdown Done!", subtitle="TimerBar", sound=True, message="The Timer has Completed!\nSeconds elapsed:"+str(elapsed)+"s.")
        notify = False

def startcount(mins):
    """start a counter for num mins"""
    global timeleft
    global notify
    global start_time
    timeleft = mins * 60 #convert to seconds
    start_time = time.time()

    notify = True
    rumps.notification(title="Countdown has begun.", subtitle="TimerBar", message="Duration: "+str(mins)+"min.\nTime Left: "+str(timeleft)+"s.\nA Notification will be sent when the timer stops.")

@rumps.clicked("Start Timer", "5:00")
def fivemincall(sender):
    """ start a counter for five mins"""
    startcount(5)

@rumps.clicked("Start Timer", "10:00")
def tenmincall(sender):
    """ start a counter for ten mins"""
    startcount(10)

@rumps.clicked("Start Timer", "15:00")
def fifteenmincall(sender):
    """ start a counter for fifteen mins"""
    startcount(15)

@rumps.clicked("Start Timer", "25:00")
def fifteenmincall(sender):
    """ start a counter for twenty-five mins"""
    startcount(25)

@rumps.clicked("Start Timer", "Custom...")
def customcall(sender):
    response = rumps.Window("Enter number of minutes").run()
    if response.clicked:
        try:
            startcount(float (response.text))
        except Exception, e:
            pass

@rumps.clicked("Stop")
def stoptimer(sender):
    global timeleft
    """Set the time left to zero"""
    timeleft = 0

@rumps.clicked("About TimerBar")
def aboutButton(sender):
    rumps.Window(title="TimerBar, by Alexander O'Connor", message="Thanks for using TimerBar! Please feel free to send feedback on twitter to @uberalex", default_text="To use it, just run the app and select the time limit you would like to count down to. You can click the stop button any time.\n\nThe Custom... range will accept decimal values (so 0.5 will give a 30 second countdown).\n\nNote that it's not second-accurate.").run()

#App Definition
app = rumps.App("Timebar", title="(00:00)", icon="data/rooster-128.png")

#The Menu
app.menu = [
        rumps.MenuItem("About TimerBar"),
        None,
        [rumps.MenuItem("Start Timer",icon="data/alarm_clock-128.png", dimensions=(16,16)),
        [rumps.MenuItem("5:00"),
         rumps.MenuItem("10:00"),
         rumps.MenuItem("15:00"),
         rumps.MenuItem("25:00"),
         rumps.MenuItem("Custom...")]],
        None,
        rumps.MenuItem("Stop")
]




if __name__ == "__main__":
    app.run()
