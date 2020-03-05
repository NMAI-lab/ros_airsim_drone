#!/usr/bin/env python

# Created on Wed Feb 19 16:17:21 2020
# @author: Patrick Gavigan

import airsim
import threading

# Thread safe connector to the AirSim simulator. 
# Should be treated as a singleton.
class AirSimConnector:
    
    def __init__(self):
        self.connectToAirSim()
        self.sem = threading.Semaphore()
        
    # Use destructor to ensure safe shutdown
    def __del__(self):
        self.disconnectFromAirSim(self)        
        
    def connectToAirSim(self):
        self.client = airsim.MultirotorClient()
        self.client.confirmConnection()
        self.client.enableApiControl(True)
        self.client.armDisarm(True)
        
    def disconnectFromAirSim(self):
        self.sem.acquire()
        self.client.enableApiControl(False)
        self.client.armDisarm(False)
        self.sem.release()        
        
    def commnadTakeOff(self):
        self.sem.acquire()
        self.client.takeoffAsync().join()
        self.sem.release()
        
    def commandMoveToPositionAsync(self, x, y, z, speed):
        self.sem.acquire()
        self.client.moveToPositionAsync(x,y,z,speed).join()
        self.sem.release()
        
    def commandHover(self):
        self.sem.acquire()
        self.client.hoverAsync().join()
        self.sem.release()

    def getImuData(self):
        self.sem.acquire()
        data = self.client.getImuData()
        self.sem.release()
        return data

    def getBarometerData(self):
        self.sem.acquire()
        data = self.client.getBarometerData()
        self.sem.release()
        return data
    
    def getGpsData(self):
        self.sem.acquire()
        data = self.client.getGpsData()
        self.sem.release()
        return data
    
    def getMagnetometerData(self):
        self.sem.acquire()
        data = self.client.getMagnetometerData()
        self.sem.release()
        return data
    