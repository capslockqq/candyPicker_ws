#!/usr/bin/env python
from std_msgs.msg import String,Int32MultiArray,Bool
import rospy

class imageToPhysical_node():
    def __init__(self):
        rospy.init_node('imageToPhysical_node', anonymous=True)
        rospy.Subscriber("MMsPixelCoord", Int32MultiArray, self.callbackMM)
        rospy.Subscriber("refPixelCoord", Int32MultiArray, self.callbackRef)
        rospy.Subscriber("fullyErrect", Bool, self.callbackRef)
        self.physicalCoord_publisher = rospy.Publisher("physicalCoord", Int32MultiArray)
        rospy.spin()
        
    def callbackMM(self, message):
        print "CallBack_imageToPhysical" 
        self.physicalCoord_publisher.publish([10,10])
        
    def callbackRef(message):
        print message  
    
    def callbackFullyErrect(info, message):
        print message
        
if __name__ == "__main__":
    node = imageToPhysical_node()
    