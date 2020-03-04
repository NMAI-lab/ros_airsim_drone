#!/usr/bin/env python

# Created on Wed Feb 19 16:17:21 2020
# @author: Patrick Gavigan

from AirSimConnector import AirSimConnector

import rospy
from std_msgs.msg import String

def takeOffCommand(data, airSimConnector):
    # No matter what you receive, takeoff
    airSimConnector.sendTakeOff()


def runActuators(airSimConnector):
    rospy.Subscriber('takeOffCommand', String, takeOffCommand, airSimConnector)