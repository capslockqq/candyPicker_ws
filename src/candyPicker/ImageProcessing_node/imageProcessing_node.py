#!/usr/bin/env python
from std_msgs.msg import Int32MultiArray, String, Bool
import rospy
from candyPicker.msg import arrayCoord
import processRawImg
import DetectMM
import DetectRefobj
import numpy as np



class imageProcessing_node():
    def __init__(self):
        rospy.init_node('ImageProcessing_node', anonymous=True)
        rospy.Subscriber("sort", String, self.callbackSort)
        rospy.Subscriber("doneMoving", Bool, self.callbackDoneMoving)
        rospy.Subscriber("refSetup",Bool,self.callbackRef)
        #Publish pixel coordinate to the tablecoord, to make the pixel into real life coordinates
        self.MMsPixelCord_publisher = rospy.Publisher("MMsPixelCoord", arrayCoord)
        self.MMsMessageHandling = rospy.Publisher("messageHandling", String)
        #Used for calibrating the cameras coordinate system
        self.refPixelCord_publisher = rospy.Publisher("refPixelCoord", arrayCoord)
        self.processImgObject = processRawImg.processRawImg()
        self.processImgObjectRef = processRawImg.processRawImg()
        self.detectedMMrPixelCoord = DetectMM.DetectMM()
        self.detectedRefPixelCoord = DetectRefobj.DetectRefobj()
        self.detectedDesCoord = DetectMM.DetectMM()
        self.AllowedToProcessImage = Bool()
        self.AllowedToProcessImage.data = True
        
        self.color = "Yellow"
        
        rospy.spin()
        
        
    def callbackRef(self,message):
        xref,yref = self.detectedRefPixelCoord.getRef()
        if (xref > 0 and yref > 0):
            pixelCoord = arrayCoord()
            pixelCoord.data = [xref, yref]
            self.refPixelCord_publisher.publish(pixelCoord)
            self.MMsMessageHandling.publish("Camera calibrated successfully")
        
        else:
            self.MMsMessageHandling.publish("No reference objcect to be found, please try again")
    
    def callbackSort(self, message):
        #if (self.AllowedToProcessImage == True):
        self.color = message.data
        
        self.callbackDoneMoving(self.AllowedToProcessImage)
            
    def callbackDoneMoving(self, message):

        
        self.timesCalled = 1
                
        self.proccessImage()
            
    def proccessImage(self):
        pixelCoord = arrayCoord()
        while (self.timesCalled <= 5):
            processedSingleColorImg = self.processImgObject.getProcessedImg(self.color)
            x_des,y_des =  self.detectedDesCoord.getDesCoord(self.color)
            x,y = self.detectedMMrPixelCoord.getMMs(processedSingleColorImg)
                           
            if (x > 0 and y > 0):
                pixelCoord.data = [x, y,x_des,y_des]
                self.MMsPixelCord_publisher.publish(pixelCoord)
                return
            self.timesCalled += 1
        
        self.MMsMessageHandling.publish("No more mms to be found")
        
        
            

if __name__ == "__main__":
    node = imageProcessing_node()
