#!/usr/bin/env python
from std_msgs.msg import String
import rospy

class imageProcessing_node():
    def __init__(self):
        rospy.init_node('ImageProcessing_node', anonymous=True)
        rospy.Subscriber("sort", String, self.callback)
        #Publish pixel coordinate to the tablecoord, to make the pixel into real life coordinates
        self.MMsPixelCord_publisher = rospy.Publisher("MMsPixelCord", Int32MultiArray)
        #Used for calibrating the cameras coordinate system
        self.refPixelCord_publisher = rospy.Publisher("refPixelCord", Int32MultiArray)
        
        self.AllowedToProcessImage = true
        rospy.spin()
        
        
    def callback(info, message):
        if (self.AllowedToProcessImage == true):
            self.array = [12,23,45]
            MMS.PixelCord_publisher.Publish(self.array)

if __name__ == "__main__":
    node = imageProcessing_node()
