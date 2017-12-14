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
        self.MessagePublisher = rospy.Publisher("messageHandling", String)
        
        self.refCoord = [0,0]
        rospy.spin()
        
    def callbackMM(self, message):
        print "CallBack_imageToPhysical \r"
        print message, "\r"
        if self.refCoord != [0, 0]: 
            self.pixel2physical = pixelCoord2PhysicalCoord.pixelCoord2PhysicalCoord(self.refCoord)    
            Y, X, des_Y,des_X   = self.pixel2physical.pixel2Metric(message.data)
            physicalCoord = arrayCoord()
            physicalCoord.data = [X*100,-Y*100, 0.7,des_X*100,des_Y*100,7]      
            self.physicalCoord_publisher.publish(physicalCoord)
            
        else:
            self.MessagePublisher("Please take a ref picture before using the robot \n")
        
    def callbackRef(self, message):
        print message 
        self.refCoord = message.data
    
    def callbackFullyErrect(info, message):
        print message, "\r"
        
if __name__ == "__main__":
    node = imageToPhysical_node()
    
