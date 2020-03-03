#!/usr/bin/env python

# Created on Wed Feb 19 16:17:21 2020
# @author: Patrick Gavigan

#from AirSimConnector import AirSimConnector
import rospy
from std_msgs.msg import String
from ros_airsim_drone.msg import ImuData

def runImu(airSimConnector, publisher):
    # Get the data
    data = airSimConnector.getImuData()
    
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
        
    # Start simple, keep it all as a string, define custom message soon
#    angularVelocity = "angularVelocity("+str(imu_data.angular_velocity.x_val)+","+str(imu_data.angular_velocity.y_val)+","+str(imu_data.angular_velocity.z_val)+","+str(imu_data.time_stamp)+")"
#    linearAcceleration = "linearAcceleration("+str(imu_data.linear_acceleration.x_val)+","+str(imu_data.linear_acceleration.y_val)+","+str(imu_data.linear_acceleration.z_val)+","+str(imu_data.time_stamp)+")"
#    orientation = "orientation("+str(imu_data.orientation.w_val)+","+str(imu_data.orientation.x_val)+","+str(imu_data.orientation.y_val)+","+str(imu_data.orientation.z_val)+","+str(imu_data.time_stamp)+")"
        
#    perception = angularVelocity + " " + linearAcceleration + " " + orientation
        
    # Publish the perception
#    rospy.loginfo(perception)
#    publisher.publish(perception)
    
    # Publish the message
    rospy.loginfo(message)
    publisher.publish(message)
    

def runSensors(airSimConnector):

    # Initialize the publuishers
    publisher = rospy.Publisher('imu', String, queue_size=10)
    
    # Set the sensor publishing frequency
    rate = rospy.Rate(1) # 1hz

    # Publishing loop
    while not rospy.is_shutdown():
        runImu(airSimConnector, publisher)
        rate.sleep()