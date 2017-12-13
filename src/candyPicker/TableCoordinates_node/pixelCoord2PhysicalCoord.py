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
        print "Ref coords: ", self.refx, self.refy, "\r"
        delta_r = self.refx - coordinates[0]
        delta_c = self.refy - coordinates[1] - 70
        print delta_r, delta_c
        delta_x = (self.Z*delta_r*self.Sx)/self.focalLength
        delta_y = (self.Z*delta_c*self.Sy)/self.focalLength
        
        print delta_x,delta_y+0.02
        return delta_x, delta_y+0.2