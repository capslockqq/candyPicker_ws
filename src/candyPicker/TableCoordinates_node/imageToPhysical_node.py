#!/usr/bin/env python
from std_msgs.msg import String,Int32MultiArray,Bool
import rospy
from candyPicker.msg import arrayCoord
import pixelCoord2PhysicalCoord
class imageToPhysical_node():
    def __init__(self):
        rospy.init_node('imageToPhysical_node', anonymous=True)
        rospy.Subscriber("MMsPixelCoord", arrayCoord, self.callbackMM)
        rospy.Subscriber("refPixelCoord", arrayCoord, self.callbackRef)
        rospy.Subscriber("fullyErrect", Bool, self.callbackFullyErrect)
        self.physicalCoord_publisher = rospy.Publisher("physicalCoord", arrayCoord)
        
        self.refCoord = [0,0]
        rospy.spin()
        
    def callbackMM(self, message):
        print "CallBack_imageToPhysical \r"
        print message, "\r"
        if self.refCoord != [0, 0]: 
            self.pixel2physical = pixelCoord2PhysicalCoord.pixelCoord2PhysicalCoord(message.data)    
            X, Y = self.pixel2physical.pixel2Metric(message.data)
            physicalCoord = arrayCoord()
            physicalCoord.data = [X,Y, 0]      
            self.physicalCoord_publisher.publish(physicalCoord)
        
    def callbackRef(self, message):
        print message 
        self.refCoord = message.data
    
    def callbackFullyErrect(info, message):
        print message, "\r"
        
if __name__ == "__main__":
    node = imageToPhysical_node()
    
