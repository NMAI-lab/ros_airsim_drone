#!/usr/bin/env python

# Created on Wed Feb 19 16:17:21 2020
# @author: Patrick Gavigan

from AirSimConnector import AirSimConnector
from ActuatorControllers import runActuators
from SensorControllers import runSensors

import rospy
from std_msgs.msg import String


def airSimRos():
    airSimConnector = AirSimConnector()
    rospy.init_node('AirSimDrone', anonymous=True)
    runActuators(airSimConnector)
    runSensors(airSimConnector)    

if __name__ == '__main__':
    try:
        airSimRos()
    except rospy.ROSInterruptException:
        pass