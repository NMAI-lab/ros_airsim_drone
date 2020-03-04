#!/usr/bin/env python

# Created on Wed Feb 19 16:17:21 2020
# @author   Patrick Gavigan
# @data     

import rospy
from ros_airsim_drone.msg import ImuData
from ros_airsim_drone.msg import BarometerData

def runImu(airSimConnector, publisher):
    # Get the data
    data = airSimConnector.getImuData()
    
    # Prepare the message
    message = ImuData()
    message.angularVelocity.x = data.angular_velocity.x_val
    message.angularVelocity.y = data.angular_velocity.y_val
    message.angularVelocity.z = data.angular_velocity.z_val
    
    message.linearAcceleration.x = data.linear_acceleration.x_val
    message.linearAcceleration.y = data.linear_acceleration.y_val
    message.linearAcceleration.z = data.linear_acceleration.z_val
    
    message.orientation.w = data.orientation.w_val
    message.orientation.x = data.orientation.x_val
    message.orientation.y = data.orientation.y_val
    message.orientation.z = data.orientation.z_val
    
    message.timeStamp = data.time_stamp      
   
    # Publish the message
    rospy.loginfo(message)
    publisher.publish(message)
    
def runBarometer(airSimConnector, publisher):
    # Get the data
    data = airSimConnector.getBarometerData()
    
    # Prepare the message
    message = BarometerData()
    message.altitude = data.altitude
    message.pressure = data.pressure
    message.qnh = data.qnh
    message.timeStamp = data.time_stamp
    
    # Publish the message
    rospy.loginfo(message)
    publisher.publish(message)
    
    

def runSensors(airSimConnector):

    # Initialize the publuishers
    imuPublisher = rospy.Publisher('imu', ImuData, queue_size=10)
    barometerPublisher = rospy.Publisher('barometer', BarometerData, queue_size=10)
    
    # Set the sensor publishing frequency
    rate = rospy.Rate(1) # 1hz

    # Publishing loop
    while not rospy.is_shutdown():
        runImu(airSimConnector, imuPublisher)
        runBarometer(airSimConnector, barometerPublisher)
        rate.sleep()