#!/usr/bin/env python
from std_msgs.msg import String,Int32MultiArray,Bool
import rospy
from candyPicker.msg import arrayCoord

class imageToPhysical_node():
    def __init__(self):
        rospy.init_node('imageToPhysical_node', anonymous=True)
        rospy.Subscriber("MMsPixelCoord", arrayCoord, self.callbackMM)
        rospy.Subscriber("refPixelCoord", Int32MultiArray, self.callbackRef)
        rospy.Subscriber("fullyErrect", Bool, self.callbackRef)
        self.physicalCoord_publisher = rospy.Publisher("physicalCoord", arrayCoord)
        rospy.spin()
        
    def callbackMM(self, message):
        print "CallBack_imageToPhysical"
	a = arrayCoord()
	a.arrayCoord = [10,3,20]
        self.physicalCoord_publisher.publish(a)
        
    def callbackRef(message):
        print message  
    
    def callbackFullyErrect(info, message):
        print message
        
if __name__ == "__main__":
    node = imageToPhysical_node()
    
