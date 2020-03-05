#!/usr/bin/env python

# Created on Wed Feb 19 16:17:21 2020
# @author: Patrick Gavigan

import rospy
from std_msgs.msg import String

def commnadTakeOff(data, airSimConnector):
    # No matter what you receive, takeoff
    airSimConnector.commnadTakeOff()

def commandHover(data, airSimConnector):
    # No matter what you receive, hover
    airSimConnector.commandHover()
    
def commandMoveToPosition(data, airSimConnector):
    airSimConnector.commandMoveToPositionAsync(data.location.x, data.location.y, data.location.z, data.speed)

def runActuators(airSimConnector):
    rospy.Subscriber('droneCommnad/TakeOff', String, commnadTakeOff, airSimConnector)
    rospy.Subscriber('droneCommnad/Hover', String, commandHover, airSimConnector)
    rospy.Subscriber('droneCommnad/MoveToPosition', String, commandMoveToPosition, airSimConnector)