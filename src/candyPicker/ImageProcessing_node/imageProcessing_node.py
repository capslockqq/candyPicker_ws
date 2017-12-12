#!/usr/bin/env python
from std_msgs.msg import Int32MultiArray, String, Bool
import rospy
from candyPicker.msg import arrayCoord
import processRawImg
import DetectMM
import numpy as np

class imageProcessing_node():
    def __init__(self):
        rospy.init_node('ImageProcessing_node', anonymous=True)
        rospy.Subscriber("sort", String, self.callbackSort)
        rospy.Subscriber("doneMoving", Bool, self.callbackDoneMoving)
        #Publish pixel coordinate to the tablecoord, to make the pixel into real life coordinates
        self.MMsPixelCord_publisher = rospy.Publisher("MMsPixelCoord", arrayCoord)
        #Used for calibrating the cameras coordinate system
        self.refPixelCord_publisher = rospy.Publisher("refPixelCoord", arrayCoord)
        self.processImgObject = processRawImg.processRawImg()
        self.detectedMMrPixelCoord = DetectMM.DetectMM()
        self.AllowedToProcessImage = False
        
        rospy.spin()
        
        
    def callbackSort(self, message):
        #if (self.AllowedToProcessImage == True):
        print "imageProc callback function \r"
        pixelCoord = arrayCoord()

        processedSingleColorImg = self.processImgObject.getProcessedImg(message.data)
        x,y = self.detectedMMrPixelCoord.getMMs(processedSingleColorImg)
        pixelCoord.data = [x, y]
        self.MMsPixelCord_publisher.publish(pixelCoord)
            
    def callbackDoneMoving(self, message):
        self.AllowedToProcessImage = True

if __name__ == "__main__":
    node = imageProcessing_node()
