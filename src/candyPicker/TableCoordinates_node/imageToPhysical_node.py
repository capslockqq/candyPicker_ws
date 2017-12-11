#!/usr/bin/env python
from std_msgs.msg import String,Int32MultiArray
import rospy

class imageToPhysical_node():
    def __init__(self):
        rospy.init_node('imageToPhysical_node', anonymous=True)
        rospy.Subscriber("MMsPixelCoord", String, self.callbackMM)
        rospy.Subscriber("refPixelCoord", String, self.callbackRef)
        rospy.Subscriber("fullyErrect", String, self.callbackRef)
        self.physicalCoord_publisher = rospy.Publisher("physicalCoord", Int32MultiArray)
        rospy.spin()
        
    def callbackMM(info, message):
        print "CallBack_imageToPhysical" 
        self.physicalCoord_publisher.publish([10,10])
        
    def callbackRef(info, message):
        print message  
    
    def callbackFullyErrect(info, message):
        print message
        
if __name__ == "__main__":
    node = imageToPhysical_node()
    