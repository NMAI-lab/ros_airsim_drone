#!/usr/bin/env python

# Created on Wed Feb 19 16:17:21 2020
# @author   Patrick Gavigan
# @data     

import rospy
from ros_airsim_drone.msg import ImuData
from ros_airsim_drone.msg import BarometerData
from ros_airsim_drone.msg import GpsData
from ros_airsim_drone.msg import MagnetometerData

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
    
def runGPS(airSimConnector, publisher):
    # Get the data
    data = airSimConnector.getGpsData()
    
    # Prerpare the message
    message = GpsData()
    message.gnssReport.eph = data.gnss.eph
    message.gnssReport.epv = data.gnss.epv
    message.gnssReport.fixType = data.gnss.fix_type
    
    message.gnssReport.geoPoint.altitude = data.gnss.geo_point.altitude
    message.gnssReport.geoPoint.latitude = data.gnss.geo_point.latitude
    message.gnssReport.geoPoint.longitude = data.gnss.geo_point.longitude
    
    message.gnssReport.utcTime = data.gnss.time_utc
    
    message.gnssReport.velocity.x = data.gnss.velocity.x_val
    message.gnssReport.velocity.y = data.gnss.velocity.y_val
    message.gnssReport.velocity.z = data.gnss.velocity.z_val
    
    message.isValid = data.is_valid
    message.timeStamp = data.time_stamp
    
    # Publish the message
    rospy.loginfo(message)
    publisher.publish(message)
    
def runMagnetometer(airSimConnector, publisher):
    # Get the data
    data = airSimConnector.getMagnetometerData
    
    # Prepare the message
    message = MagnetometerData()
    message.fieldBody.x = data.magnetic_field_body.x_val
    message.fieldBody.y = data.magnetic_field_body.y_val
    message.fieldBody.z = data.magnetic_field_body.z_val
    
    for instance in data.magnetic_field_covatiance:
        message.covariance.append(instance)
    
    # Publish the message
    rospy.loginfo(message)
    publisher.publish(message)   

def runSensors(airSimConnector):

    # Initialize the publuishers
    imuPublisher = rospy.Publisher('droneSensor/imu', ImuData, queue_size=10)
    barometerPublisher = rospy.Publisher('droneSensor/barometer', BarometerData, queue_size=10)
    gpsPublisher = rospy.Publisher('droneSensor/gps', GpsData, queue_size=10)
    magnetometerPublisher = rospy.Publisher('droneSensor/magnetometer', MagnetometerData, queue_size=10)
    
    # Set the sensor publishing frequency
    rate = rospy.Rate(1) # 1hz

    # Publishing loop
    while not rospy.is_shutdown():
        runImu(airSimConnector, imuPublisher)
        runBarometer(airSimConnector, barometerPublisher)
        runGPS(airSimConnector, gpsPublisher)
        runMagnetometer(airSimConnector, magnetometerPublisher)
        rate.sleep()