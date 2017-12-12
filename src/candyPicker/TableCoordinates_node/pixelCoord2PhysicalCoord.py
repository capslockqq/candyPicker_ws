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
        delta_x = (self.Z*delta_r*self.Sx)/self.focal
        delta_y = (self.Z*delta_c*self.Sy)/self.focal
        
        return self.refx-delta_x, self.refy-delta_y