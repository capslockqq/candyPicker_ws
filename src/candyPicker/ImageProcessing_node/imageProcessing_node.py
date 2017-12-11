#!/usr/bin/env python
from std_msgs.msg import Int32MultiArray, String, Bool
import rospy

class imageProcessing_node():
    def __init__(self):
        rospy.init_node('ImageProcessing_node', anonymous=True)
        rospy.Subscriber("sort", String, self.callbackSort)
        rospy.Subscriber("doneMoving", Bool, self.callbackDoneMoving)
        #Publish pixel coordinate to the tablecoord, to make the pixel into real life coordinates
        self.MMsPixelCord_publisher = rospy.Publisher("MMsPixelCoord", Int32MultiArray)
        #Used for calibrating the cameras coordinate system
        self.refPixelCord_publisher = rospy.Publisher("refPixelCoord", Int32MultiArray)
        
        self.AllowedToProcessImage = False
        rospy.spin()
        
        
    def callbackSort(info, message):
        #if (self.AllowedToProcessImage == True):
            print "imageProc callback function"
            MMsPixelCord_publisher.Publish([10,10,10])
            
    def callbackDoneMoving(info, message):
        self.AllowedToProcessImage = True

if __name__ == "__main__":
    node = imageProcessing_node()
