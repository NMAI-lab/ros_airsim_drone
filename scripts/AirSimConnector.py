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
        
    def connectToAirSim(self):
        self.client = airsim.MultirotorClient()
        self.client.confirmConnection()
        self.client.enableApiControl(True)
        self.client.armDisarm(True)
        
    def sendTakeOff(self):
        self.sem.acquire()
        self.client.takeoffAsync().join()
        self.sem.release()

    def getImuData(self):
        self.sem.acquire()
        imuData = self.client.getImuData()
        self.sem.release()
        return imuData
        