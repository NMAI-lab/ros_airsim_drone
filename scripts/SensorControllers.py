#!/usr/bin/env python

# Created on Wed Feb 19 16:17:21 2020
# @author: Patrick Gavigan

from AirSimConnector import AirSimConnector
import rospy
from std_msgs.msg import String

def runImu(airSimConnector, publisher):
    # Get the data
    imu_data = airSimConnector.getImuData()
        
    # Start simple, keep it all as a string, define custom message soon
    angularVelocity = "angularVelocity("+str(imu_data.angular_velocity.x_val)+","+str(imu_data.angular_velocity.y_val)+","+str(imu_data.angular_velocity.z_val)+","+str(imu_data.time_stamp)+")"
    linearAcceleration = "linearAcceleration("+str(imu_data.linear_acceleration.x_val)+","+str(imu_data.linear_acceleration.y_val)+","+str(imu_data.linear_acceleration.z_val)+","+str(imu_data.time_stamp)+")"
    orientation = "orientation("+str(imu_data.orientation.w_val)+","+str(imu_data.orientation.x_val)+","+str(imu_data.orientation.y_val)+","+str(imu_data.orientation.z_val)+","+str(imu_data.time_stamp)+")"
        
    perception = angularVelocity + " " + linearAcceleration + " " + orientation
        
    # Publish the perception
    rospy.loginfo(perception)
    publisher.publish(perception)
    

def runSensors(airSimConnector):

    # Initialize the publuishers
    publisher = rospy.Publisher('imu', String, queue_size=10)
    
    # Set the sensor publishing frequency
    rate = rospy.Rate(1) # 1hz

    # Publishing loop
    while not rospy.is_shutdown():
        runImu(airSimConnector, publisher)
        rate.sleep()