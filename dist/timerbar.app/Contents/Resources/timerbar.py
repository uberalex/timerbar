#!/usr/bin/python

# -*- coding: utf-8 -*-

""" Simple OSX Bar with Countdown Timer """

import os
import sys
import rumps # uses the rumps library from http://github.com/tito/rumps

__author__ = "Alexander O'Connor <oconnoat@gmail.com>"
__copyright__ = "Copyright 2012, Alexander O'Connor <oconnoat@gmail.com>"
__credits__ = ["Alexander O'Connor <oconnoat@gmail.com>"]
__license__ = "Copyright"
__version__ = "0.1"
__email__ = "Alexander O'Connor <oconnoat@gmail.com>"
__status__ = "Prototype"

timeleft = 0
elapsed = 0
notify = False


@rumps.timer(1)
def tick(sender):
    """ Called authomatically every second """
    global elapsed
    global timeleft
    global notify
    global app

    if timeleft > 0:
        timeleft -= 1
        elapsed += 1
        app.title = 'TimerBar (%s:%s)' %  (timeleft / 60, timeleft % 60)
    if timeleft == 0 and notify:
        timeleft = 0
        app.title = 'TimerBar (Done!)'
        rumps.notification(title="Countdown Done!", subtitle="TimerBar", message="The Timer has Completed!\nSeconds elapsed:"+str(elapsed)+"s.")
        notify = False

def startcount(mins):
    """start a counter for num mins"""
    global timeleft
    global notify
    timeleft = mins * 60 #convert to seconds
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

@rumps.clicked("Stop")
def stoptimer(sender):
    global timeleft
    """Set the time left to zero"""
    timeleft = 0

#App Definition
app = rumps.App("Timebar", title="TimeBar")

#The Menu
app.menu = [
        rumps.MenuItem('TimerBar'),
        None,
        {'Start Timer':
        [rumps.MenuItem("5:00"),
         rumps.MenuItem("10:00"),
         rumps.MenuItem("15:00")]},
        None,
        rumps.MenuItem("Stop")
]




if __name__ == '__main__':
    app.run()
