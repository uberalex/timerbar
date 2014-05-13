#!/usr/bin/python

# -*- coding: utf-8 -*-

""" Simple OSX Bar with Countdown Timer """

import os
import sys
import rumps # uses the rumps library from http://github.com/tito/rumps
import parsedatetime # natural language expressions for parsing https://github.com/bear/parsedatetime
from datetime import datetime, timedelta # temporal objects

__author__ = "Alexander O'Connor <oconnoat@gmail.com>"
__copyright__ = "Copyright 2014, Alexander O'Connor <oconnoat@gmail.com>"
__credits__ = ["Alexander O'Connor <oconnoat@gmail.com>"]
__license__ = "Copyright"
__version__ = "1.5"
__email__ = "Alexander O'Connor <oconnoat@gmail.com>"
__status__ = "Release"

target_time = None
notify = False

@rumps.timer(1)
def tick(sender):
    """ Called automatically every second """
    global target_time
    global notify
    global app

    if target_time:
        timeleft = target_time - datetime.now()

        app.title = "(%02d:%02d:%02d)" % (timeleft.total_seconds()//3600,(timeleft.seconds % 3600)//60, timeleft.seconds%60)

        if (timeleft.total_seconds() < 1) and notify:
            app.title = "Done!"
            rumps.notification(title="Countdown Done!", subtitle="TimerBar", sound=True, message="The Timer has Completed!")
            notify = False
            target_time = None

def startcount(target):
    """start a counter for num mins"""
    global target_time
    global notify

    print 'target: %s' % target


    target_time = target
    notify = True

    rumps.notification(title="Countdown has begun.", subtitle="TimerBar", message="Ends at %s"%target)

@rumps.clicked("Start Timer", "5:00")
def fivemincall(sender):
    """ start a counter for five mins"""
    target = datetime.now() + timedelta(minutes=5)
    startcount(target)

@rumps.clicked("Start Timer", "10:00")
def tenmincall(sender):
    """ start a counter for ten mins"""
    target = datetime.now() + timedelta(minutes=10)
    startcount(target)

@rumps.clicked("Start Timer", "15:00")
def fifteenmincall(sender):
    """ start a counter for fifteen mins"""
    target = datetime.now() + timedelta(minutes=15)
    startcount(target)

@rumps.clicked("Start Timer", "25:00")
def fifteenmincall(sender):
    """ start a counter for twenty-five mins"""
    target = datetime.now() + timedelta(minutes=25)
    startcount(target)

@rumps.clicked("Start Timer", "Custom...")
def customcall(sender):
    response = rumps.Window("Enters number of minutes").run()
    p = parsedatetime.Calendar(parsedatetime.Constants())

    print response
    if response.clicked:
        try:
            print(datetime(*p.parse(response.text)[0][:6]))
            startcount(datetime(*p.parse(response.text)[0][:6]))
        except Exception, e:
            print e

@rumps.clicked("Stop")
def stoptimer(sender):
    global target_time
    """Set the time left to zero"""
    target_time = datetime.now()

@rumps.clicked("About TimerBar")
def aboutButton(sender):
    rumps.Window(title="TimerBar, by Alexander O'Connor", message="Thanks for using TimerBar! Please feel free to send feedback on twitter to @uberalex", default_text="To use it, just run the app and select the time limit you would like to count down to. You can click the stop button any time.\n\nThe Custom... box will take a variety of input such as '5 minutes' or 'at 4pm' or 'tomorrow' (see https://code.google.com/p/parsedatetime/ for more examples).").run()

#App Definition
app = rumps.App("Timebar", title="(00:00:00)", icon="data/rooster-128.png")

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
