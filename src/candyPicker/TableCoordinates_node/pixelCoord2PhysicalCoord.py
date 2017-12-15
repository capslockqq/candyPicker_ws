#!/usr/bin/env python
import math
class pixelCoord2PhysicalCoord():
    def __init__(self, refCoordinates):
        self.focalLength = 3.15*(math.pow(10, -3))
        self.Z = 0.932
        self.Sx = (2.550*(math.pow(10, -3)))/640
        self.Sy = (1.910*(math.pow(10, -3)))/480
        self.refx = refCoordinates[0]
        self.refy = refCoordinates[1]
    
    def pixel2Metric(self, coordinates):
        delta_r = self.refx - coordinates[0]
        delta_c = self.refy - coordinates[1] - 40
        delta_x = (self.Z*delta_r*self.Sx)/self.focalLength
        delta_y = (self.Z*delta_c*self.Sy)/self.focalLength
        
        delta_rDes = self.refx - coordinates[2]
        delta_cDes = self.refy - coordinates[3] 
        delta_xDes = (self.Z*delta_rDes*self.Sx)/self.focalLength
        delta_yDes = (self.Z*delta_cDes*self.Sy)/self.focalLength
        
        
        return delta_x, delta_y+0.2,delta_xDes,delta_yDes+0.2